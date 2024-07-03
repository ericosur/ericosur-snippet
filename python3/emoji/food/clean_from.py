#!/usr/bin/env python3
# coding: utf-8

'''
clean up from_emojipedia.txt
'''

import re

class Cleanup():
    ''' clean up '''
    fn = "from_emojipedia.txt"
    ofn = "cleaned.txt"

    def __init__(self):
        pass

    def action(self):
        ''' action '''
        with open(self.fn, 'rt', encoding='UTF-8') as fobj:
            with open(self.ofn, 'wt', encoding='UTF-8') as fout:
                for ln in fobj.readlines():
                    ln = ln.strip()
                    m = re.match('^[A-Za-z ]+$', ln)
                    if not m:
                        print(ln, file=fout)
        print(f'output to {self.ofn}')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Cleanup.run()

if __name__ == '__main__':
    main()
