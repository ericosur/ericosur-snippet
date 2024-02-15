#!/usr/bin/env python3
# coding: utf-8

'''
有一個七位數的魔法數字前三位數與後四位數的和為9314，
前四位數與後三位數之和為2132，求此數為？
'''

def get_head(digits, no):
    '''
    input val=1234567, no=4, get 1234
    input val=23579, no=3, get 235
    '''
    assert no<len(digits)
    s = slice(0, no)
    return digits[s]

def get_tail(digits, no):
    '''
    input val=1234567, no=4, get 4567
    '''
    assert len(digits)>=no
    return digits[len(digits)-no:]

def get_value(digits):
    ''' given digits, return value '''
    val = 0
    try:
        for d in digits[:-1]:
            val += int(d)
            val *= 10
        val += int(digits[-1])
    except:
        print("something wrong")
        return None
    return val

def test():
    ''' test '''
    digits = list(str(1234567))
    print(get_head(digits, 3))
    print(get_tail(digits, 4))
    print(get_value(['3','2','1']))
    print(get_value(get_tail(digits, 3)))

def action():
    ''' action '''
    drop = 0
    for i in range(1000000, 2999999+1):
        digits = list(str(i))
        if digits[3] == '8' or digits[3] == '9':
            m = get_value(get_head(digits, 3))
            n = get_value(get_tail(digits, 4))
            p = get_value(get_head(digits, 4))
            q = get_value(get_tail(digits, 3))
            print(f'{i}: {m}+{n}={m+n:5d},{p}+{q}={p+q:5d}\r', end='')
            if m+n == 9314 and p+q == 2132:
                print(f'\n{i} matched')
        else:
            drop+=1
    print()
    print(f'{drop=}')

def main():
    ''' main '''
    #test()
    action()

if __name__ == '__main__':
    main()
