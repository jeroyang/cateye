#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from collections import defaultdict
from shove import Shove

def invert_index(source_dir, store_path):
    """
    Build the invert index from give source_dir
    Output a Shove object built on the store_path
    Input:
        source_dir: a directory on the filesystem
        store_path: store_path for the Shove object
    Output:
        index: a Shove object
    """
    raw_index = defaultdict(list)
    for base, dir_list, fn_list in os.walk(source_dir):
        for fn in fn_list:
            fp = os.path.join(base, fn)
            code = fn
            with open(fp) as f:
                tokens = f.read().strip().split('\n')
                for token in tokens:
                    raw_index[token].append(code)
    index = Shove(store=store_path)
    index.update(raw_index)
    index.sync()
    return index
