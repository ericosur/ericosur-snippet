#!/usr/bin/env python3
# coding: utf-8

'''
The output of this script is almost same as hira.py.
Input from text (one character each line).

五十音類
あ い う え お
か き く け こ
さ し す せ そ
た ち つ て と
な に ぬ ね の
は ひ ふ へ ほ
ま み む め も
や ゆ よ
ら り る れ ろ
わ ゐ ゑ
を ん

'''



class Solution():
    ''' here I put three question mark in ya/wa line '''
    afn = 'a.txt'
    Afn = 'A.txt'
    magics = [5,5,5,5,5,5,5,5,5,5,1,99]

    def __init__(self):
        self.a = self.__load(Solution.afn)
        self.A = self.__load(Solution.Afn)

    def __load(self, fn):
        ''' load txt '''
        the_list = []
        with open(fn, 'rt', encoding='UTF-8') as fobj:
            for ln in fobj.readlines():
                t = ln.strip()
                the_list.append(t)
        return the_list

    @staticmethod
    def println(alist):
        ''' println '''
        msg = ''
        for c in alist:
            msg += f'{c:2s}'
        print(msg)

    def output(self, the_list):
        t = the_list.copy()
        for m in self.magics:
            p = []
            for c in range(m):
                if t:
                    p.append(t.pop(0))
            self.println(p)

    def output_py(self, the_list):
        t = the_list.copy()
        print('the_a = [')
        for m in self.magics:
            p = []
            for c in range(m):
                if t:
                    p.append(t.pop(0))
            if p:
                print(p, end=',\n')
        print(']')

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.output(obj.a)
        obj.output(obj.A)

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
