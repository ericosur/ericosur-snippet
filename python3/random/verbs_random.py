#!/usr/bin/env python3

'''
get random verbs
'''

import argparse
import json
import os
import random
import re

from random_common import do_nothing, get_logd, prt

logd = do_nothing


class GetVerbs:
    ''' get verbs from data file '''
    repeat = 5
    # data from: https://github.com/monolithpl/verb.forms.dictionary
    csvfn = '../data/verbs-dictionaries.csv'
    jsonfn = '../data/verbs-dictionaries.json'

    def __init__(self):
        self.verbs = self.__read_json(self.jsonfn)

    def __read_json(self, fn) -> list:
        ''' read json file and return a list of verbs '''
        verbs = []
        if not os.path.isfile(fn):
            raise FileNotFoundError(f"File not found: {fn}")
        logd(f'Reading verbs from {fn}')
        with open(fn, 'rt', encoding='UTF-8') as f:
            try:
                data = json.load(f)
                for item in data:
                    text = item[0]
                    if " " not in text:
                        verbs.append(text)
            except FileNotFoundError as e:
                logd(f"Error reading {fn}: {e}")
        return verbs

    def __read_csv(self, fn) -> list:
        ''' read csv file and return a list of verbs '''
        verbs = []
        #home = os.environ.get('HOME')
        if not os.path.exists(fn):
            raise FileNotFoundError(f"File not found: {fn}")
        logd(f'Reading verbs from {fn}')
        with open(fn, 'rt', encoding='UTF-8') as f:
            try:
                cnt = 0
                for line in f:
                    line = line.strip()
                    m = re.match(r'^([a-z]+)\s', line)
                    if m:
                        verbs.append(m.group(0))
                        cnt += 1
            except FileNotFoundError as e:
                logd(f"Error reading {fn}: {e}")
        return verbs

    def action(self):
        ''' perform the action of getting random verbs '''
        if not self.verbs:
            print("No verbs found.")
            return
        #logd(f"Found verbs: {self.verbs}")
        logd(f"length verbs: {len(self.verbs)}")
        logd(f'the last verb: {self.verbs[-1]}')
        prt('Random verbs:')
        cnt = 0
        brake = 0
        while cnt < self.repeat:
            brake += 1
            verb = random.choice(self.verbs)
            if len(verb) > 3 and len(verb) < 6:
                prt(f"{verb}")
                cnt += 1
            if brake > 100:
                prt("Too many iterations, breaking the loop.")
                break

    @classmethod
    def run(cls):
        ''' run the get verbs '''
        obj = cls()
        obj.action()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get random verbs with 4-5 character length')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug logging')
    args = parser.parse_args()
    
    if args.debug:
        logd = get_logd()
    else:
        logd = do_nothing
    
    GetVerbs.run()
