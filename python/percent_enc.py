#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

def percent_enc(tok):
    print tok
    print urllib.quote(tok.encode("utf-8"))

'''
for unicdoe codepage 0000 to FFFF, use lower case \u, eg: u'\u1234'
for 00010000 to 0001FFFF, use upper case \U, eg: u'\U000123456'
'''
if __name__ == '__main__':
    tokens = [u"长度会有变化",
        u"\U0001f648\U0001f649\U0001f64a",
        u"\U0001F1F9\U0001F1FC"]
    for tok in tokens:
        percent_enc(tok)

