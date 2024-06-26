#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''demo fetch image from imgur'''

from __future__ import print_function
import os
from PIL import Image
from imgconfig import read_image_config
from loadimgur import fetch_image

def try_to_download(json_data, title):
    '''load setting variables from jsonfile and download'''
    for img in json_data:
        if img['title'] == title:
            url = img['url']
            fn = img['fn']
            print(f'download url({url}) as fn({fn})')
            fetch_image(url, fn)
            return fn
    return None


def main():
    '''main function'''
    app_name = 'imgur.py'
    data = read_image_config()
    json_data = data[app_name]['picture']
    title = 'deer'
    fn = 'deer.png'

    if os.path.exists(fn):
        print(f'file {fn} already exists, will not download')
    else:
        fn = try_to_download(json_data, title)

    im = Image.open(fn)
    im.show()


if __name__ == '__main__':
    main()
