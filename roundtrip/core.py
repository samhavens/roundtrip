#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate

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

    trans = translate(phrase, to_language=to_language, from_language=from_language)
    back = translate(trans, to_language=from_language, from_language=to_language)
    return back

