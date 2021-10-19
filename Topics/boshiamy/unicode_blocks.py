#!/usr/bin/env python3
# coding: utf-8

''' show input character in which unicode block '''


import re
import random
import pickle
import os

class UnicodeBlock():
    ''' solution '''
    def __init__(self):
        self.txtfile = 'Blocks.txt'
        self.pfile = 'blocks.p'
        self.blocks = []
        self.need_save = False
        self.data_loaded = False
        #print('__init__')
        self.load_pickle()

    def __enter__(self):
        #print('__enter__')
        self.load_pickle()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        #print('__exit__')
        #print('len(self.pvalues)', len(self.pvalues))
        #print('self.init_size', self.init_size)
        if not os.path.exists(self.pfile):
            if self.need_save:
                #print('__exit__ call save_pickle...')
                self.save_pickle()
            # else:
            #     print('__exit__ no need to save...')

    def get_blocks(self):
        ''' return blocks '''
        return self.blocks

    def get_cjkblocks(self):
        ''' get_cjkblocks '''
        _debug = False
        cjk_blocks = []
        for start, end, name in self.blocks:
            try:
                _ = name.index('CJK')
                if _debug:
                    print(f'{start:06x} ... {end:06x}  {name}')
                cjk_blocks.append([start, end, name])
            except ValueError:
                pass
        return cjk_blocks

    def block(self, ch):
        '''
        Return the Unicode block name for ch, or None if ch has no block.

        >>> block(u'a')
        'Basic Latin'
        >>> block(unichr(0x0b80))
        'Tamil'
        >>> block(unichr(0xe0080))
        '''
        assert isinstance(ch, str) and len(ch) == 1, repr(ch)
        cp = ord(ch)
        #print(cp)
        for start, end, name in self.blocks:
            if start <= cp <= end:
                return name
        return "Not Found"

    def load_pickle_impl(self):
        ''' load pickle implementation '''
        with open(self.pfile, "rb") as inf:
            self.blocks = pickle.load(inf)
            self.need_save = False
            return True

    def load_pickle(self):
        '''
        load pickle file, or from text
        https://stackoverflow.com/questions/243831/unicode-block-of-a-character-in-python
        retrieved from http://unicode.org/Public/UNIDATA/Blocks.txt
        '''
        if self.data_loaded:
            #print('block data already loaded...')
            return True

        #print('load_pickle...')
        try:
            ret = self.load_pickle_impl()
            self.data_loaded = True
            return ret
        except IOError:
            print('pickle file not found, try to load text file')
            self.blocks = []

        if not os.path.exists(self.txtfile):
            print(f'{self.txtfile} not found, exit')
            return False

        pattern = re.compile(r'([0-9A-F]+)\.\.([0-9A-F]+);\ (\S.*\S)')
        with open(self.txtfile, 'rt', encoding='utf8') as f:
            for line in f.readlines():
                m = pattern.match(line)
                if m:
                    start, end, name = m.groups()
                    self.blocks.append((int(start, 16), int(end, 16), name))
        self.data_loaded = True
        self.need_save = True
        self.save_pickle()
        return True

    def save_pickle_impl(self):
        ''' implementation of save pickle '''
        with open(self.pfile, 'wb') as outf:
            pickle.dump(self.blocks, outf)

    def save_pickle(self):
        ''' save pvalues into pickle file '''
        if self.blocks is None:
            return
        #print('save_pickle...')
        if self.need_save:
            self.save_pickle_impl()
            self.need_save = False
        # else:
        #     print('no need to save')


def main():
    ''' main '''
    with UnicodeBlock() as s:
        for _ in range(10):
            r = random.randint(0, 0x2ffff)
            print(f'{r:6X}', end='  ')
            print(s.block(chr(r)))

if __name__ == '__main__':
    main()
