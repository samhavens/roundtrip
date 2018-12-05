#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from roundtrip.core import backtranslate
import sys

USAGE = ("""Name: roundtrip
Usage:
$ roundtrip text_to_translate to_lang from_lang
from_lang is optional
to_lang is recommended
Example:
$ roundtrip "Returns the translation using google translate you must shortcut the language you define" fr
Returns the translation using Google Translate, you must shorten the language you set
""")


def main():
    if (len(sys.argv) < 3):
        print(USAGE)
        return (1)
    text = sys.argv[1]
    dest = sys.argv[2]
    if (len(sys.argv) > 3):
        src = sys.argv[3]
    else:
        src = "auto"
    print(backtranslate(text, dest, src))
    return (0)

if __name__ == '__main__':
    main()