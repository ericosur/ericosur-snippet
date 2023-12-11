#!/usr/bin/env python3
# coding: utf-8

'''
refer to:
http://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
'''

import sys

try:
    import cgitb

    import BaseHTTPServer
    import CGIHTTPServer
    cgitb.enable()  ## This line enables CGI error reporting
except ImportError:
    print('cannot import related modules...')
    sys.exit(1)

def main():
    ''' main '''
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    server_address = ("", 8000)
    handler.cgi_directories = ["/"]

    httpd = server(server_address, handler)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
