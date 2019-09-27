#!/usr/bin/env python3
# coding: utf-8

'''
input text from CLI and generate qrcode image
'''

import sys
#from PIL import Image
try:
    import qrcode
except ImportError:
    print('need install module **qrcode**')
    sys.exit()

def main(argv):
    ''' main '''
    if argv == []:
        argv.append('https://www.google.com/')

    for a in argv:
        print(a)
        im = qrcode.make(a)
        im.show()

if __name__ == '__main__':
    main(sys.argv[1:])
