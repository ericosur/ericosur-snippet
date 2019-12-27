#!/usr/bin/env python3
# coding: utf-8

'''
pip install base58
'''

import sys
try:
    import base58
except ImportError:
    print('need install module **base58**')
    sys.exit(1)

def main(argv):
    ''' main '''
    print('base58.alphabet:', base58.alphabet)

    if argv == []:
        s = 'the quick smart fox jumps over the lazy dog'
        argv.append(s)

    for ii in argv:
        len1 = len(ii)
        b58 = base58.b58encode(ii)
        b58s = b58.decode('utf-8')
        len2 = len(b58s)
        print('   original len:', len1)
        print('    encoded len:', len2)
        print('     input:', ii)
        print('   encoded:', b58)
        print('   ratio:', len2 / len1)

        print('-' * 40)

        b58c = base58.b58encode_check(b58)
        len3 = len(b58c)
        print('encoded_check:', b58c)
        print('check len:', len3)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
