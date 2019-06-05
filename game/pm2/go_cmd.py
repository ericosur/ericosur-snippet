#!/usr/bin/env python3
# coding: utf-8
#

'''
read command and do action
'''

import os
import sys
import json
import shutil
from show_gnx import ShowGnx

class CommandAction():
    ''' class to read cmd.json and data.json to do modification '''
    ADDR_CHECKSUM = 0x1114

    def __init__(self, cmd_fn, gnx_fn):
        self._cmd_fn = cmd_fn
        self._data_fn = None
        self._cmds = None
        self._data = None
        self.gnxfile = gnx_fn
        self.delta_checksum = 0

    @staticmethod
    def read_jsonfile(fn):
        '''
        specify json filename and return whole json object
        '''
        data = None
        try:
            # read from json file
            with open(fn, 'rt', encoding='UTF-8') as fh:
                data = json.load(fh)
        except FileNotFoundError as e:
            print('read_jsonfile():', e)
        return data

    def read_data(self):
        '''
        build data json from gnx file
        read data and cmd json
        '''
        # call ShowGnx to build it
        print('showgnx')
        showgnx = ShowGnx(self.gnxfile)
        showgnx.do_action()
        self._data_fn = showgnx.get_data_filename()

        self._data = CommandAction.read_jsonfile(self._data_fn)
        self._cmds = CommandAction.read_jsonfile(self._cmd_fn)
        if self._data is None or self._cmds is None:
            return False
        return True

    def perform_cmd(self):
        ''' read command from json '''

        # backup file
        new_fn = self.gnxfile.replace('GNX', 'GNX.bak')
        shutil.copyfile(self.gnxfile, new_fn)

        for cc in self._cmds:
            #print('{}: {}'.format(cc['tag'], cc['delta']))
            self.find_and_patch(cc['tag'], cc['delta'])
        #print('delta_checksum:', self.delta_checksum)

        saved_checksum = self._data['checksum']
        new_checksum = (saved_checksum + self.delta_checksum) % 2**32
        print('at addr(0x{:x}), checksum from {} to {}'.format(
            CommandAction.ADDR_CHECKSUM, saved_checksum, new_checksum))
        self.modify_addr_with_value(CommandAction.ADDR_CHECKSUM,
                                    saved_checksum, new_checksum, size=4)


    def find_and_patch(self, tag, delta):
        ''' find and patch '''
        try:
            for item in self._data['values']:
                if item['tag'] == tag:
                    new_val = item['value'] + delta
                    print('at addr(0x{:x}), from {} to {}'.format(
                        item['addr'], item['value'], new_val))
                    self.modify_addr_with_value(item['addr'], item['value'], new_val)
                    self.delta_checksum += delta
        except ValueError as e:
            print(e)

    def modify_addr_with_value(self, addr, oldvalue, newvalue, size=2):
        ''' write bytes into file '''
        old_bytes = oldvalue.to_bytes(size, byteorder='little', signed=False)
        new_bytes = newvalue.to_bytes(size, byteorder='little', signed=False)
        #print('oldvalue', old_bytes)
        #print('new_bytes', new_bytes)
        try:
            with open(self.gnxfile, 'r+b') as ofh:
                ofh.seek(addr)
                read_bytes = ofh.read(size)
                #print('read_bytes', read_bytes)
                assert read_bytes == old_bytes
                ofh.seek(addr)
                ofh.write(new_bytes)
        except FileNotFoundError as e:
            print(e)

    def do_action(self):
        ''' action '''
        if self.read_data():
            self.perform_cmd()
        else:
            print('[FAIL] something wrong')


def main(fn):
    ''' main '''
    if not os.path.isfile(fn):
        print('[FAIL] file not found:', fn)
        return

    ca = CommandAction('cmd.json', fn)
    ca.do_action()

if __name__ == '__main__':
    FN = 'F101.GNX'
    if len(sys.argv) == 1:
        main(FN)
    else:
        FN = sys.argv[1]
        main(FN)
