#!/usr/bin/env python3
# coding: utf-8

'''
script to solve Python Chanllenge #4
'''

from urllib.request import urlopen
import re

def get_web(url):
    ''' get web '''
    print("get_web: ", url)
    web = urlopen(url)
    content = web.read()
    return content

def main():
    ''' main '''
    cnt = 0
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=46059"
    while url and cnt < 200:
        cnt += 1
        print("cnt = ", cnt,)
        cont = get_web(url)
        url = None
        #if cnt > 1: print cont
        for line in cont.splitlines():
            m0 = re.search('Yes', line)
            if m0:
                print(cont)
                break
            m = re.search(r'and the next nothing is (\d+)', line)
            if m:
                print("match: ", m.group(1))
                url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + m.group(1)
                print("try to get: ", url)
                break

if __name__ == '__main__':
    main()
