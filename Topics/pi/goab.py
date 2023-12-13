#!/usr/bin/env python3
# coding: utf-8

'''
get text from known position and length

use ```grep -ob 123456 pi-billion.txt```
to get position of matched string token

'''

import os


def get_pipath():
    ''' return pi-billion.txt full path '''
    home = os.environ["HOME"]
    fn = home + '/Dropbox/src/pi_digits/pi-billion.txt'
    return fn

def main():
    ''' main '''
    fn = get_pipath()
    target = '19890604'
    # use ```grep -ob 19890604 pi-billion``` will get these numbers
    pos_list = [
        350378481, 427142832, 585858476, 705391152, 771039633,
        808353115, 836748874, 846783124, 921591435
    ]
    try:
        with open(fn, 'rt', encoding='UTF-8') as pi:
            for pp in pos_list:
                pi.seek(pp, 0)
                buf = pi.read(len(target))
                print(f'{buf} @{pp}')
                if buf != target:
                    print('[ERROR] not matched!')
    except FileNotFoundError as e:
        print('except:', e)

if __name__ == '__main__':
    main()
