#!/usr/bin/python3
# coding: utf-8

'''
lookup bpmf from bpmf.json
'''

import sys
from myutil import read_jsonfile

class Solution():
    ''' solution '''
    def __init__(self):
        self.keys = list('/.,;-1234567890abcdefghijklmnopqrstuvwxyz')
        self.bpmf = list('ㄥㄡㄝㄤㄦㄅㄉˇˋㄓˊ˙ㄚㄞㄢㄇㄖㄏㄎㄍㄑㄕㄘㄛㄨㄜㄠㄩㄙㄟㄣㄆㄐㄋㄔㄧㄒㄊㄌㄗㄈ')
        assert len(self.keys) == len(self.bpmf)
        self.bpmf_dict = dict(zip(self.keys, self.bpmf))
        self.data = None
        self.load_json()

    def load_json(self):
        ''' load json '''
        self.data = read_jsonfile('bpmf.json')

    def translate_key(self, key_list, space=True):
        ''' translate key into han bpmf '''
        result = ''
        for k in key_list:
            #print('k', k)
            for kl in list(k):
                result = result + self.bpmf_dict[kl]
            if space:
                result = result + '  '
        return result

    def lookup(self, s):
        ''' lookup han character for bpmf '''
        if s in self.data:
            v = self.data[s]
            #print('{}: {}'.format(s, v))
            print(s, end='  ')
            res = ''
            for k in v:
                res = self.translate_key(k, space=False)
                print(res, end=',')
            print()

    def dump_all(self):
        '''
        dump all data as same format bopomofo-u8.txt, like:
        一 3 ㄧ  ㄧˊ  ㄧˋ
        '''
        fn = 'dump-bpmf.txt'
        with open(fn, 'wt') as f:
            for k in sorted(self.data):
                v = self.data[k]
                r = self.translate_key(v)
                print('{} {} {}'.format(k, len(v), r), file=f)
        print('output to {}'.format(fn))

def test():
    ''' test '''
    sol = Solution()
    sol.dump_all()

def main(argv):
    ''' main '''
    query = list()
    if argv == []:
        query = list('零一二三四五六七八九○')
    else:
        for a in argv:
            if len(a) > 1:
                query.extend(list(a))
            else:
                query.append(a)
    sol = Solution()
    for k in query:
        sol.lookup(k)


if __name__ == '__main__':
    # test()
    if len(sys.argv) == 1:
        main([])
    elif sys.argv[1] == 'dump':
        test()
    else:
        main(sys.argv[1:])
