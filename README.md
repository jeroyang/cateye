# Cateye

[![](https://img.shields.io/pypi/v/cateye.svg)](https://pypi.python.org/pypi/cateye)

Cateye is a Python framework for building real-time search engines over biomedical classification systems such as ICD-10, SNOMED CT, or any structured code set with human-readable descriptions.

Clinicians and medical coders often need to look up a code from a vague or incomplete description — a drug name, a symptom, or an abbreviation. Cateye handles the messiness of natural clinical language: it corrects typos, expands abbreviations, recovers partial matches, and learns which codes are used most often to push relevant results to the top.

The included demo runs against a set of ICD-10 respiratory codes. You can replace the data with any classification system and have a working search site in minutes.

## Features

- **Interactive hints:** As results appear, Cateye suggests related terms you can click to refine the search — useful when you know the concept but not the exact wording.
- **Graceful fallback:** When a multi-term query returns nothing, the least informative term is dropped automatically and the search retries, so users always see something useful.
- **Spelling correction:** Misspelled query terms are corrected against a frequency-ranked vocabulary before searching.
- **Abbreviation expansion:** A configurable abbreviation table maps short forms (e.g. "DM" → "diabetes mellitus") transparently during search.
- **Frequency-ranked results:** Results are sorted by a score that combines term overlap and historical search frequency, so common codes surface first.
- **CJK support:** The tokenizer handles mixed English and Chinese/Japanese/Korean text out of the box.

## Requirements

- Python 3.9+

## Installation

```bash
git clone https://github.com/jeroyang/cateye.git
cd cateye
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Usage

### 1. Run the demo site

```bash
python application.py
```

Then open http://127.0.0.1:5000/ and try searching for "rhinitis".

### 2. Build your own site

#### 2-1. Configure constants.py

Edit `constants.py` to set your paths and site metadata:

| Variable | Description |
|---|---|
| `SITE_TITLE` | HTML title shown in the header |
| `SITE_SUBTITLE` | Subtitle shown in the header |
| `TOKEN_FOLDER` | Directory containing token files (one file per entity) |
| `SNIPPET_FOLDER` | Directory containing HTML snippet files (one file per entity) |
| `HINT_FOLDER` | Directory containing hint files (one file per entity) |
| `SPELLING_FILE` | Path to the spelling reference file |
| `ABBREVIATION_FILE` | Path to the abbreviation list file |
| `INDEX_FP` | File path for the on-disk shelve index |

#### 2-2. Prepare your data

All data files use the entity's term ID as the filename.

```
data/
├── token/          # Tokenized text for each entity (one token per line)
├── snippet/        # HTML snippet shown in search results (one file per entity)
├── hint/           # Related terms for hint suggestions (one per line)
├── spelling.txt    # Reference vocabulary, sorted by frequency (most common first)
└── abbrevation.txt # Abbreviation pairs: <short form><TAB><long form>, one per line
```

Cateye provides basic text processing utilities:

- `cateye.tokenize(s)` — splits a string into tokens, handles hyphenated terms and CJK text
- `cateye.lemmatize(tokens)` — lowercases tokens for case-insensitive matching

Use these same functions when preprocessing your documents so that index and query tokens match.

#### 2-3. Build the index

```bash
cateye newindex
```

Reads all files in `TOKEN_FOLDER` and builds an on-disk index at `INDEX_FP`. To update an existing index without wiping it:

```bash
cateye updateindex
```

#### 2-4. Run your application

```bash
python application.py
```

## License

MIT
