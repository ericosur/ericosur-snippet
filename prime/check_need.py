#!/usr/bin/env python3
# coding: utf-8

''' check need '''

from store_prime import StorePrime

def main():
    ''' main '''
    fn = 'need_check.txt'
    cnt = 0

    with StorePrime() as sp:
        with open(fn, 'rt', encoding='utf8') as f:
            while True:
                cnt += 1
                ln = f.readline().strip()
                if ln == '':
                    break
                if sp.find(int(ln)) == -1:
                    print('not prime: ', ln)
                if cnt % 10000 == 0:
                    print(cnt)
    print(cnt)

if __name__ == '__main__':
    main()
