#!/usr/bin/env python3
# coding: utf-8

'''
a list full of free API service
https://github.com/public-apis/public-apis#anime

https://ghibliapi.herokuapp.com/#section/Studio-Ghibli-API
https://github.com/janaipakos/ghibliapi

'''

import shutil
import re
import requests


class Ghibli():
    ''' ghibli api '''
    def __init__(self):
        self.base_url = 'https://ghibliapi.herokuapp.com'

def fetch_random_dog():
    ''' test '''
    url = 'https://dog.ceo/api/breeds/image/random'
    r = requests.get(url, timeout=5.0)
    if r.status_code == 200:
        j = r.json()
        # {'message': 'https://images.dog.ceo/breeds/entlebucher/n02108000_1122.jpg',
        # 'status': 'success'}
        print(j)
        if j['status'] == 'success':
            img_url = j['message']
            img_fn = grep_image_name(img_url)
            dog_breed = grep_breed_name(img_url)
            print('breed:', dog_breed)
            save_image_from_url(img_url, img_fn)

def grep_image_name(url):
    ''' image name '''
    r = None
    m = re.search(r'([^\/]+)$', url)
    if m:
        r = m.group()
    return r

def grep_breed_name(url):
    ''' breed name '''
    r = None
    m = re.search(r'breeds\/([^\/]+)/', url)
    if m:
        r = m.group(1)
        #print(r)
    return r

# https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
def save_image_from_url(url, fn):
    ''' save image from specified url '''
    r = requests.get(url, stream=True, timeout=5.0)
    if r.status_code == 200:
        with open(fn, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        print('output to:', fn)

def test():
    ''' test '''
    grep_breed_name('https://images.dog.ceo/breeds/dingo/n02115641_5033.jpg')
    grep_breed_name('https://images.dog.ceo/breeds/retriever-chesapeake/n02099849_2020.jpg')
    grep_breed_name('https://images.dog.ceo/breeds/entlebucher/n02108000_1122.jpg')


def main():
    ''' main '''
    fetch_random_dog()
    #test()


if __name__ == '__main__':
    main()
