#!/usr/bin/env python
# coding: utf-8

'''
https://pi.delivery/

```
$ curl 'https://api.pi.delivery/v1/pi?start=0&numberOfDigits=100'
```

related post:
https://cloud.google.com/blog/products/compute/calculating-31-4-trillion-digits-of-archimedes-constant-on-google-cloud

31,415,926,535,897 (or pi * 10^13)

independently verified the calculation using Bellard's formula and BBP formula.
Here are the last 97 digits of the result.

6394399712 5311093276 9814355656 1840037499 3573460992
1433955296 8972122477 1577728930 8427323262 4739940

'''

import time

import requests

#from httpbin import show_results

def do_request(the_max):
    ''' query ip '''
    url = 'https://api.pi.delivery/v1/pi'
    start = 1
    if the_max >= 9:
        start = the_max - 10 + 1
    request_len = 10
    payload = {
        'start': start,
        'numberOfDigits': request_len
    }
    r = requests.get(url, payload)
    return r.json()['content']

def main():
    ''' main '''
    req_list = [0, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13, 31415926535897]
    for n in req_list:
        r = int(n)
        ans = do_request(r)
        print('pos {}: {}'.format(r, ans))
        # I do not know if such server would block massive continuous requests
        # so make a little sleep
        time.sleep(1.57)


if __name__ == '__main__':
    main()
