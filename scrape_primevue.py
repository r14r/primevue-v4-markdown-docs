import os
import argparse
import time
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from markdownify import markdownify
from urllib.parse import urljoin, urlparse

# --- Configuration ---
SIDEBAR_SELECTOR = 'aside.layout-sidebar'
CONTENT_SELECTOR = 'div.doc'
RIGHT_NAV_SELECTOR = 'ul.doc-section-nav'
IMAGE_TAG = 'img'
REQUEST_DELAY_SECONDS = 1 # Delay between requests to be polite to the server
HEADERS = { # Pretend to be a browser
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# --- End Configuration ---

def get_page_html(url):
    """Fetches HTML content from a URL with error handling and delay."""
    print(f"  Fetching: {url}")
    try:
        verify=False # Disable SSL verification for simplicity
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        print(f"  Status: {response.status_code}")
        # Introduce delay *after* a successful request
        time.sleep(REQUEST_DELAY_SECONDS)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"  Error fetching {url}: {e}")
        time.sleep(REQUEST_DELAY_SECONDS) # Still delay even on error
        return None

def extract_links_from_sidebar(sidebar_html, base_url):
    """Extracts absolute URLs from anchor tags within the sidebar HTML."""
    links = set() # Use a set to avoid duplicates
    try:
        soup = BeautifulSoup(sidebar_html, 'lxml')
        sidebar_el = soup.select_one(SIDEBAR_SELECTOR) # Find sidebar within the provided HTML
        if sidebar_el:
            anchor_tags = sidebar_el.find_all('a', href=True)
            for tag in anchor_tags:
                href = tag['href']
                # Construct absolute URL
                absolute_url = urljoin(base_url, href)
                # Optional: Only include links within the same domain/path structure
                if absolute_url.startswith(base_url):
                     # Remove fragment identifiers (#) if needed
                    parsed_url = urlparse(absolute_url)
                    clean_url = parsed_url._replace(fragment="").geturl()
                    links.add(clean_url)
            print(f"  -> Found {len(links)} unique links in sidebar.")
        else:
            print("  -> Sidebar element not found in the initial page HTML.")
    except Exception as e:
        print(f"  Error extracting links from sidebar: {e}")
    return sorted(list(links)) # Return a sorted list

def extract_and_convert(html_content, is_first_file, base_url):
    """
    Extracts sidebar (if first file) and main content from HTML content,
    removes specified elements, converts to Markdown, and strips images.
    Tries different selectors for main content.
    """
    if not html_content:
        return None, None

    try:
        soup = BeautifulSoup(html_content, 'lxml')
    except Exception as e:
        print(f"  Error parsing HTML: {e}")
        return None, None

    sidebar_md = None
    content_md = None

    # 1. Extract Sidebar (only for the first file)
    if is_first_file:
        sidebar_el = soup.select_one(SIDEBAR_SELECTOR)
        if sidebar_el:
            try:
                # Make links absolute if they are relative
                for a_tag in sidebar_el.find_all('a', href=True):
                    a_tag['href'] = urljoin(base_url, a_tag['href'])
                sidebar_md = markdownify(str(sidebar_el), strip=[IMAGE_TAG], heading_style="ATX")
                print(f"  -> Sidebar converted.")
            except Exception as e:
                print(f"  -> Error converting sidebar: {e}")
        else:
            print(f"  -> Sidebar element ({SIDEBAR_SELECTOR}) not found.")

    # 2. Extract Main Content - Try multiple selectors
    # Try the selector for component pages first
    content_el = soup.select_one('div.doc-main')
    content_selector_used = 'div.doc-main'

    if not content_el:
        # If not found, try the selector for general pages
        content_el = soup.select_one('div.doc')
        content_selector_used = 'div.doc'

    if content_el:
        print(f"  -> Found main content using selector: '{content_selector_used}'")
        try:
            # Remove the right-hand navigation menu if it exists within the content
            right_nav_el = content_el.select_one(RIGHT_NAV_SELECTOR)
            if right_nav_el:
                right_nav_el.decompose()
                print(f"  -> Right navigation ({RIGHT_NAV_SELECTOR}) removed.")
            else:
                print(f"  -> Right navigation ({RIGHT_NAV_SELECTOR}) not found within content.")


            # Make internal links absolute
            for a_tag in content_el.find_all('a', href=True):
                 # Only modify relative links or links starting with /
                 if not urlparse(a_tag['href']).scheme and not a_tag['href'].startswith('#'):
                    a_tag['href'] = urljoin(base_url, a_tag['href'])

            # Convert content to Markdown, stripping images
            content_md = markdownify(str(content_el), strip=[IMAGE_TAG], heading_style="ATX")
            print(f"  -> Main content converted.")
        except Exception as e:
            print(f"  -> Error converting main content: {e}")
    else:
        # If neither selector worked
        print(f"  -> Main content element not found using selectors: 'div.doc-main' or 'div.doc'.")

    return sidebar_md, content_md

def main():
    parser = argparse.ArgumentParser(description="Scrape PrimeVue HTML documentation and convert to a single Markdown file.")
    parser.add_argument("start_url", help="The starting URL of the documentation (e.g., the introduction page).")
    parser.add_argument("output_file", help="Path for the output Markdown file.")
    # Removed input_dir and sort arguments

    args = parser.parse_args()

    start_url = args.start_url
    output_file = args.output_file
    base_url = urlparse(start_url)._replace(path='/', params='', query='', fragment='').geturl() # Get base e.g., https://primevue.org/

    print(f"Starting scrape from: {start_url}")
    print(f"Base URL detected: {base_url}")

    # 1. Fetch the starting page to get the sidebar links
    print("Fetching starting page to extract navigation links...")
    initial_html = get_page_html(start_url)
    if not initial_html:
        print("Failed to fetch the starting page. Exiting.")
        return

    # 2. Extract all unique URLs from the sidebar
    page_urls = extract_links_from_sidebar(initial_html, base_url)
    if not page_urls:
        print("Could not extract any links from the sidebar. Trying only the start URL.")
        page_urls = [start_url]
    elif start_url not in page_urls:
         # Ensure the start page itself is included if not found via sidebar link
         page_urls.insert(0, start_url)


    print(f"Found {len(page_urls)} URLs to process:")
    # for url in page_urls: print(f"- {url}") # Uncomment to see all URLs

    final_sidebar_md = None
    all_content_md = []
    is_first = True

    # 3. Iterate through URLs, fetch content, convert
    for i, url in enumerate(page_urls):
        print(f"\nProcessing URL {i+1}/{len(page_urls)}: {url}")
        current_html = get_page_html(url)

        if current_html:
            # Pass the base_url for link conversion
            sidebar, content = extract_and_convert(current_html, is_first, base_url)

            if is_first and sidebar:
                final_sidebar_md = sidebar
                is_first = False # Sidebar only from the very first page processed

            if content:
                all_content_md.append(content)
            else:
                print(f"  -> Warning: No main content extracted from '{url}'.")
        else:
            print(f"  -> Skipping conversion for '{url}' due to fetch error.")


    # 4. Write the combined output
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            if final_sidebar_md:
                f.write(final_sidebar_md)
                f.write("\n\n---\n\n") # Separator after sidebar
                print(f"\nSidebar written to '{output_file}'.")

            if all_content_md:
                # Join content with double newline and separator
                f.write("\n\n---\n\n".join(all_content_md))
                print(f"{len(all_content_md)} content sections written to '{output_file}'.")
            else:
                 print("No main content was successfully extracted from any page.")

        print(f"\nSuccessfully created Markdown file: '{output_file}'")

    except Exception as e:
        print(f"\nError writing output file '{output_file}': {e}")

if __name__ == "__main__":
    main()