#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''demo fetch image from imgur'''

from __future__ import print_function
from PIL import Image
import myutil
import getimg

def try_to_download(json_data, title):
    '''load setting variables from jsonfile and download'''
    for img in json_data:
        if img['title'] == title:
            url = img['url']
            fn = img['fn']
            print('download url({0}) as fn({1})'.format(url, fn))
            getimg.download_url_to_file(url, fn)
            return fn
    return None



def main():
    '''main function'''
    app_name = 'imgur.py'
    data = myutil.read_setting('setting.json')
    json_data = data[app_name]['picture']
    title = 'deer'
    fn = 'deer.png'

    if myutil.isfile(fn):
        print('file {} already exists, will not download'.format(fn))
    else:
        fn = try_to_download(json_data, title)

    im = Image.open(fn)
    im.show()


if __name__ == '__main__':
    main()
