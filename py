#!/usr/bin/python3
# coding: utf-8

'''
brief description for this script
'''

import argparse

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='brief description for this script')
    parser.add_argument("strings", metavar='str', type=str, nargs='+',
        help="show these strings")
    parser.add_argument('-o', '--output', help='Output file name', default='stdout')
    parser.add_argument("-v", "--verbose", action='store_true', default=False,
        help='verbose mode')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)

    #parser.parse_args(['-i input.txt -o out.txt str1 str2'])

    args = parser.parse_args()

    print(args.strings)
    if args.output:
        print('output:', args.output)
    if args.input:
        print('input:', args.input)


if __name__ == '__main__':
    main()
