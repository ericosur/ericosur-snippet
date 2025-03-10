#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position
#
# mypy: ignore-errors


'''

factorial n!

It will save calculated n! into redis.

require redis server is running!
'''

import sys
from random import randint

import redis

# ruff: noqa: E402
sys.path.insert(0, '.')
sys.path.insert(0, '..')
from myutil import get_home, read_jsonfile


class FactorialRedis():
    ''' fib w/ redis '''
    def __init__(self):
        self.redis = None
        self.key = 'fachash'
        self.query = 0
        self._connect()
        # field pattern
        # fac{n}

    def _connect(self):
        ''' connect to redis '''
        h = get_home()
        fn = h + '/Private/redis.json'
        data = read_jsonfile(fn)
        print(f"host: {data['host']}, port: {data['port']}")
        try:
            self.redis = redis.Redis(host=data['host'], port=data['port'], \
                decode_responses=True, charset='utf-8', password=None)
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
        # store into redis
        self.redis.hset(self.key, field, ans)   # store into redis
        return int(ans)

    def action(self):
        ''' action '''
        # demo 11 <= x <= 40
        LOWER = 10 + randint(1, 30)
        for i in range(LOWER, LOWER+10):
            ret = self.factorial(i)
            print(f'factorial({i}) = {ret}')


def main():
    ''' main '''
    Solution = FactorialRedis()
    Solution.action()


if __name__ == '__main__':
    main()
