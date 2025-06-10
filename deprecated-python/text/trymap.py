#!/usr/bin/python3
# coding: utf-8

'''
string functions
'''

def flip(s):
    ''' flip string '''
    a = list(s)
    a.reverse()
    return ''.join(a)

def capitalize(s):
    ''' captalize '''
    a = s.split()
    def mycap(s):
        sl = list(s)
        sl[0] = sl[0].upper()
        return ''.join(sl)
    a = map(mycap, a)
    return ' '.join(a)

def main():
    ''' main '''
    normalize = lambda s: ' '.join(s.split())

    s = '''once upon a time,
    there was a castle in
    the bad land
    '''

    print('      flip:', flip(s))
    print('capitalize:', capitalize(normalize(s)))

if __name__ == '__main__':
    main()
