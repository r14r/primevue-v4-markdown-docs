# Paginator

Paginator displays data in paged format and provides navigation between pages.

## Import [#](https://primevue.org/paginator/#import)

```

import Paginator from 'primevue/paginator';


```

## Basic [#](https://primevue.org/paginator/#basic)

Paginator is used as a controlled component with *first* and *rows* properties to manage the first index and number of records to display per page. Total number of records need to be with *totalRecords* property. Default template includes a dropdown to change the *rows* so *rowsPerPageOptions* is also necessary for the dropdown options.

12345

10

```

<Paginator :rows="10" :totalRecords="120" :rowsPerPageOptions="[10, 20, 30]"></Paginator>


```

## Template [#](https://primevue.org/paginator/#template)

Paginator elements can be customized using the *template* property using the predefined keys, default value is "FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink RowsPerPageDropdown". Here are the available elements that can be placed inside a paginator in any order.

* FirstPageLink
* PrevPageLink
* PageLinks
* NextPageLink
* LastPageLink
* RowsPerPageDropdown
* JumpToPageDropdown
* JumpToPageInput
* CurrentPageReport

(1 of 12)

```

<Paginator v-model:first="first" :rows="1" :totalRecords="12" template="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink" />

<div class="p-4 text-center">
    <img :src="`https://primefaces.org/cdn/primevue/images/nature/nature${first + 1}.jpg`" :alt="first" class="rounded w-full sm:w-[30rem]" />
</div>


```

## Current Page Report [#](https://primevue.org/paginator/#currentpagereport)

Current page report item in the template displays information about the pagination state. Default value is ({currentPage} of {totalPages}) whereas available placeholders are the following;

* {currentPage}
* {totalPages}
* {rows}
* {first}
* {last}
* {totalRecords}

Showing 1 to 10 of 120

```

<Paginator :rows="10" :totalRecords="120" template="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
    currentPageReportTemplate="Showing {first} to {last} of {totalRecords}" />


```

## Responsive [#](https://primevue.org/paginator/#responsive)

Paginator elements can be customized per screen size by defining a template per breakpoint. Note that breakpoints are based on max-width setting, if default key is omitted then the default template would be used. Example below has 4 settings; up to 640px, between 641px-960px, between 961px-1300px and larger than 1301px which is the default.

(1 of 12)

(1 of 12)

12345

12345

1

```

<Paginator
    :template="{
        '640px': 'PrevPageLink CurrentPageReport NextPageLink',
        '960px': 'FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink',
        '1300px': 'FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink',
        default: 'FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink JumpToPageDropdown JumpToPageInput'
    }"
    :rows="10"
    :totalRecords="120">
</Paginator>


```

## Custom Content [#](https://primevue.org/paginator/#customcontent)

There are two templates available named *start* and *end* to add custom content to these locations. Both templates get a state object as a slot property to provide the current page, first index and the rows.

Page: 0 First: 0 Rows: 10

12345

10

```

<Paginator :rows="10" :totalRecords="120" :rowsPerPageOptions="[10, 20, 30]">
    <template #start="slotProps">
        Page: {{ slotProps.state.page }}
        First: {{ slotProps.state.first }}
        Rows: {{ slotProps.state.rows }}
    </template>
    <template #end>
        <Button type="button" icon="pi pi-search" />
    </template>
</Paginator>


```

## Headless [#](https://primevue.org/paginator/#headless)

Headless mode is enabled by defining a *container* slot that lets you implement entire UI instead of the default elements. The template receives the following data;

* first
* last
* rows
* page
* pageCount
* totalRecords
* firstPageCallback
* lastPageCallback
* prevPageCallback
* nextPageCallback
* rowChangeCallback

Showing 1 to 10 of 120Page 1 of 12

```

<Paginator :rows="10" :totalRecords="120">
    <template #container="{ first, last, page, pageCount, prevPageCallback, nextPageCallback, totalRecords }">
        <div class="flex items-center gap-4 border border-primary bg-transparent rounded-full w-full py-1 px-2 justify-between">
            <Button icon="pi pi-chevron-left" rounded variant="text" @click="prevPageCallback" :disabled="page === 0" />
            <div class="text-color font-medium">
                <span class="hidden sm:block">Showing {{ first }} to {{ last }} of {{ totalRecords }}</span>
                <span class="block sm:hidden">Page {{ page + 1 }} of {{ pageCount }}</span>
            </div>
            <Button icon="pi pi-chevron-right" rounded variant="text" @click="nextPageCallback" :disabled="page === pageCount - 1" />
        </div>
    </template>
</Paginator>


```

## Accessibility [#](https://primevue.org/paginator/#accessibility)

### Screen Reader

Paginator is placed inside a *nav* element to indicate a navigation section. All of the paginator elements can be customized using templating however the default behavious is listed below.

First, previous, next and last page navigators elements with *aria-label* attributes referring to the *aria.firstPageLabel*, *aria.prevPageLabel*, *aria.nextPageLabel* and *aria.lastPageLabel* properties of the [locale](https://primevue.org/configuration/#locale) API respectively.

Page links are also button elements with an *aria-label* attribute derived from the *aria.pageLabel* of the [locale](https://primevue.org/configuration/#locale) API. Current page is marked with *aria-current* set to "page" as well.

Current page report uses *aria-live="polite"* to instruct screen reader about the changes to the pagination state.

Rows per page dropdown internally uses a dropdown component, refer to the [select](https://primevue.org/select) documentation for accessibility details. Additionally, the dropdown uses an *aria-label* from the *aria.rowsPerPageLabel* property of the [locale](https://primevue.org/configuration/#locale) API.

Jump to page input is an *input* element with an *aria-label* that refers to the *aria.jumpToPageInputLabel* property and jump to page dropdown internally uses a dropdown component, with an *aria-label* that refers to the *aria.jumpToPageDropdownLabel* property of the [locale](https://primevue.org/configuration/#locale) API.

### Keyboard Support

| Key | Function |
| --- | --- |
| *tab* | Moves focus through the paginator elements. |
| *enter* | Executes the paginator element action. |
| *space* | Executes the paginator element action. |

### Rows Per Page Dropdown Keyboard Support

Refer to the [select](https://primevue.org/select) documentation for more details about keyboard support.