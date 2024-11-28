#!/usr/bin/env python3
# coding: utf-8

'''
test mnemonic
'''

#import mnemonic
from hexdump import hexdump
from mnemonic import Mnemonic


def main():
    ''' main '''

    # langs = [
    #     "english",
    #     "chinese_simplified",
    #     "chinese_traditional",
    #     "french",
    #     "italian",
    #     "japanese",
    #     "korean",
    #     "spanish",
    #     "turkish",
    #     "czech",
    #     "portuguese"
    # ]

    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=256)
    seed = mnemo.to_seed(words, passphrase="")
    entropy = mnemo.to_entropy(words)

    print('words=')
    print(words)
    print('seed=')
    hexdump(seed)
    print('entropy=')
    hexdump(entropy)

if __name__ == '__main__':
    main()
