#!/usr/bin/env python3
#coding: utf-8

'''
try tomllib or tomli
'''

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

class Solution():
    ''' class solution '''
    def __init__(self):
        self.value = 0

    @staticmethod
    def test():
        ''' test '''
        s = tomllib.loads("['This parses fine with Python 3.6+']")
        print(f'test: {s=}')

    def action(self):
        ''' action '''
        print('action!')
        Solution.test()

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
