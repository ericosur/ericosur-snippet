#!/usr/bin/python3
# coding: utf-8

''' split a file with many lines into several small ones
'''

import os

def main():
    ''' main '''
    TOTAL_LINE = 113233
    left_line = TOTAL_LINE
    cut_size = 10000
    start = 1
    end = start + cut_size - 1
    fno = 1
    fn = 'cc.txt'
    o_files = list()
    while left_line > 0 and start < TOTAL_LINE:
        end = start + cut_size - 1
        if end >= TOTAL_LINE:
            end = TOTAL_LINE

        ofn = 'of{:03d}.txt'.format(fno)
        o_files.append(ofn)
        cmd = 'sed -n {},{}p {} > {}'.format(start, end, fn, ofn)
        print(cmd)
        os.system(cmd)
        start += cut_size
        fno += 1
        if left_line >= cut_size:
            left_line -= cut_size
    print(o_files)
    cmd = 'cat ' + ' '.join(o_files) + ' > total.txt'
    print(cmd)

if __name__ == '__main__':
    main()
