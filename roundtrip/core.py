#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from mtranslate import translate

if os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') is not None:
    from google.cloud import translate as gtranslate
    translate_client = gtranslate.Client()
    USE_OFFICIAL = True
else:
    USE_OFFICIAL = False

def backtranslate(phrase, to_language="auto", from_language="auto"):
    """Returns the translation using google translate
    you must shortcut the language you define
    (French = fr, English = en, Spanish = es, etc...)
    if not defined it will detect it or use english by default
    Example:
    print(backtranslate("Returns the translation using google translate you must shortcut the language you define",\
        "fr"))
    > Returns the translation using Google Translate, you must shorten the language you set
    """

    if not USE_OFFICIAL:
        """By default, we use the exposed unofficial API
        this is to make it easy to use from the CLI for testing
        """
        trans = translate(phrase, to_language=to_language, from_language=from_language)
        back = translate(trans, to_language=from_language, from_language=to_language)
        return back
    else:
        """However, if you want to use this at a large scale,
        you'll get banned if you don't use it the official way
        """
        translation = translate_client.translate(
            phrase,
            target_language=to_language)
        back = translate_client.translate(
            translation,
            target_language=from_language)
        return back
