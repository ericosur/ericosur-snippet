#!/usr/bin/python3
# coding: utf-8

'''
try types
'''

def main():
    ''' main '''
    def test(x):
        ''' test '''
        print(type(x))
        if isinstance(x, float):
            print("float", x)
        elif isinstance(x, int):
            print("int", x)

    arr = [3.14159, 3982, 4397913753]
    map(test, arr)

if __name__ == '__main__':
    main()
