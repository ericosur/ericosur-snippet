#!/usr/bin/env python

def show_utf8char(ch):
    uch = ch.decode('utf8')
    print uch
    print 'len: ', len(uch)
    # not work if codepoint > 0xffff
    #print 'hex: ', hex(ord(uch))
    print 'uen: ', uch.encode('unicode-escape')
    print


# utf8 octets for apple logo (private use area)
# utf8: EF A3 BF
# U+F8FF

a = '\xef\xa3\xbf'
show_utf8char(a)

b = '\xF0\x9F\x90\xB1'
show_utf8char(b)

# U+F92F (CJK Compatibility Ideographs)
print u'\uF92F'

# U+52DE (CJK Unified Ideographs)
print u'\u52DE'