#!/usr/bin/python

import base64

hellostr = "Hello Python!"

b64 = base64.encodestring(hellostr)
print type(b64), b64
print base64.decodestring(b64)

b64 = base64.b64encode(hellostr)
print type(b64), b64
print base64.b64decode(b64)

inf = open("rnd.bin", "r")
ouf = open("out.b64", "w")

base64.encode(inf, ouf)


