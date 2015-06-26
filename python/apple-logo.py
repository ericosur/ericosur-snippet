#!/usr/bin/env python

# utf8 octets for apple logo (private use area)
# utf8: EF A3 BF
# U+F8FF

a = '\xef\xa3\xbf'
ua = a.decode('utf8')

print ua
print hex(ord(ua))
