#!/usr/bin/python3.6
# coding: utf-8

'''
brief description for this script
'''

import argparse
import sys

class Converter():
    def __init__(self):
        self.density = 0

    def set_density(self, den):
        ''' set density '''
        self.density = den

    def dp2px(self, dp):
        ''' dp2px '''
        if self.density == 0:
            print('[ERROR] need set density first')
            return None
        px = dp * (self.density / 160)
        return px

    def px2dp(self, px):
        ''' px to dp '''
        if self.density == 0:
            print('[ERROR] need set density first')
            return None
        dp = px / (self.density / 160)
        return dp

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='convert dp to dx, given dp and density')
    # parser.add_argument("strings", metavar='str', type=str, nargs='+',
    #     help="show these strings")
    parser.add_argument("dp", type=int, nargs='+', help='dp to calculate...')
    parser.add_argument("-d", "--density", type=int, default=320, nargs='?', help='set density, default=320')
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
    for dp in args.dp:
        print(f"dp = {dp} => px = {foo.dp2px(dp)}")

if __name__ == '__main__':
    main()
