#!/usr/bin/env python
# coding: utf-8
#

'''
simple demo to test against https://httpbin.org/
it is a great website to test http requests
'''


from __future__ import print_function
import requests

def show_results(r):
    ''' show data member of **response** '''
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
        fn = content_type.replace('/', '.')
        with open(fn, 'wb') as ofh:
            ofh.write(r.content)
        print('save content into', fn)
        return fn
    elif 'text' in content_type:
        print('r.text', r.text)
    elif 'octet' in content_type:
        print('r.content', r.content)
    return None

def test0():
    ''' query ip '''
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
    '''
    fetch links
    '''
    try:
        n = 3
        offset = 5
        url = 'https://httpbin.org/links/{}/{}'.format(n, offset)
        r = requests.get(url)
        show_results(r)
    except ConnectionError as e:
        print("type: {}, args: {}".format(type(e), e.args))

def test3():
    '''
    fetch numbers
    '''
    try:
        n = 32
        url = 'https://httpbin.org/range/{}'.format(n)
        r = requests.get(url)
        show_results(r)
    except ConnectionError as e:
        print("type: {}, args: {}".format(type(e), e.args))

def test4():
    '''
    fetch anything
    '''
    try:
        url = 'https://httpbin.org/anything/{anything}'
        r = requests.get(url)
        show_results(r)
    except ConnectionError as e:
        print("type: {}, args: {}".format(type(e), e.args))


def main():
    ''' main test function '''
    test4()
    print('-' * 60)


if __name__ == '__main__':
    main()
