#!/usr/bin/env python3

'''
1<a<15
1<b<7
3*(a+b) == a*b
'''

def main():
    ''' main '''
    for a in range(15):
        for b in range(7):
            if 3*(a+b)==a*b:
                print(a, b)

if __name__ == '__main__':
    main()
