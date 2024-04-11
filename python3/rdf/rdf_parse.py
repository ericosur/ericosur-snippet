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

import argparse
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('use pip install beautifulsoup4')
    print('use pip install lxml')
    sys.exit(1)

sys.path.insert(0, "..")
from myutil import isfile, read_textfile, sha256sum, MyDebug, MyVerbose

class Solution(MyDebug, MyVerbose):
    ''' solution to read en.xml and output as csv-like data '''

    def __init__(self, debug=False, verbose=False):
        super().__init__(debug)
        MyVerbose.__init__(self, verbose)
        self.rdfs = []
        self.content = None
        self.digests = []
        self.check = False

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
        self.logd("len:", len(self.digests))

    def set_rdf(self, rdf):
        ''' set rdf '''
        self.rdfs = rdf

    def set_check(self, yesNo):
        ''' check or not '''
        self.check = yesNo

    @staticmethod
    def _sha256sum(f, d):
        ''' sha256sum and checksum '''
        s256 = sha256sum(f)
        return s256 == d

    def dump_digest(self):
        ''' dump digests '''
        for i in self.digests:
            h = i.get('hash')
            f = i.get('file')
            print(f'{h}  {f}')

    def check_digest(self):
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
                self.logv(f'file not found: {the_file}')

    def action(self) -> None:
        ''' action '''
        for f in self.rdfs:
            print(f'parsing {f}...', file=sys.stderr)
            self.content = read_textfile(f)
            self.logd('content: ', self.content)

            # parsing xml and store into list()
            self.make_soup()
            if self.check:
                self.check_digest()
            else:
                self.dump_digest()

    @classmethod
    def run(cls, files, check, verbose):
        ''' run '''
        obj = cls(verbose=verbose)
        obj.set_rdf(files)
        obj.set_check(check)
        obj.action()


def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='parse rdf file and perform checksum',
                    epilog='try ```rdf_parse.py digest.rdf -c```')
    # nargs like regexp, '*' means 0+, '+' means 1+
    parser.add_argument("files", metavar='file', type=str, nargs='+',
        help="show these strings")
    parser.add_argument("-c", "--check", action='store_true', default=False,
        help='perform checksum check')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')

    args = parser.parse_args()
    Solution.run(args.files, check=args.check, verbose=args.verbose)

if __name__ == '__main__':
    main()
