#!/usr/bin/env python3
# coding: utf-8

'''
use yagmail to send mail via gmail

reference:
- https://github.com/kootenpv/yagmail
- http://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html
'''

import os
import time
import yagmail
from myutil import read_jsonfile, isfile

class FoolMail(object):
    def __init__(self):
        self.conf = 'ggmail.json'
        self.auth = None
        self.appkey = None
        self.oathfile = None
        self.from_ = None
        self.to = None
        self.subject = None
        self.bodyfile = None
        self.body = None
        self.load_config()

    def load_config(self):
        d = read_jsonfile(self.conf)
        if d is None:
            print('[FAIL] failed to load config')
        else:
            self.auth = d.get('auth')
            if self.auth == 'appkeyfile':
                self.get_appkey(self.append_path(d.get('appkeyfile')))
            else:
                self.oathfile = self.append_path(d.get('oathfile'))
            self.from_ = d.get('from')
            self.to = d.get('to')
            self.subject = d.get('subject')
            self.bodyfile = d.get('bodyfile')
            #self.load_body()

    def dump(self):
        if self.auth == 'appkeyfile':
            print('appkey:', self.appkey)
        else:
            print('oath:', self.oathfile)
        print('from:', self.from_)
        print('to:', self.to)
        print('subject:', self.subject)
        print('bodyfile: ', self.bodyfile)

    @staticmethod
    def append_path(fn):
        home = os.environ.get('HOME')
        path = home + '/Private/' + fn
        if not isfile(path):
            print('[FAIL] key file not exist: {}'.format(path))
            return None
        return path

    def get_appkey(self, fn):
        d = read_jsonfile(fn)
        self.appkey = d.get('appkey')

    def load_body(self):
        with open(self.bodyfile, "rt") as bodyf:
            self.body = bodyf.read()
        print('finish loading body')

    def send(self):
        print('send file via gmail...')
        if self.auth == 'appkeyfile':
            yag = yagmail.SMTP(self.from_, self.appkey)
        else:
            yag = yagmail.SMTP(self.from_, oauth2_file=self.oathfile)
        subject = '{} @{}'.format(self.subject, int(time.time()))
        ret = yag.send(to=self.to, subject=subject,
            contents=['please refer to my attchment', self.bodyfile])
        print(ret)

def main():
    foo = FoolMail()
    foo.dump()
    foo.send()

if __name__ == '__main__':
    main()
