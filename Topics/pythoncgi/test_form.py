#!/usr/bin/env python3
# coding: utf-8

'''
refer to:
http://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-2/
'''

import cgi

def main():
    ''' main '''
    form = cgi.FieldStorage()
    val1 = form.getvalue('comments')
    msg = """Content-type: text/html

    The form input is below...</br>"""

    print(msg)
    print(val1)

if __name__ == '__main__':
    main()
