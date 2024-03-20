'''
Q11. 觀察以下的數列：請問，其中有多少個最簡分數？
⅛, 2/9, 3/10, 4/11, 5/12, … 2021/2028
'''



def gcd(m: int, n: int) -> int:
    '''
    calculate gcd number by rescursive
    '''
    if n == 0:
        return m
    return gcd(n, m % n)


def main():
    ''' main '''
    cnt = 0
    for p in range(1,2021+1):
        q = p + 7
        if gcd(p, q) == 1:
            print(p, q)
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
