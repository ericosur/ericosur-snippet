#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position
# pylint: disable=unreachable

'''
just for reference, it is not useful for my own working environment

use yagmail to send mail via gmail

reference:
- https://github.com/kootenpv/yagmail
- http://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html
'''


import os
import sys
import time

# ruff: noqa
sys.path.insert(0, '../')
sys.path.insert(0, '../../')
sys.path.insert(0, 'python3/')
from myutil import read_jsonfile

print('Just for reference, DO NOT run this script...')
sys.exit(1)

try:
    import yagmail
except ImportError:
    print('cannot import module: yagmail')
    sys.exit(1)


class FoolMail():
    ''' class to send mail via gmail '''
    def __init__(self):
        self.auth = None
        self.appkey = None
        self.oathfile = None
        self.from_ = None
        self.to_ = None
        self.subject = None
        self.bodyfile = None
        self.load_config()

    def load_config(self):
        ''' load api key from config '''
        app_conf = 'ggmail.json'
        d = read_jsonfile(app_conf)
        if d is None:
            print('[FAIL] failed to load config')
        else:
            self.auth = d.get('auth')
            if self.auth == 'appkeyfile':
                self.get_appkey(self.append_path(d.get('appkeyfile')))
            else:
                self.oathfile = self.append_path(d.get('oathfile'))
            self.from_ = d.get('from')
            self.to_ = d.get('to')
            self.subject = d.get('subject')
            self.bodyfile = d.get('bodyfile')
            #self.load_body()

    def dump(self):
        ''' dump variables '''
        if self.auth == 'appkeyfile':
            print('appkey:', self.appkey)
        else:
            print('oath:', self.oathfile)
        print('from:', self.from_)
        print('to:', self.to_)
        print('subject:', self.subject)
        print('bodyfile: ', self.bodyfile)

    @staticmethod
    def append_path(fn):
        ''' append $HOME '''
        home = os.environ.get('HOME')
        path = os.path.join(home, 'Private', fn)
        if not os.path.exists(path):
            print(f'[FAIL] key file not exist: {path}')
            return None
        return path

    def get_appkey(self, fn):
        ''' get appkey from fn '''
        d = read_jsonfile(fn)
        self.appkey = d.get('appkey')

    def load_body(self):
        ''' load content of body from file '''
        body = None
        with open(self.bodyfile, "rt", encoding='utf8') as bodyf:
            body = bodyf.read()
        print('finish loading body')
        return body

    def send(self):
        ''' send mail '''
        print('send file via gmail...')
        if self.auth == 'appkeyfile':
            yag = yagmail.SMTP(self.from_, self.appkey)
        else:
            yag = yagmail.SMTP(self.from_, oauth2_file=self.oathfile)
        subject = f'{self.subject} @{int(time.time())}'
        ret = yag.send(to=self.to_, subject=subject,
                       contents=['please refer to my attchment', self.bodyfile])
        print(ret)

def main():
    ''' main '''
    foolmail = FoolMail()
    foolmail.dump()
    foolmail.send()

if __name__ == '__main__':
    main()
