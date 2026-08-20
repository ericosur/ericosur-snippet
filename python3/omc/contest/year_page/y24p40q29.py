'''
P29 Q24.
P = 2**2 + 4**2 + 6**2 + ... + 98**2 + 100**2
Q = 1**2 + 3**2 + 5**2 + ... + 99**2
S = (P - Q) / 50

3, 7, 11, ..., 199

'''

def mk_list(start, upper):
    ''' make evens <= upper '''
    n = start
    the_list = []
    while n <= upper:
        the_list.append(n)
        n += 2
    return the_list


def main():
    ''' main '''
    p = mk_list(2, 100)
    print(p)
    q = mk_list(1, 99)
    print(q)

if __name__ == '__main__':
    main()
