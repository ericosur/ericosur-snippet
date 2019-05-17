#!/usr/bin/env python3
# coding: utf-8

'''
use yagmail to send mail via gmail
'''

import os
import time
import yagmail
from myutil import read_jsonfile, isfile

def append_path(fn):
    home = os.environ.get('HOME')
    path = home + '/Private/' + fn
    if not isfile(path):
        print('[FAIL] key file not exist: {}'.format(path))
        return None
    return path

def main():
    data = read_jsonfile(append_path('gmail-app-local.json'))
    if data is None:
        print('cannot fetch key, exit...')
        return
    appkey = data.get('appkey')

    data = read_jsonfile(append_path('pushover-net.json'))
    if data is None:
        print('cannot fetch setting, exit...')
        return
    email = data.get('email')

    print('send content via email gateway by pushover')

    imgurl = 'https://i.imgur.com/Y7VTPOis.jpg'
    yagmail.register('ericosur@gmail.com', appkey)
    yag = yagmail.SMTP('ericosur@gmail.com')
    to = email
    subject = 'yagmail + pushover @{}'.format(int(time.time()))
    body = 'just have fun with yagmail, visit url: {}'.format(imgurl)
    img = '/home/rasmus/Pictures/test/ff.jpg'
    yag.send(to=to, subject=subject, contents=[body, img])


if __name__ == '__main__':
    main()
