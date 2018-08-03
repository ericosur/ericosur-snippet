#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
simple python dict usage
'''

from __future__ import print_function

def main():
    '''main function'''
    d = {'name':'bob', 'number':'99', 'phone':'123456789'}
    for key, value in d.iteritems():    # this statement for python 2.x
        print("{} => {}".format(key, value))

    # use for key, value in d.items():   for python 3.x

    # pylint not recommend:
    #for key in d.keys():
    #    print(key, '=>', d[key])

if __name__ == '__main__':
    main()
