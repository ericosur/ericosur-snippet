#!/usr/bin/python3
#coding: utf-8

'''

factorial n!

It will save calculated n! into redis.

require redis server is running!
'''

import sys
import redis

class FactorialRedis():
    ''' fib w/ redis '''
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
        self.key = 'fachash'
        self.query = 0
        # field pattern
        # fac{n}
        try:
            self.redis.ping()
        except redis.exceptions.ConnectionError as e:
            print('Need redis server running\n', e)
            sys.exit(1)

    @staticmethod
    def stupid_factorial(m: int) -> int:
        '''
        a trivia way to get n! recursively
        '''
        if m <= 1:
            return 1

        return m * FactorialRedis.stupid_factorial(m - 1)

    def factorial(self, n: int) -> int:
        ''' calculate fib values with redis cache '''
        if 0 <= n <= 1:
            return 1

        if not isinstance(n, int):
            n = int(n)

        field = f'fac{n}'
        ret = self.redis.hexists(self.key, field)

        if ret == 1:
            ans = self.redis.hget(self.key, field)
            return int(ans)

        # this answer does not exist in redis
        #print(f'no cache for {n}')
        ans = n * self.factorial(n - 1)
        self.redis.hset(self.key, field, ans)   # store into redis
        return int(ans)

    def action(self):
        ''' action '''
        for i in range(30, 40):
            ret = self.factorial(i)
            print(f'factorial({i}) = {ret}')


def main():
    ''' main '''
    Solution = FactorialRedis()
    Solution.action()


if __name__ == '__main__':
    main()
