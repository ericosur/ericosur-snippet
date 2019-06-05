#!/usr/bin/env python3
# coding: utf-8

'''
read values from save file of princess maker 2
read tags from 'tags.txt'
'''

import sys
import json

class ShowGnx():
    ''' class to show data in gnx file '''

    GNXFILE_SIZE = 8192
    CHECKSUM_POS = 0x1114
    CHECKSUM_LEN = 4
    CNT = 28
    BASEADDR = 0x3a
    TAGSFILE = 'tags.txt'

    def __init__(self, fn):
        #print('ShowGnx.__init__')
        self.gnxfile = fn
        self.tags = []
        self.value_list = []
        self.ofn = None
        self.read_tags()

    @staticmethod
    def get_int(bb):
        '''
        bb [in] bytes
        split 2-bytes into one integer
        return list of int
        '''
        ints = []
        for ii in range(len(bb)//2):
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
        #print('read {} tags'.format(len(self.tags)))

    @staticmethod
    def get_file_checksum(bb):
        '''
        get saved checksum from buffer
        return checksum, int
        '''
        pos1 = ShowGnx.CHECKSUM_POS
        pos2 = ShowGnx.CHECKSUM_POS + ShowGnx.CHECKSUM_LEN
        byte_checksum = bb[pos1:pos2]
        saved_checksum = int.from_bytes(byte_checksum, byteorder='little')
        return saved_checksum

    def read_gamedate(self, bb):
        ''' read game date from buffer '''
        pos_y = 0
        pos_m = 2
        size_u16 = 2
        yy_b = bb[pos_y:pos_y+size_u16]
        mm_b = bb[pos_m:pos_m+size_u16]
        year = int.from_bytes(yy_b, 'little')
        month = int.from_bytes(mm_b, 'little')
        self.append_value_list(pos_y, year, 'year')
        self.append_value_list(pos_m, month, 'month')

    def append_value_list(self, addr, val, tag):
        ''' append item into value list '''
        v = {}
        v['addr'] = addr
        v['value'] = val
        v['tag'] = tag
        self.value_list.append(v)


    def read_body(self, bb):
        '''
        bb [in] bytes
        return body_dict
        '''
        pos1 = 0xc0
        pos2 = pos1 + 5 * 2
        body_values = self.get_int(bb[pos1:pos2])
        body_tag = ['height', 'weight', 'bust', 'waist', 'hips']
        for ii, (tag, val) in enumerate(zip(body_tag, body_values)):
            addr = pos1 + ii * 2
            self.append_value_list(addr, val, tag)


    def read_values(self, bb):
        '''
        bb [in] bytes
        return jsonified str
        '''
        checksum = self.get_file_checksum(bb)
        self.read_body(bb)
        self.read_gamedate(bb)

        pos1 = ShowGnx.BASEADDR
        pos2 = ShowGnx.BASEADDR + ShowGnx.CNT * 2
        core_values = self.get_int(bb[pos1:pos2])
        for ii, (val, tag) in enumerate(zip(core_values, self.tags)):
            addr = ShowGnx.BASEADDR + ii * 2
            self.append_value_list(addr, val, tag)

        d = {
            'filename': self.gnxfile,
            'checksum': checksum,
            'values': self.value_list
        }
        return json.dumps(d, sort_keys=True, indent=2)

    def get_data_filename(self):
        ''' return 'F101.json'  '''
        return self.ofn

    def do_action(self):
        ''' main action '''
        #print('ShowGnx.do_action')
        # read from file
        try:
            with open(self.gnxfile, 'rb') as fh:
                bb = fh.read()
        except FileNotFoundError as e:
            print('ShowGnx.do_action:', e.args)
            return
        print('read from {}, {} bytes'.format(self.gnxfile, len(bb)))
        j = self.read_values(bb)

        # out to a json file
        self.ofn = self.gnxfile.replace('GNX', 'json')
        with open(self.ofn, 'wt', encoding='UTF-8') as f:
            f.write(j)
        print('also output json file:', self.ofn)

def main(fn):
    ''' main '''
    import os
    if os.path.isfile(fn):
        showgnx = ShowGnx(fn)
        showgnx.do_action()
    else:
        print('[FAIL] file not found:', fn)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        FN = 'F101.GNX'
        print('default file:', FN)
        print('    Or show_gnx.py [filename]')
        main(FN)
