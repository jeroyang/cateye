# -*- coding: utf-8 -*-
import os
import hashlib

from flask import Flask, jsonify, render_template, request
import cateye
from constants import *

application = Flask(__name__)

cm_index = cateye.Shove(INDEX_URL)


# Load spelling.txt
term_freq = cateye.load_spelling(spell_file=SPELLING_FILE)

@application.route('/_search')
def search():
    s = request.args.get('s', '')
    response, tokens, hints, hint_scores,\
    abbr_log, correct_log, fallback_log = cateye.search(cm_index, s, term_freq,
                                                snippet_folder=SNIPPET_FOLDER,
                                                hint_folder=HINT_FOLDER)
    return jsonify(render_template('response.html',
                                   result_count=len(response),
                                   response=response[:cateye.MAX_RESULT],
                                   tokens=tokens,
                                   hints=hints,
                                   abbr_log=abbr_log,
                                   correct_log=correct_log,
                                   fallback_log=fallback_log
                                   ))

@application.route('/')
def index():
    s = request.args.get('s', '')
    return render_template('index.html',
                            site_title=cateye.SITE_TITLE,
                            site_subtitle=cateye.SITE_SUBTITLE,
                            query=s,
                            )

if __name__ == '__main__':
    application.debug = True
    application.run()
