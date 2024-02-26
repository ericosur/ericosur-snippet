#!/usr/bin/env python3
# coding: utf-8

'''
get water reservoir
https://steam.oxxostudio.tw/category/python/spider/beautiful-soup.html#a3

The browser could get the current data, but this script seems to get test
data only.
'''


import requests
from bs4 import BeautifulSoup

def save2file(the_str, ofn):
    ''' save to file '''
    with open(ofn, 'wt', encoding='UTF-8') as fobj:
        print(the_str, file=fobj)
    print(f'save to {ofn}')

def do_query():
    ''' perform query '''
    url = 'https://water.taiwanstat.com/'
    web = requests.get(url, timeout=5)
    save2file(web.text, "web.txt")
    soup = BeautifulSoup(web.text, "html.parser")
    reservoir = soup.select('.reservoir')     # 取得所有 class 為 reservoir 的 tag
    for i in reservoir:
        print(i.find('div', class_='name').get_text(), end=' ')  # 取得內容的 class 為 name 的 div 文字
        print(i.find('h5').get_text(), end=' ')   # 取得內容 h5 tag 的文字
        print()

def main():
    ''' main '''
    do_query()

if __name__ == '__main__':
    main()
