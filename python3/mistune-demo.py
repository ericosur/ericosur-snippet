#!/usr/bin/python3
# coding: utf-8

'''
demo of mistune

cannot upgrade to mistune 2.0.0 because of nbconvert or networkx?
'''

import sys
try:
    import mistune
except ImportError:
    print('cannot import mistune')
    sys.exit(1)

def main():
    ''' main '''
    print('mistune version:', mistune.__version__)

    if mistune.__version__ == "0.8.4":
        print('[ERROR] too old to run')
        return

    ifn = "README.md"
    ofn = 'test.html'
    try:
        with open(ifn, 'rt', encoding='utf-8') as fobj:
            with open(ofn, 'wt', encoding='utf-8') as fout:
                content = fobj.read()
                print(content)
                h = mistune.html(fobj)
                fout.write(h)
            print(f'read {ifn} output to {ofn}')
    except AttributeError as e:
        print(f'Maybe mistune is too old? {e}')

if __name__ == '__main__':
    main()
