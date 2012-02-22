
import re
def re_show(pat, s):
    print re.compile(pat, re.M).sub("{\g<0>}", s.rstrip()),'\n'

s = '''Mary had a little lamb
And everywhere that Mary
went, the lamb was sure
to go'''

re_show("\w+", s)
