#!/usr/bin/env python3
# coding: utf-8

''' check need '''

def main():
    ''' main '''
    fn = 'need_check.txt'
    cnt = 0
    from store_prime import StorePrime
    with StorePrime() as sp:
        with open(fn, 'rt') as f:
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
