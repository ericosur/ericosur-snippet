#!/usr/bin/env python3

''' trivia regexp demo of python '''

import re

def main():
    ''' main '''
    test = ['1', '01', '2', '03', '5', '8', '13', '21', '34', '101']
    pattern = r"^([1-9][0-9]?|)$"
    p = re.compile(pattern)

    for i in test:
        m = p.match(i)
        print(i, "\t", end='')
        if m is None:
            print("is not matched")
        else:
            print("is matched: ", m.group(1))

if __name__ == '__main__':
    main()
