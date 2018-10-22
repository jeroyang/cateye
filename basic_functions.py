#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import string
from constants import STOPCHARS, STOPWORDS

def gen_path(base, code):
    return os.path.join(base, code[:2], code[:3])

def tokenize(s):
    s = re.sub(r'(?a)(\w+)\'s', r'\1', s) # clean the 's from Crohn's disease
    s = re.sub(r'(?a)\b', ' ', s) # split the borders of chinese and english chars

    split_pattern = r'[{} ]+'.format(STOPCHARS)

    tokens = []
    for snippet in re.split(split_pattern, s):
        if set(snippet) <= set(string.printable): # not chinese snippet
            tokens.append(snippet)
        else: # has chinese char
            tokens.extend(k_mer(snippet))
    return tokens

def lemmalize(tokens):
    return [token.lower() for token in tokens]

def filterout(tokens):
    return [token for token in tokens if token not in STOPWORDS]

def fetch(index, tokens):
    return set.intersection(*[set(index[token]) for token in tokens])

def get_snippets(base, code_list):
    output = []
    for code in code_list:
        path = gen_path(base, code)
        fp = os.path.join(path, code)
        with open(fp) as f:
            output.append(f.read())
    return output

def search(index, query, base):
    tokens = tokenize(query)
    tokens = lemmalize(tokens)
    tokens = filterout(tokens)
    code_list = fetch(index, tokens)
    return code_list, get_snippets(base, code_list)

def fingerprint(index):
    keys = ['right', 'upper', 'device']
    return ([(k, len(index['cm'][k])) for k in keys],
     [(k, len(index['pcs'][k])) for k in keys])
