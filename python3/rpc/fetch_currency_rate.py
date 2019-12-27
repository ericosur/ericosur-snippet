#!/usr/bin/env python3

''' fetch capi.php '''

import json
import requests

def grep_keyword(data, keyword):
    ''' grep_keyword '''
    for kk in data.keys():
        try:
            kk.index(keyword)
            print('{}: {}'.format(kk, data[kk]))
        except ValueError:
            pass

def dump_to_json(fn, data):
    ''' dump dict to file as json '''
    with open(fn, 'wt') as f:
        f.write(json.dumps(data))
    print('output to {}'.format(fn))


def main():
    ''' main '''
    r = requests.get('https://tw.rter.info/capi.php')
    currency = r.json()

    grep_keyword(currency, 'TWD')
    grep_keyword(currency, 'EUR')
    grep_keyword(currency, 'GBP')

    # fn = 'curr.json'
    # dump_to_json(fn, currency)


if __name__ == '__main__':
    main()
