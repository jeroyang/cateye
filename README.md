# Cateye


[![](https://img.shields.io/travis/jeroyang/cateye.svg)](https://travis-ci.org/jeroyang/cateye)
[![](https://img.shields.io/pypi/v/cateye.svg)](https://pypi.python.org/pypi/cateye)

A hint enabled search engine for fixed-size documents

## Features
- Hint: Show hints for search terms which can fast narrow down the results
- Spelling correction: Build-in spelling correction
- Abbreviation expension: Pre-defined abbreviation list will be automatically applied during search

## Installation

```bash
$ python setup.py install
```

## Usage
### 1. Prepare your data:

Folders overview:
  - data: The data source for search engine, all information in this subfolders using the document id as their filenames.
  - data/token: The tokens of the documents, after lemmaization
  - data/snippet: The html snippets of the documents, which will be shown on the search results
  - data/hint: The hints for each document
  - data/spelling_correction.txt: The formal spelling of your tokens (before lemmalization). If possible, sort the tokens with frequency of usage, the most common word the first.
  - data/abbreviation.txt: The abbrevations, one line for one abbrevation pair, using tab to seprate the short form and long form

Cateye include some very basic text processing tools:
tokenizer (basic_functions.tokenize) and lemmalizer (basic_functions.lemmalize)

The tokenize function will be used in two places: the first place is to cut your documents into tokens, and the second place is to cut your query into tokens.

The lemmalize function will normalize your tokens. If you wish to build a case-insensitive search engine, you may use lowercase lemmalizer on the tokens.

### 2. Check the configuration.py:
The configuration.py setups the paths of token_folder, index_url, snippet_folder, hint_folder, abbreviation_file, and spelling_correction_file.

The index_url is used in the Shove object, which can be a remote url such as s3:// or a local url such as file:// please check the document of Shove.

### 3. Build the index:
Run command in command line
```bash
$ cateye buildindex
```
This command read the files in token_folder and build a on disk index in the index_url. It take times depends on the size of your data

### 4. Run the application:
```bash
$ FLASK_APP=app.py flask run
```

## License
* Free software: MIT license
