#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''

Fibonacci number

- Demo a fib function which would store calculated fib_redis(n) to redis
  to elimate unnecessary recursive and calculation

require redis server is running!
'''

import os
import sys
from random import randint

import redis

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import get_home, read_jsonfile


class FibRedis():
    ''' fib w/ redis '''
    def __init__(self):
        self.redis = None
        self.key = 'fibhash'
        self.query = 0
        self._connect()
        # field pattern
        # fib{n}

    def _connect(self):
        ''' connect to redis '''
        fn = os.path.join(get_home(), 'Private', 'redis.json')
        data = read_jsonfile(fn, debug=True)
        if data is None:
            print('[FAIL] no data')
        print(f"host: {data['host']}, port: {data['port']}")
        try:
            self.redis = redis.Redis(host=data['host'], port=data['port'], \
                decode_responses=True, charset='utf-8', password=None)
            self.redis.ping()
        except redis.exceptions.ConnectionError as e:
            print('Need redis server running\n', e)
            sys.exit(1)

    @staticmethod
    def _fib(n: int) -> int:
        ''' simple recursive version to get fib '''
        if n <= 2:
            return 1
        return FibRedis._fib(n - 1) + FibRedis._fib(n - 2)

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

    def show_stat(self) -> None:
        ''' show stat '''
        print('key:', self.key)
        ret = self.redis.hlen(self.key)
        print('heln:', ret)

    @classmethod
    def run(cls):
        ''' run demo '''
        obj = cls()
        obj.show_stat()
        print('-----')
        RANGE = 2
        LOWER = 3
        UPPER = 999
        REPEAT = 1
        pivot = randint(LOWER, UPPER)
        for _ in range(REPEAT):
            for i in range(pivot-RANGE, pivot+RANGE):
                ret = obj.fib(i)
                print(f'fib({i}) = {ret})')
            print('-----')


def main():
    ''' main '''
    FibRedis.run()


if __name__ == '__main__':
    main()
