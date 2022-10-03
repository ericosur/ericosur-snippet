#!/usr/bin/python3
# coding: utf-8

'''
    curl -X POST https://api.reurl.cc/shorten \
              -H 'Content-Type: application/json' \
              -H 'reurl-api-key: YOUR_OWN_APIKEY' \
              -d '{ "url" : "https://reurl.cc", "utm_source" : "FB_AD" }'
'''

import argparse
import sys
import json
import os
import requests
import myutil

class MakeReurl():
    ''' call reurl to shorten url '''
    def __init__(self, url=None, output=sys.stderr, verbose=False):
        self.output=output
        self.verbose=verbose

        self.server = ''
        self.apikey = ''
        self._load_config()
        if url is not None:
            self.shorten(url)

    def _load_config(self) -> None:
        ''' load config '''
        h = myutil.get_home()
        p = h + '/Private/reurl.json'
        conf = myutil.read_jsonfile(p)
        self.server = conf['server']
        self.apikey = conf['apikey']

    #pylint: disable=consider-using-with
    def handle_results(self, r):
        ''' show data member of **response** '''

        if self.verbose:
            out = sys.stderr
        else:
            out = open(os.devnull, 'wb')

        content_type = r.headers['Content-Type']
        if self.verbose:
            print('r.url:', r.url, file=out)
            print('r.elapsed:', r.elapsed, file=out)
            print('r.ok:', r.ok, file=out)
            print('r.status_code:', r.status_code, file=out)
            print('r.reason:', r.reason, file=out)
            print('r.headers:', r.headers, file=out)
            #print('r.links:', r.links, file=out)
            #print('r.encoding:', r.encoding, file=out)
            print('Content-Type:', content_type, file=out)
        if 'application/json' in content_type:
            if self.verbose:
                print('r.json():', r.json(), file=out)
                #print('r.content():', r.content)
                #print('r.text():', r.text)
            if r.ok:
                return r.json()

        return None

    def do_request(self):
        ''' issue request '''
        server = f'{self.server}/shorten'
        headers = {
            'content-type': 'application/json',
            'reurl-api-key': self.apikey
        }
        j = {'url': self.long_url}


        # if self.verbose:
        #     print('will requst with:')
        #     print(headers)
        #     print(json.dumps(j))
        r = requests.post(server, data=json.dumps(j), headers=headers)
        # r is a Response class, useless to print it, use handle_results()
        j = self.handle_results(r)

        if j is None:
            print('ERROR')
            return

        out = None
        if self.output == "stdout":
            out = sys.stdout
        elif self.output == "stderr":
            out = sys.stderr
        if out is not None:
            print('short_url:', j['short_url'], file=out)
            return

        with open(self.output, 'wt', encoding='utf8') as txt:
            print('short_url:', j['short_url'], file=txt)


    def shorten(self, url=None):
        ''' shorten '''
        if url is None:
            print('shorten: url is none')
            return
        self.long_url = url
        self.do_request()


def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='reurl python script')
    parser.add_argument("url", metavar='url', type=str, nargs='+',
        help="long URL you want to shorten...")
    parser.add_argument('-o', '--output', help='Output file name', default='stdout')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')

    #parser.parse_args(['-i input.txt -o out.txt str1 str2'])

    args = parser.parse_args()

    print(args.url)
    if args.output:
        print('output:', args.output)
    if args.verbose:
        print('verbose:', args.verbose)

    _ = MakeReurl(args.url[0], output=args.output, verbose=args.verbose)

if __name__ == '__main__':
    main()
