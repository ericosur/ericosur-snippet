#!/usr/bin/env python
# coding: utf-8
#

'''
simple demo to test against https://httpbin.org/
it is a great website to test http requests

its docker:
docker run -p 80:80 kennethreitz/httpbin
'''


from __future__ import print_function

import time

import requests


def show_results(r):
    ''' show data member of **response** '''
    print('r.url:', r.url)
    print('r.elapsed:', r.elapsed)
    print('r.ok:', r.ok)
    print('r.status_code:', r.status_code)
    print('r.reason:', r.reason)
    print('r.headers:', r.headers)
    print('r.links:', r.links)
    print('r.encoding:', r.encoding)
    content_type = r.headers['Content-Type']
    print('Content-Type:', content_type)
    if content_type == 'application/json':
        print('r.json():', r.json())
    elif 'image' in content_type:
        # maybe not printable
        print('may not printable...')
        #print('r.content', r.content)
        epoch = time.time()
        fn = content_type.replace('/', f'-{epoch:.0f}.')
        # will overwrite if file exists
        with open(fn, 'wb') as ofh:
            ofh.write(r.content)
        print('save content into:', fn)
        return fn
    elif 'text' in content_type:
        print('r.text:', r.text)
    elif 'octet' in content_type:
        print('r.content:', r.content)
    return None

class TestHttpbin():
    ''' class test httpbin '''
    server = 'https://httpbin.org'

    def __init__(self):
        pass

    def test_url(self, subcmd: str) -> None:
        ''' test with given subcmd '''
        url = f'{self.server}/{subcmd}'
        r = requests.get(url, timeout=5.0)
        show_results(r)

    def test_getip(self):
        ''' query ip '''
        self.test_url('ip')

    def test_jpeg(self):
        ''' request an image '''
        self.test_url('image/jpeg')


    def run(self):
        ''' run '''
        self.test_getip()
        print('-' * 48)
        self.test_jpeg()
        print('-' * 48)

def test2():
    '''
    fetch links
    '''
    try:
        n = 3
        offset = 5
        url = f'https://httpbin.org/links/{n}/{offset}'
        r = requests.get(url, timeout=5.0)
        show_results(r)
    except ConnectionError as e:
        print(f"type: {type(e)}, args: {e.args}")

def test3():
    '''
    fetch numbers
    '''
    try:
        n = 32
        url = f'https://httpbin.org/range/{n}'
        r = requests.get(url, timeout=5.0)
        show_results(r)
    except ConnectionError as e:
        print(f"type: {type(e)}, args: {e.args}")

def test4():
    '''
    fetch anything
    '''
    try:
        url = 'https://httpbin.org/anything/{anything}' # it isn't a f-string
        r = requests.get(url, timeout=5.0)
        show_results(r)
    except ConnectionError as e:
        print(f"type: {type(e)}, args: {e.args}")

def test_post():
    ''' test post '''
    print("test_post() =========>")
    url = 'https://httpbin.org/post'
    r = requests.post(url, timeout=5.0)
    show_results(r)

def main():
    ''' main test function '''
    # httpbin = TestHttpbin()
    # httpbin.run()
    test_post()

if __name__ == '__main__':
    main()
