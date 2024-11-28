#!/usr/bin/env python3
# coding: utf-8
#

'''
demo how to use os.path.join()

It will take care the dir seperator from different OS.
'''

import os.path


def main():
    ''' main '''
    print('demo os.path.join()')
    folder_output_name = 'output'
    for frame_number in range(6):
        fn = f'frame_{frame_number:05d}.png'
        f = os.path.join(folder_output_name, fn)
        print(f)

if __name__ == '__main__':
    main()
