#!/usr/bin/env python3
#coding: utf-8

'''
try tomllib or tomli
'''

try:
    import tomllib
except ModuleNotFoundError:
    print('[WARN] no tomllib, try tomli')
    import tomli as tomllib

class Solution():
    ''' class solution '''
    toml = '''
# a long string in format TOML
[main]
filename = "trytoml.py"
md5sum = "e5b1f6b7a8aaa5ec34b6b6573fd66f38"
    '''
    def __init__(self):
        self.value = 0

    @staticmethod
    def test():
        ''' test '''
        s = tomllib.loads(Solution.toml)
        print(s)

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
