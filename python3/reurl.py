#!/usr/bin/env python3

'''
    curl -X POST https://api.reurl.cc/shorten \
              -H 'Content-Type: application/json' \
              -H 'reurl-api-key: YOUR_OWN_APIKEY' \
              -d '{ "url" : "https://reurl.cc", "utm_source" : "FB_AD" }'
'''

import argparse
import os
import sys

import requests

import myutil


class MakeReurl:
    ''' call reurl to shorten url '''
    def __init__(self, url=None, output=sys.stderr, verbose=False):
        self.output = output
        self.verbose = verbose

        self.server = ''
        self.apikey = ''
        self._load_config()
        if url is not None:
            self.shorten(url)

    def _load_config(self) -> None:
        ''' load config '''
        h = myutil.get_home()
        p = os.path.join(h, 'Private', 'reurl.json')
        if os.path.exists(p):
            conf = myutil.read_jsonfile(p)
            self.server = conf['server']
            self.apikey = conf['apikey']
        else:
            print('[ERROR] conf not found, exit')
            sys.exit(1)

    #pylint: disable=consider-using-with
    def handle_results(self, r):
        '''Log response metadata in verbose mode and return parsed JSON on success.'''

        content_type = r.headers.get('Content-Type', '')

        if self.verbose:
            out = sys.stderr
            print('r.url:', r.url, file=out)
            print('r.elapsed:', r.elapsed, file=out)
            print('r.ok:', r.ok, file=out)
            print('r.status_code:', r.status_code, file=out)
            print('r.reason:', r.reason, file=out)
            print('r.headers:', r.headers, file=out)
            #print('r.links:', r.links, file=out)
            #print('r.encoding:', r.encoding, file=out)
            print('Content-Type:', content_type, file=out)

        if not r.ok or 'application/json' not in content_type:
            return None

        try:
            payload = r.json()
        except ValueError:
            if self.verbose:
                print('r.json(): <invalid json>', file=sys.stderr)
            return None

        if self.verbose:
            print('r.json():', payload, file=sys.stderr)
            #print('r.content():', r.content)
            #print('r.text():', r.text)

        return payload

    def do_request(self):
        ''' issue request '''
        server = f'{self.server}/shorten'
        headers = {
            'content-type': 'application/json',
            'reurl-api-key': self.apikey
        }
        payload = {'url': self.long_url}


        # if self.verbose:
        #     print('will requst with:')
        #     print(headers)
        #     print(json.dumps(payload))
        try:
            response = requests.post(server, json=payload, headers=headers, timeout=5.0)
            # response is a Response class, use handle_results() for details.
            result = self.handle_results(response)
        except ConnectionError as e:
            print(e)
            return

        if result is None:
            print('ERROR')
            return

        if self.output == "stdout":
            print('short_url:', result['short_url'], file=sys.stdout)
            return
        elif self.output == "stderr":
            print('short_url:', result['short_url'], file=sys.stderr)
            return

        if not isinstance(self.output, str):
            print('ERROR')
            return

        with open(self.output, 'wt', encoding='utf8') as txt:
            print('short_url:', result['short_url'], file=txt)


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
