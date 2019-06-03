#!/usr/bin/env python3
# coding: utf-8

'''
read values from save file of princess maker 2
read tags from 'tags.txt'

{
    [
        {
            "tag": "體力",
            "value": 399,
            "addr": 0x3a
        },
        {
            "tag": "智力",
            "value": 499,
            "addr": 0x3e
        }
    ]
}
'''

import json

class ShowGnx():
    ''' class to show data in gnx file '''

    CNT = 28
    BASEADDR = 0x3a
    TAGSFILE = 'tags.txt'

    def __init__(self, fn):
        self.gnxfile = fn
        self.tags = []
        self.value_list = []
        self.read_tags()

    @staticmethod
    def get_int(bb):
        '''
        bb [in] bytes
        split 2-bytes into one integer
        return list of int
        '''
        ints = []
        for ii in range(ShowGnx.CNT):
            bs = bb[ii*2:ii*2+2]
            val = int.from_bytes(bs, byteorder='little')
            ints.append(val)
        return ints

    @staticmethod
    def show_value_list(vl):
        ''' show value from list '''
        for v in vl:
            print('(0x{:x}){}: {:>8d}'.format(v['addr'], v['tag'], v['value']))

    def read_tags(self):
        ''' read tags from file '''
        with open(ShowGnx.TAGSFILE, 'rt', encoding='UTF-8') as fh:
            for ln in fh.readlines():
                self.tags.append(ln.strip())
        #print(self.tags)


    def show_values(self):
        ''' main action '''
        try:
            with open(self.gnxfile, 'r+b') as fh:
                fh.seek(ShowGnx.BASEADDR)
                bb = fh.read(ShowGnx.CNT * 2)
                values = ShowGnx.get_int(bb)
        except FileNotFoundError as e:
            print(e.args)
            return

        for ii, (val, tag) in enumerate(zip(values, self.tags)):
            v = {}
            addr = ShowGnx.BASEADDR + ii * 2
            v['addr'] = addr
            v['value'] = val
            v['tag'] = tag
            #print(v)
            self.value_list.append(v)

        #print(value_list)
        ShowGnx.show_value_list(self.value_list)
        d = json.dumps(self.value_list)
        ofn = 'a.json'
        with open(ofn, 'wt', encoding='UTF-8') as f:
            f.write(d)
        print('also output json file:', ofn)

def main():
    ''' main '''
    fn = 'F110.GNX'
    showgnx = ShowGnx(fn)
    showgnx.show_values()

if __name__ == '__main__':
    main()
