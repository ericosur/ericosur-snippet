#!/usr/bin/env python
# coding: utf-8
#

'''
simple demo to test against https://httpbin.org/
it is a great website to test http requests
'''

import requests

def show_results(r):
    print('r.url', r.url)
    print('r.elapsed', r.elapsed)
    print('r.ok', r.ok)
    print('r.status_code', r.status_code)
    print('r.reason', r.reason)
    print('r.headers', r.headers)
    print('r.links', r.links)
    print('r.encoding', r.encoding)
    content_type = r.headers['Content-Type']
    print('Content-Type:', content_type)
    if content_type == 'application/json':
        print('r.json()', r.json())
    elif 'image' in content_type:
        # maybe not printable
        print('may not printable...')
        #print('r.content', r.content)
    elif 'text' in content_type:
        print('r.text', r.text)
    elif 'octet' in content_type:
        print('r.content', r.content)


def test0():
    url = 'https://httpbin.org/ip'
    r = requests.get(url)
    show_results(r)

def test1():
    '''
    TODO: save fetched image into file
    '''
    url = 'https://httpbin.org/image/jpeg'
    r = requests.get(url)
    show_results(r)

def test2():
    try:
        n = 3
        offset = 5
        url = 'https://httpbin.org/links/{}/{}'.format(n, offset)
        r = requests.get(url)
        show_results(r)
    except Exception as e:
        print(type(e))
        print(e.args)

def test3():
    try:
        n = 32
        url = 'https://httpbin.org/range/{}'.format(n)
        r = requests.get(url)
        show_results(r)
    except Exception as e:
        print(type(e))
        print(e.args)

def test4():
    try:
        url = 'https://httpbin.org/anything/{anything}'
        r = requests.get(url)
        show_results(r)
    except Exception as e:
        print(type(e))
        print(e.args)


def main():
    test4()
    print('-' * 60)


if __name__ == '__main__':
    main()
