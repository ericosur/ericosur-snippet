#!/usr/bin/python

''' binascii '''

import binascii

def main():
    ''' main '''
    hexstr = "e98099e698afe4b880e6aeb5e4b8ade69687e5ad97e794a87574662d38e7b7a8e7a2bc"
    print(binascii.unhexlify(hexstr))

    data = b"A quick fox jumps over a lazy dog"
    print(binascii.hexlify(data))

if __name__ == '__main__':
    main()
