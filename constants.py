#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

SITE_TITLE = 'Cateye'
SITE_SUBTITLE = 'A hint-enabled search engine framework'

TOKEN_FOLDER = 'data/token'
SNIPPET_FOLDER = 'data/snippet'
HINT_FOLDER = 'data/hint'

SPELLING_FILE = 'data/spelling.txt' # The formal spelling of tokens
ABBREVIATION_FILE = 'data/abbrevation.txt'
SEARCH_FREQ_JSON = 'data/search_freq.json'

INDEX_URL = 'file://index'

MAX_HINT_SMAPLING_SIZE = 100 # smaller the size, faster the system, less accurate hint
MAX_RESULT = 10 # The upper limit of the showing results

STOPCHARS = '之或及的型在與和併於，、,'

STOPWORDS =  list(string.punctuation) + [ '',  ' ', 'and', 'at', 'as', 'by',
            'for', 'due', 'from', 'in', 'into', 'of', 'or', 'the', 'to',
            'using', 'via', 'with', '伴有']
