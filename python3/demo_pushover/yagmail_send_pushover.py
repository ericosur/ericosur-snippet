#!/usr/bin/env python3
# coding: utf-8

'''
use yagmail to send mail via gmail
'''

from __future__ import print_function
import os
import sys
import time
from myutil import read_jsonfile, isfile
try:
    import yagmail
except ImportError:
    print('cannot import yagmail, need install such module...')
    sys.exit(1)

def append_path(fn):
    ''' append path '''
    home = os.environ.get('HOME')
    path = home + '/Private/' + fn
    if not isfile(path):
        print(f'[FAIL] key file not exist: {path}')
        return None
    return path

def main():
    ''' main '''
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

    imgurl = 'https://i.imgur.com/ATTKrU7.jpg'
    #yagmail.register('ericosur@gmail.com', appkey)
    yag = yagmail.SMTP('ericosur@gmail.com', appkey)
    to = email
    subject = f'yagmail + pushover @{int(time.time())}'
    body = f'img @imgur: {imgurl}'
    img = '/home/rasmus/Pictures/picked/794724259_0f5edb1cd4.jpg'
    yag.send(to=to, subject=subject, contents=[body, img])


if __name__ == '__main__':
    main()
