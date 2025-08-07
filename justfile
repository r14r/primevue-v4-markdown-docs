default:
	cat justfile

setup:
	python3.12 -m venv .venv
	python -m pip install --upgrade pip
	pip install uv

install-requirements:
	uv pip install -r requirements.txt 

install-pyproject:
	uv pip install -r pyproject.toml
	

run: 
	python scrape_primevue.py https://primevue.org/introduction/ primevue_v4_docs_latest.md

