#!/usr/bin/env python3
# coding: utf-8

'''
refer to:
https://www.dropbox.com/s/91w40oxq9eftrn1/%E8%9E%A2%E5%B9%95%E6%88%AA%E5%9C%96%202014-10-09%2009.52.19.png?dl=0
'''

import cgi


def main():
    ''' main '''
    form = cgi.FieldStorage()

    val1 = form.getvalue('first')
    val2 = form.getvalue('last')

    print(f"""Content-type: text/html

<html><head><title>Test URL Encoding</title></head>
<body>Hello my name is {val1} {val2}
</body></html>""")

if __name__ == '__main__':
    main()
