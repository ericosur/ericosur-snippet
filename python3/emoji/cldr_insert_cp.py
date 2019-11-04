#!/usr/bin/env python3
# coding: utf-8
#

'''
read pre-processed csv table (cldr.csv)
and add a clumne for unicode codepoint (out.csv)
'''

import csv

# pylint: disable=invalid-name

class Solution():
    ''' solution for csv file '''
    def __init__(self, fn, ofn):
        self.fn = fn
        self.ofn = ofn

    def run(self):
        ''' run '''
        cnt = 0
        with open(self.fn) as csvfile, open(self.ofn, 'w') as outfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            csvwriter = csv.writer(outfile, delimiter=',', quotechar='"',
                                   quoting=csv.QUOTE_ALL)
            for row in csvreader:
                cnt += 1
                newrow = []
                cp = Solution.to_codepoint(row[0])
                newrow.append(row[0])
                newrow.append(cp)
                newrow.extend(row[1:])
                csvwriter.writerow(newrow)
        print('{} rows processed'.format(cnt))
        print('result goes to {}'.format(self.ofn))

    @staticmethod
    def to_codepoint(cc: str):
        '''
        cc [in] unicode char
        calling: to_from_u16(chr(0x0001f3c8))
        '''
        ue = cc.encode('unicode-escape').decode('utf-8')
        return ue

def main():
    ''' main '''
    sol = Solution('cldr.csv', 'emoji.csv')
    sol.run()

if __name__ == '__main__':
    main()
