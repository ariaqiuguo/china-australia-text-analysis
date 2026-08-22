# China-Australia Official-Text Analysis

A reproducible portfolio demonstration for collecting, cleaning, and analysing public official texts concerning China-Australia relations.

## Research purpose

The project shows how dynamically rendered search results can be converted into an auditable text corpus. It combines browser-based discovery, article extraction, passage filtering, transparent dictionary measures, and summary outputs.

## What this repository demonstrates

- JavaScript-rendered search discovery with Playwright
- HTML extraction with Requests and Beautiful Soup
- URL normalization and deduplication
- Chinese text cleaning and keyword-based passage selection
- Transparent issue and cooperation indicators
- Reproducible CSV outputs and data-quality checks

## Repository structure

```text
data/               Small synthetic/public-format example
notebooks/          Cleaned research notebook with outputs removed
src/                Reusable text-processing functions
tests/              Unit tests for core transformations
```

## Quick start

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests
python src/text_pipeline.py data/sample_documents.csv output/analysis.csv
```

The crawler notebook should be run slowly and only where collection is permitted. Website structure can change; selectors and access rules must be checked before use.

## Data and ethics

The repository contains no private or licensed research data. The example dataset is synthetic and exists only to demonstrate the expected schema. Researchers remain responsible for website terms, robots policies, rate limits, copyright, and institutional research requirements.

## Portfolio note

This public version was cleaned for demonstration: notebook outputs, machine-specific paths, debugging files, and generated corpora were excluded.
