#!/usr/bin/env python3
# coding: utf-8

'''
android dp to px and verse
'''

import argparse
import sys

class Converter():

    DENSITY_DEFAULT = 160  # android default reference density

    def __init__(self):
        self.density = 0   # device LCD density

    def set_density(self, den):
        ''' set density '''
        self.density = den
        print(f'density: {self.density}')

    def dp2px(self, dp):
        ''' dp2px '''
        if self.density == 0:
            print('[ERROR] need set density first')
            return None
        px = dp * (self.density / self.DENSITY_DEFAULT)
        return px

    def px2dp(self, px):
        ''' px to dp '''
        if self.density == 0:
            print('[ERROR] need set density first')
            return None
        dp = px / (self.density / self.DENSITY_DEFAULT)
        return dp

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='convert dp to dx, given dp and density')
    # parser.add_argument("strings", metavar='str', type=str, nargs='+',
    #     help="show these strings")
    parser.add_argument("dp", type=int, nargs='+', help='dp to calculate...')
    parser.add_argument("-d", "--density", type=int, default=400, nargs='?', help='set density, default=320')
    parser.add_argument("-v", "--verbose", action='store_true', help='verbose')
    args = parser.parse_args()

    # print(args.strings)
    if args.verbose:
        print('verbose on')
    if not args.dp:
        parser.print_help()
        sys.exit(0)

    foo = Converter()
    foo.set_density(args.density)
    for d in args.dp:
        print(f"dp = {d} => px = {foo.dp2px(d)}")
        print(f"dx = {d} => px = {foo.px2dp(d)}")

if __name__ == '__main__':
    main()
