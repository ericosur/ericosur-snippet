#!/usr/bin/env python
#

import myutil
import getimg

import os
import sys
from PIL import Image

def try_to_download(json_data, title):
    for img in json_data:
        if img['title'] == title:
            url = img['url']
            file = img['file']
            print('download url({0}) as file({1})'.format(url, file))
            getimg.download_url_to_file(url, file)
            return file


def main():
    app_name = 'imgur.py'
    data = myutil.read_setting('setting.json')
    json_data = data[app_name]['picture']
    title = 'deer'
    file = 'deer.png'

    if not myutil.isfile(file):
        file = try_to_download(json_data, title)

    im = Image.open(file)
    im.show()


if __name__ == '__main__':
    main()
