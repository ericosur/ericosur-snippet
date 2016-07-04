#!/usr/bin/env python

# refer to:
# http://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-2/

import cgi

form = cgi.FieldStorage()
val1 = form.getvalue('comments')
print """Content-type: text/html

The form input is below...</br>"""

print val1

