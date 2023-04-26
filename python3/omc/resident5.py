#!/usr/bin/python3
# coding: utf-8

'''
1,2,3,4,5,6,7,8,9,10,11,13

除以1餘0
除以2餘1
除以3餘2
除以5餘4
除以4餘3
除以7餘6
除以6餘5
除以8餘7
除以9餘8
除以10餘9
除以11餘10
除以13餘11或12
'''

class Solution():
    ''' try to find the number that match residual '''
    def __init__(self):
        self.minimum = 10000
        self.maximum = 99999

    @staticmethod
    def test_by(m, n):
        ''' return true if m % n = n-1 '''
        if n <= 1:
            raise ValueError("must >= 1")
        # special case
        r = m % n
        if n == 13:
            if r == 11:
                print('n=13, r=11')
                return True
            if r == 12:
                print('n=13, r=12')
                return True
            return False

        return r == n - 1

    def is_allpass(self, m):
        ''' return true if all pass '''
        tester = [2,3,4,5,6,7,8,9,10,11,13]
        for t in tester:
            if not self.test_by(m, t):
                return False
        return True


    def test(self):
        ''' test '''
        assert self.test_by(25, 13)
        assert self.test_by(29, 14) is False
        assert self.test_by(27, 14)
        assert self.test_by(8, 3)
        assert self.test_by(9, 1) is False

    def run(self):
        ''' run '''
        for i in range(self.minimum, self.maximum+1):
            if self.is_allpass(i):
                print(i)

def main():
    ''' main '''
    sol = Solution()
    sol.run()

if __name__ == '__main__':
    main()
