#!/usr/bin/python3
#coding: utf-8

'''

Fibonacci number

- Demo a fib function which would store calculated fib_redis(n) to redis
  to elimate unnecessary recursive and calculation

'''

from random import randint
import sys
import redis

class FibRedis():
    ''' fib w/ redis '''
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, \
            decode_responses=True, charset='utf-8', password=None)
        self.key = 'fibhash'
        self.query = 0
        # field pattern
        # fib{n}
        try:
            self.redis.ping()
        except redis.exceptions.ConnectionError as e:
            print('Need redis server running\n', e)
            sys.exit(1)

    @staticmethod
    def original_fib(n: int) -> int:
        ''' simple recursive version to get fib '''
        if n <= 2:
            return 1
        return FibRedis.original_fib(n - 1) + FibRedis.original_fib(n - 2)

    def fib(self, n: int) -> int:
        ''' calculate fib values with redis cache '''
        if n <= 2:
            return 1

        if not isinstance(n, int):
            n = int(n)

        field = f'fib{n}'
        ret = self.redis.hexists(self.key, field)
        if ret == 1:
            ans = self.redis.hget(self.key, field)
            return int(ans)

        # this answer does not exist in redis
        #print(f'no cache for {n}')
        ans = self.fib(n - 1) + self.fib(n - 2)
        # store into redis
        self.redis.hset(self.key, field, ans)
        return int(ans)

    def action(self):
        ''' action '''
        # demo 50 <= x <= 200
        LOWER = 50 + randint(1, 150)
        for i in range(LOWER, LOWER+10):
            ret = self.fib(i)
            print(f'fib({i}) = {ret}')


def main():
    ''' main '''
    Solution = FibRedis()
    Solution.action()


if __name__ == '__main__':
    main()
