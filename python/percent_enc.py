#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

def percent_enc(tok):
    print( tok )
    print( urllib.quote(tok.encode("utf-8")) )


'''
for unicdoe codepage 0000 to FFFF, use lower case \u, eg: u'\u1234'
for 00010000 to 0001FFFF, use upper case \U, eg: u'\U00012345'
'''
def main():
    tokens = [
        u"\u00A1 \u00BF",
        u"\u00C0 \u00C1 \u00C2 \u00C3 \u00C4 \u00C5 \u00C6",
        u"\u00E0 \u00E1 \u00E2 \u00E3 \u00E4 \u00E5 \u00E6",
        u"\u00C7 \u00C8 \u00C9 \u00CA \u00CB",
        u"\u00CC \u00CD \u00CE \u00CF",
        u"\u00D0 \u00D1 \u00DD \u00DE",
        u"\u00D2 \u00D3 \u00D4 \u00D5 \u00D6 \u00D8",
        u"\u00D9 \u00DA \u00DB \u00DC",

        u"长度会有变化",
        u"\U0001f648\U0001f649\U0001f64a",
        u"\U0001F1F9\U0001F1FC"
    ]

    for tok in tokens:
        percent_enc(tok)


if __name__ == '__main__':
    main()
