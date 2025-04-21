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
    home = os.environ.get("HOME")
    if home is None:
        raise ValueError('HOME not found')
    # dropbox or Dropbox
    dirs = ['Dropbox', 'dropbox']
    top = None
    for d in dirs:
        t = os.path.join(home, d)
        if os.path.exists(t):
            top = t
            break
    fn = os.path.join(top, 'src', 'pi_digits', 'pi-billion.txt')
    if not os.path.exists(fn):
        raise FileNotFoundError(f'pi-billion.txt not found: {fn}')
    return fn

def main():
    ''' main '''
    target = '19890604'
    # use ```grep -ob 19890604 pi-billion``` will get these numbers
    pos_list = [
        350378481, 427142832, 585858476, 705391152, 771039633,
        808353115, 836748874, 846783124, 921591435
    ]
    try:
        fn = get_pipath()
        with open(fn, 'rt', encoding='UTF-8') as pi:
            for pp in pos_list:
                pi.seek(pp, 0)
                buf = pi.read(len(target))
                print(f'{buf} @{pp}')
                if buf != target:
                    print('[ERROR] not matched!')
    except ValueError as e:
        print('except:', e)
    except FileNotFoundError as e:
        print('except:', e)

if __name__ == '__main__':
    main()
