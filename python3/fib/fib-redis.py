#!/usr/bin/python3
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
from random import randint
import sys
import redis

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_jsonfile, get_home

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
        # demo 51 <= x <= 200
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
