# Cateye

A hint-enabled search engine framework for biomedical classification systems

[![Build Status](https://travis-ci.org/jeroyang/cateye.svg?branch=master)](https://travis-ci.org/jeroyang/cateye)

## Features
- Hint: Show hints for search terms which can fast narrow down the results
- Automatic fallback: If no result satisfying the query, the system automatically eliminates less important search terms.
- Spelling correction: Build-in spelling correction
- Abbreviation expansion: Pre-defined abbreviation list will be automatically applied during the search

## Installation

```bash
$ python setup.py install
```

## Usage
### 1. Prepare your data:

Folders overview:
  - data: The data source for the search engine, all information in this subfolders using the document id as their filenames.
  - data/token: The tokens of the documents, after lemmatization
  - data/snippet: The HTML snippets of the documents, which will be shown on the search results
  - data/hint: The hints for each document
  - data/spelling.txt: The formal spelling of your tokens (before normalization). If possible, sort the tokens with the frequency of usage, the most common word the first.
  - data/abbreviation.txt: The abbreviations, one line for one abbreviation pair, using tab to separate the short form and long form

Cateye include some very basic text processing tools:
tokenizer (basic_functions.tokenize) and lemmalizer (basic_functions.lemmalize)

The tokenize function will be used in two places: the first place is to cut your documents into tokens, and the second place is to cut your query into tokens.

The lemmatizing function will normalize your tokens. If you wish to build a case-insensitive search engine, you may use lowercase lemmatizer on the tokens.

### 2. Check the configuration.py:
The configuration.py setups the paths of token_folder, index_url, snippet_folder, hint_folder, abbreviation_file, and spelling_correction_file.

The index_url is used in the Shove object, which can be a remote URL starts with s3:// or a local URL starts with file:// please check the document of [Shove](https://pypi.org/project/shove/).

### 3. Build the index:
Run command in the command line
```bash
$ cateye buildindex
```
This command read the files in token_folder and build an on-disk index in the index_url. It takes times depends on the size of your data

### 4. Run the application:
```bash
$ FLASK_APP=app.py flask run
```

## License
* Free software: MIT license
