#!/usr/bin/python3
# coding: utf-8

'''
number root is the sum of digits till smaller than 10
here we define a "product root", multiple each digits till smaller than 10
'''

def product_root(n):
    ''' product root '''
    ans = list()
    # n must be larger than 10
    if n <= 10:
        return ans
    val = n
    while True:
        ans.append(val)
        if val < 10:
            break
        val = (n // 10) * (n % 10)
        n = val
    return ans

def output_csv(vals):
    ''' output csv '''
    r = [ str(x) for x in vals ]
    s = ','.join(r)
    print(s)

def main():
    ''' main '''
    # print header
    last_two_digits = set()
    print("number,1st,2nd,3rd,4th")
    for i in range(1, 100):
        a = product_root(i)
        if len(a) > 3:
            last_two_digits.add(a[-2])
    r = list(last_two_digits)
    r.sort()
    print(r)

if __name__ == '__main__':
    main()
