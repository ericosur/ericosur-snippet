'''
Q15. 一個三位數，如果它的每一位數字都不小於另一個三位數對應數位上的數字，就稱它"吃掉"後一個三位數，
例如，472吃掉370，但是472不能吃掉228。請問，能吃掉587的三位數有多少個？
'''

def digitalize(val):
    ''' give int(1234)
    return [1,2,3,4]
    '''
    t = list(str(val))
    the_ints = [int(x) for x in t]
    return the_ints

def validate(p, q):
    ''' meet the condition '''
    if p == q:
        return False
    pp = digitalize(p)
    qq = digitalize(q)
    for i in range(3):
        if pp[i] < qq[i]:
            return False
    return True


def main():
    ''' main '''
    cnt = 0
    answers = []
    for n in range(587,999+1):
        if validate(n, 587):
            answers.append(n)
            cnt += 1
    print(f'{cnt=}')
    print(len(answers))
    print(answers)

if __name__ == '__main__':
    main()
