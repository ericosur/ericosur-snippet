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


import os
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('use pip install beautifulsoup4')
    print('use pip install lxml')
    sys.exit(1)

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_textfile, sha256sum


class Solution():
    ''' solution to read en.xml and output as csv-like data '''

    def __init__(self):
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
            fn = i.get('rdf:about')
            pair["file"] = fn
            ds = i.find("digest:sha256")
            pair["hash"] = ds.getText()
            self.digests.append(pair)

    @staticmethod
    def _sha256sum(f, d):
        ''' sha256sum and checksum '''
        s256 = sha256sum(f)
        return s256 == d

    def dump(self):
        ''' dump self.digests '''
        for p in self.digests:
            if os.path.exists(p["file"]):
                ret = Solution._sha256sum(p["file"], p["hash"])
                print(f'{p["file"]}\t{p["hash"]}', end='  ')
                if ret:
                    print("OK")
                else:
                    print("NG")


    def action(self) -> None:
        ''' action '''
        fn = self.fn
        print(f'parsing {fn}...')
        self.content = read_textfile(fn)
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
