#!/usr/bin/python3
# coding: utf-8

'''
P36 Q15. 把1059, 1417 和2312分別除以正整數d，
得到的餘數都是r 而且r是大於1的整數，試求d-r的值
'''

vals = [1059, 1417, 2312]

def valmods(d):
    '''
    list of reminders
    '''
    rems = []
    for v in vals:
        r = v % d
        rems.append(r)
    return rems

def validate(the_list):
    ''' need r > 1 '''
    [a, b, c] = the_list
    if a>1 and b>1 and c>1:
        if a==b==c:
            return True
    return False

def main():
    ''' main '''
    for n in range(3,999):
        r = valmods(n)
        if validate(r):
            print(n, r)

if __name__ == '__main__':
    main()
