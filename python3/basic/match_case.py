#!/usr/bin/python3.10
# coding: utf-8

'''
patern match (need python >= 3.10)
To demo a 3.10 new feature, match-case with simple patterh

https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching

You will get a SyntaxError if run this script directly with python < 3.10
'''

def buy(thing):
    ''' buy something '''
    match thing:
        case 'apple':
            print('It is red.')
        case 'banana':
            print('It is yellow.')
        case 'grape':
            print('It is purple.')
        case _:
            print('You cannot buy it.')


if __name__ == '__main__':
    print('refuse run this script directly..., run "match.py"')
