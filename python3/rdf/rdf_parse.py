#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
parse digest.rdf to get hash values

ImageMagick gave digest.rdf for digest checking, use this script to check
similar to "sha256sum -c SHA256SUM"

'''

import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('use pip install beautifulsoup4')
    print('use pip install lxml')
    sys.exit(1)

sys.path.insert(0, "..")
from myutil import isfile, read_textfile, sha256sum, MyDebug


class Solution(MyDebug):
    ''' solution to read en.xml and output as csv-like data '''

    def __init__(self):
        super().__init__(False)
        self.fn = 'digest.rdf'
        self.content = None
        self.digests = []

    def make_soup(self) -> None:
        ''' parse xml from content, store into self.emoji '''
        soup = BeautifulSoup(self.content, features='xml')
        t = soup.find('rdf:RDF')
        anns = t.find_all('digest:Content')
        for i in anns:
            pair = {}
            pair["file"] = i.get('rdf:about')
            ds = i.find("digest:sha256")
            pair["hash"] = ds.getText()
            self.digests.append(pair)
        if self.debug:
            print("len:", len(self.digests))

    @staticmethod
    def _sha256sum(f, d):
        ''' sha256sum and checksum '''
        s256 = sha256sum(f)
        return s256 == d

    def dump(self):
        ''' dump self.digests '''
        for p in self.digests:
            the_file = p['file']
            if isfile(the_file):
                ret = Solution._sha256sum(the_file, p["hash"])
                print(f'{the_file}\t{p["hash"]}', end='  ')
                if ret:
                    print("OK")
                else:
                    print("NG")
            else:
                if self.debug:
                    print(f'not found: {the_file}')


    def action(self) -> None:
        ''' action '''
        self.debug = False
        print(f'parsing {self.fn}...')
        self.content = read_textfile(self.fn)
        #print('[DEBUG]', self.content)

        # parsing xml and store into list()
        self.make_soup()
        if self.digests:
            self.dump()

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
