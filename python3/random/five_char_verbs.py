#!/usr/bin/env python3
# utf-8

'''
read data from verbs.csv as text file
and search for lines that match a given pattern
'''

import os
import sys
import re

class Solution():
    ''' my grep solution '''
    VERB_LIST = 'verbs.csv'

    def __init__(self):
        ''' constructor '''
        self.home = os.environ.get('HOME')
        self.verb_filepath = self.get_data_filepath(self.VERB_LIST)
        self.verbs = []

    def get_data_filepath(self, filename: str) -> str:
        ''' get data file path '''
        # /home/user/src/github/english-irregular-verbs/data
        target = os.path.join(self.home, 'src', 'github', 'english-irregular-verbs', 'data', filename)
        if os.path.isfile(target):
            return target
        return ""

    def parse_file(self):
        ''' perform grep action '''
        pattern = r"^([a-z]{5}),([^,]+),([^,]+)$"
        try:
            with open(self.verb_filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    m = re.match(pattern, line)
                    if m:
                        self.verbs.append(m[1])
        except FileNotFoundError:
            print(f"Error: '{self.VERB_LIST}' file not found.", file=sys.stderr)

    def action(self):
        ''' action '''
        self.parse_file()
        print(f'Found {len(self.verbs)} verbs:')
        for verb in self.verbs:
            print(verb)

def main():
    ''' main '''
    obj = Solution()
    obj.action()

if __name__ == '__main__':
    main()
