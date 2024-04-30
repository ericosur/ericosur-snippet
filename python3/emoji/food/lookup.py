#!/usr/bin/python3
# coding: utf-8
#
# pylint: disable=wrong-import-position
#

'''
picked up some emoji
'''

import sys

sys.path.insert(0, "..")
sys.path.insert(0, "../..")
from myutil import is_file, read_textfile, die
from en_emoji import EMOJI


def logd(*args, **wargs):
    ''' logd '''
    debug = True
    if debug:
        print(*args, **wargs)


class LookupEmoji():
    ''' pick up emojis
    from foods.txt
    look up in en_emoji.py
    '''
    foods_file = "foods.txt"

    def __init__(self):
        self.text_emojis = []
        self.swapped_emojis = {}
        self.__load_data()

    def __load_data(self):
        if not is_file(self.foods_file):
            die(f"file not found: {self.foods_file}")
            return

        tmp = read_textfile(self.foods_file)
        self.text_emojis = tmp.splitlines()
        logd("len of self.text_emojis:", len(self.text_emojis))
        self.swapped_emojis = {value: key for key, value in EMOJI.items()}
        logd("len of self.swapped_emojis:", len(self.swapped_emojis))

    def test_shoot(self):
        ''' for loops '''
        for one_key in self.keys:
            k = one_key.replace(' ', '_')
            k = k.lower()
            ret = partial_match(self.emojikeys, k)
            self.results[k] = ret

    def action(self):
        ''' action '''
        # will output to file
        outfile = "ofile.py"
        with open(outfile, "wt", encoding='UTF-8') as ofile:
            for k in self.text_emojis:
                r = self.swapped_emojis.get(k)
                print(f'"{k}": "{r}",', file=ofile)
        print(f'output to {outfile}')

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    LookupEmoji.run()


if __name__ == '__main__':
    main()
