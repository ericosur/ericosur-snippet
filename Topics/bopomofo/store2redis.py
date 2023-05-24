#!/usr/bin/python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
__phone.json__ is a lookup table from phonetic radicals to han characters.
If local redis server (w/ rejson) stores such table, it will query the server.
If not, it store this table into redis, and then query.

Need start the service of redis/rejson first.
'''

from typing import List
import os
import sys

from rejson import  Client, Path
import redis

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_jsonfile

# pylint: disable=invalid-name
class StoreAndQuery():
    ''' read a json and store it into redis and then query '''
    def __init__(self):
        self.tests = ['ru.4', '5k4', 'u;4', 'ji3', '5', '2l4', 'xk7']   # no need bracket here
        # the redis server
        self.rj = Client(host='localhost', port=6379, decode_responses=True)
        # phonetic table, radical to han characters
        self.fn = 'phone.json'
        self.objname = 'obj'
        self.data = None
        self.check_and_store()

    def check_and_store(self):
        ''' if no data here, read json and store it '''
        #print('[INFO] check_and_store')
        try:
            res = self.test_one_query('284', show=False)
            if res is None:
                print('[INFO] no data stored? read and store it')
                self.data = read_jsonfile(self.fn)
                self.rj.jsonset(self.objname, Path.rootPath(), self.data)
                print(f'[INFO] read {self.fn} and store as {self.objname}')
            print('[TEST] res:', res)
        except redis.exceptions.ConnectionError as e:
            print('[ERROR] cannot connect to redis server:\n', e)
            print('\nNeed start the service of redis/rejson first.')
            sys.exit(1)
        except redis.exceptions.ResponseError as e:
            print('[ERROR]', e)
            print('SHOULD USE rejson docker, not redis docker')
            sys.exit(1)

    @staticmethod
    def transcode(ans: List) -> List:
        ''' transcode, do not know why rejson split a han char (3-byte utf-8)
            into 3 unicode chars (no really utf8 encode/decode, just splited)
            so here I could combine them back

            For example, "中" in utf8 is "e4 b8 ad", query out of redis, I got
            "\u00e4 \u00b8 \u00ad".
        '''
        u8ans = []
        for m in ans:
            s = ''
            if isinstance(m, bytes):
                ansi = m.encode('ISO8859-1')    # m is str, ansi is bytes
                s = ansi.decode('UTF-8')    # s is str in correct unicode char
            elif isinstance(m, str):
                s = m
            u8ans.append(s)
        return u8ans

    @staticmethod
    def show_result(res: List) -> None:
        ''' show only 10 results '''
        break_flag = False
        for i, s in enumerate(res):
            if i > 9:
                print('...', end=' ')
                break_flag = True
                break
            print(s, end=' ')
        if break_flag:
            print(res[-1])
        else:
            print()

    def test_one_query(self, key, show=True) -> List:
        ''' test one query
        127.0.0.1:6379> json.get  obj  noescape "zul4"
        "[\"\xe8\xa6\x85\",\"\xf0\xa1\xa0\x8d\"]"

        list all keys in json obj:
          > json.objkeys obj
        '''
        qkey = '["' + key + '"]'    # like ["su;6"]
        try:
            r = self.rj.jsonget(self.objname, Path(qkey))
            if r:
                if show:
                    print(key)
                res = self.transcode(r)
                if show:
                    self.show_result(res)
                return res
        except redis.exceptions.ResponseError as e:
            print(e)

        return None

    def test_query(self) -> None:
        ''' test redis json '''
        for v in self.tests:
            self.test_one_query(v)

    def test_json(self) -> None:
        ''' test json obj '''
        for v in self.tests:
            try:
                print(self.data[v])
            except KeyError as e:
                print('KeyError: ', e)

    @classmethod
    def action(cls) -> None:
        ''' action '''
        obj = cls()
        obj.test_query()

def main():
    ''' main '''
    StoreAndQuery.run()

if __name__ == '__main__':
    main()
