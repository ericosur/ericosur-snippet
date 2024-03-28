'''
Q5. 一個四位數能被9整除，若將其個位數位擦掉，剩下的三位數能被4整除，試求滿足條件的最大四位數
'''

def main():
    ''' main '''
    for n in range(9999,9000,-1):
        #print(n)
        if n % 9 == 0:
            p = n // 10
            #print(f'{p=}')
            if p % 4 == 0:
                print(f'{n=}, {p=}')
                break

if __name__ == '__main__':
    main()
