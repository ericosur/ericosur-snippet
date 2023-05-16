#!/usr/bin/python

'''
when was 7n the same as sum of 1 to n?
'''

def sum_to(n):
    ''' sum from 1 to n '''
    return n*(n+1)//2

def seven(n):
    ''' 7n '''
    return 7*n

def main():
    ''' main '''
    n = 1
    while n < 20:
        n += 1
        n7 = seven(n)
        sum_n = sum_to(n)
        print(f"{n} {sum_n} {n7}")
        if n7 % sum_n == 0:
            print(f"=====> {n} {sum_n} {n7}")
            #break

def test(n):
    ''' print if the same '''
    n7 = seven(n)
    sum_n = sum_to(n)
    print(f"=====> {n} {sum_n} {n7}")


if __name__ == '__main__':
    main()
    #test(13)
