#!/usr/bin/env python3
# coding: utf-8

''' try requests to download imgur image '''

import requests


def show_results(r):
    ''' show data member of **response** '''
    print('r.url', r.url)
    #print('r.elapsed', r.elapsed)
    print('r.ok', r.ok)
    print('r.status_code', r.status_code)
    print('r.reason', r.reason)
    print('r.headers', r.headers)
    #print('r.links', r.links)
    #print('r.encoding', r.encoding)
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
        print('[INFO] save content into', fn)
        return fn
    elif 'text' in content_type:
        print('r.text', r.text)
    elif 'octet' in content_type:
        print('r.content', r.content)
    return None

def getimg(url):
    '''
    TODO: save fetched image into file
    '''
    r = requests.get(url, timeout=5.0)
    show_results(r)


def main():
    ''' main '''
    getimg('https://i.imgur.com/H0WsDJgs.jpg')


if __name__ == '__main__':
    main()
