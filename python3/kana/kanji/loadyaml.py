#!/usr/bin/env python3
# coding: utf-8

''' loading yaml '''

import yaml

def main():
    ''' main '''
    fn = "kanji.yaml"
    with open(fn, 'rt', encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    for d in data:
        print(data[d])

if __name__ == '__main__':
    main()
