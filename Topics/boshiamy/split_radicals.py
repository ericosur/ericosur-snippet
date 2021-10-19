#!/usr/bin/env python3
# coding: utf-8

'''
read boshiamy_radicals.txt and output into lui.json

'''


import json

class Solution:
    ''' solution '''
    def __init__(self):
        self.data_file = 'boshiamy_radicals.txt'
        self.fileobj = None
        self.rad_dict = {}

    def run(self):
        ''' run '''
        cnt = 0
        with open(self.data_file, 'rt', encoding='utf8') as f:
            for ll in f.readlines():
                r, c = Solution.split_line(ll)
                try:
                    cp = ord(c)
                    if c in self.rad_dict:
                        self.rad_dict[cp].append(r)
                    else:
                        r_list = []
                        r_list.append(r)
                        self.rad_dict[cp] = r_list
                    cnt += 1
                except TypeError:
                    pass
        print('process cnt:', cnt)
        self.output_to_json('liu.json')

    def output_to_json(self, fn: str):
        ''' output to json '''
        print(f'ouput to {fn}...')
        with open(fn, 'wt', encoding='utf8') as of:
            of.write(json.dumps(self.rad_dict, indent=2, sort_keys=True))
        print(f'size: {len(self.rad_dict)}')


    @staticmethod
    def split_line(s: str) -> (str, str):
        ''' split line into two part '''
        #print(s)
        arr = s.split(' ')
        if len(arr) != 2:
            return (None, None)
        #print(arr)
        return (arr[0].strip(), arr[1].strip())


def main():
    ''' main '''
    s = Solution()
    s.run()


if __name__ == '__main__':
    main()
