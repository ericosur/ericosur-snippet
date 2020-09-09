#!/usr/bin/env python3
# coding: utf-8

'''
use yagmail to send mail via gmail

reference:
- https://github.com/kootenpv/yagmail
- http://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html
'''

from __future__ import print_function
import os
import sys
import time
try:
    import yagmail
except ImportError:
    print('ggmail: cannot import module: yagmail')
    sys.exit(1)

sys.path.insert(0, '/home/rasmus/src/ericosur-snippet/python3')
try:
    from myutil import read_jsonfile, isfile
except ImportError:
    print('ggmail: cannot import module: myutil')
    sys.exit(1)


class FoolMail():
    ''' class to send mail via gmail '''
    def __init__(self, filename=None):
        self.appkey = None
        self.oathfile = None
        self.from_ = None
        self.to_ = None
        self.subject = None
        self.bodyfile = None
        self.load_config(filename)

    def load_config(self, fn):
        ''' load api key from config '''
        home = os.environ.get('HOME')
        app_conf = home + '/set-send-attach.json'
        print('read settings from:', app_conf)
        d = read_jsonfile(app_conf)
        if d is None:
            print('[FAIL] failed to load config:', app_conf)
        else:
            auth_method = d.get('auth')
            if auth_method == 'appkeyfile':
                self.get_appkey(self.append_path(d.get('appkeyfile')))
            else:
                self.oathfile = self.append_path(d.get('oathfile'))
            self.from_ = d.get('from')
            self.to_ = d.get('to')
            self.subject = d.get('subject')
            if fn:
                print('body file is override by:', fn)
                self.bodyfile = fn
            else:
                self.bodyfile = d.get('bodyfile')
            #self.load_body()
        self._check()

    def _check(self):
        ''' check '''
        if self.bodyfile:
            if not isfile(self.bodyfile):
                print('[ERROR] bodyfile not found:', self.bodyfile)
                sys.exit(1)

    def dump(self):
        ''' dump variables '''
        print('[INFO] basic fields:')
        # if self.auth == 'appkeyfile':
        #     print('appkey:', self.appkey)
        # else:
        #     print('oath:', self.oathfile)
        print('      from:', self.from_)
        print('        to:', self.to_)
        #print('subject:', self.subject)
        print('  bodyfile:', self.bodyfile)

    @staticmethod
    def append_path(fn):
        ''' append $HOME '''
        home = os.environ.get('HOME')
        path = home + '/Private/' + fn
        if not isfile(path):
            print('[FAIL] key file not exist: {}'.format(path))
            return None
        return path

    def get_appkey(self, fn):
        ''' get appkey from fn '''
        d = read_jsonfile(fn)
        self.appkey = d.get('appkey')

    def load_body(self):
        ''' load content of body from file '''
        body = None
        with open(self.bodyfile, "rt") as bodyf:
            body = bodyf.read()
        print('finish loading body')
        return body

    def send(self):
        ''' send mail '''
        print('[INFO] Send file via gmail...')
        if self.appkey:
            yag = yagmail.SMTP(self.from_, self.appkey)
        else:
            yag = yagmail.SMTP(self.from_, oauth2_file=self.oathfile)
        subject = '{} @{}'.format(self.subject, int(time.time()))
        print('subject: {}'.format(subject))
        ret = yag.send(to=self.to_, subject=subject,
                       contents=['please refer to my attchment', self.bodyfile])
        print(ret)

def main(fn=None):
    ''' main '''
    fmail = None
    if fn and os.path.isfile(fn):
        fmail = FoolMail(filename=fn)
    else:
        fmail = FoolMail()
    if fmail:
        fmail.dump()
        fmail.send()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print('info: may specify file name to send')
        main()
