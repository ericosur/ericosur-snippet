#!/usr/bin/python
# -*- coding: utf-8 -*-

str = '黿鼇龜鼈竈黿鼇龜鼈竈黿鼇龜鼈竈'
for cc in list(str.decode("utf8")):
    #print cc,"\n"
    print cc, cc.encode('unicode-escape'),
    for hh in list(cc.encode('utf8')):
        print hex(ord(hh)),
    print
