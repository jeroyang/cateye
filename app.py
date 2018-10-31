#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import cateye

application = Flask(__name__)

the_index = cateye.Shove('file://index')

@application.route('/_search')
def search():
    s = request.args.get('s', '')
    response, tokens, hints, hint_scores,\
    abbr_log, correct_log, fallback_log = cateye.search(the_index, s)
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
    return render_template('index.html',
                            site_title=cateye.SITE_TITLE,
                            site_subtitle=cateye.SITE_SUBTITLE
                            )

if __name__ == '__main__':
    application.run()
