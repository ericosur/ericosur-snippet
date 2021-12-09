#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
simple python dict usage
'''

def main():
    '''main function'''
    d = {'name':'bob', 'number':99, 'phone':'123456789'}
    for key, value in d.items():
        print(f"{key} => {value}")

    # pylint not recommend:
    #for key in d.keys():
    #    print(key, '=>', d[key])

if __name__ == '__main__':
    main()
