#!/usr/bin/env python3
# coding: utf-8
#

'''
query elements with class ShowElement
'''

from brief import ShowElement

def main():
    ''' main '''
    obj = ShowElement()
    obj.query_list([16, 92, 53, 34, 53])
    obj.query_list([9, 92, 5, 92, 19, 53])
    obj.query_list(['I', 'Am', 'At', 'U', 'Ra'])
    obj.query_list(['U', 'Hs', 'Mn', 'Ta'])
    obj.query_list(['Er', 'I', 'Co', 'S', 'U'])
    obj.query_list(['Ra', 'S', 'Mn', 'S'])

if __name__ == "__main__":
    main()
