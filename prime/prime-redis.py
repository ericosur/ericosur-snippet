#!/usr/bin/python3
# coding: utf-8

'''
provide a basic interface/class for load/save/search primes

need redis service running

Compares to text file, pickle, and redis

'''

import os
import re
import sys
import time
from random import randint

import redis
from findlist_func import index, find_le, find_ge

class StorePrimeToRedis():
    ''' class will help to handle read pickle file '''
    def __init__(self):
        #print('__init__')
        # init values
        self.txtfile = 'large.txt'
        self.primes = []
        self.redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
        self.key = 'primelist'
        self._test_redis()

    def _test_redis(self):
        try:
            self.redis.ping()
            r = self.redis.exists(self.key)
            if r == 1:
                print(f'[INFO] yes, {self.key} exists in redis server...')
                r = self.redis.llen(self.key)
                print(f"[INFO] there are {r} values in {self.key} from redis")
                # load primes from redis to local list
                print('[INFO] load primes from database...')
                start = time.time()
                r = self.redis.lrange(self.key, 0, -1)
                self.primes = [ int(v) for v in r ]
                during = time.time() - start
                print(f'load from redis during: {during}')
            else:
                print(f'{self.key} not found...')
                self.load_text()
        except redis.exceptions.ConnectionError as e:
            print('Need redis server running\n', e)
            sys.exit(1)

        print('[INFO] the last prime number is:', self.primes[-1])

    @staticmethod
    def get_local_data_path() -> str:
        ''' get data file from local '''
        p = os.getenv('HOME') + '/.prime/'
        if os.path.exists(p):
            return p
        return None

    def confirm_datafile(self) -> bool:
        ''' will confirm self.txtfile existence or
            exit the script
        '''
        # find data file from data path first
        p = self.get_local_data_path()
        datafn = p + self.txtfile
        if os.path.exists(datafn):
            self.txtfile = datafn
            return True
        # find data file local directory
        datafn = self.txtfile
        if os.path.exists(datafn):
            return True
        print(f'[ERROR] cannot find data file: {self.txtfile}')
        sys.exit(1)
        return False

    def load_text(self) -> None:
        '''
        load prime numbers from file and store into a list
        and push into redis list at the same time
        '''
        self.confirm_datafile()
        print(f'[INFO] read prime numbers from: {self.txtfile}')
        with open(self.txtfile, "rt", encoding='utf8') as txtinf:
            count = 0
            # expect one prime number one line
            start = time.time()
            for ln in txtinf.readlines():
                count += 1
                if count % 10000 == 0:
                    print('.', end='')
                ln = ln.strip()
                if ln == '':
                    print('empty, break')
                    continue

                result = re.match(r'^(\d+)$', ln)
                if result:
                    el = int(result.groups()[0])
                    # here fill the self.primes and rpush into redis
                    self.primes.append(el)
            print()
            during = time.time() - start
        print(f'[INFO] Read from text file: {count} lines...')
        print(f'[INFO] It takes {during} sec to read into a python list')
        self.store_list_to_reids()


    def store_list_to_reids(self) -> None:
        ''' store the primelist into redis '''
        start = time.time()
        for v in self.primes:
            self.redis.rpush(self.key, v)
        during = time.time() - start
        print(f'[INFO] It takes {during} sec to store a list into redis')


    def find(self, val: int) -> int:
        ''' find val in list of primes '''
        #if val in self.pvalues:
        return self.primes.index(val)
        #return -1

    def index(self, val: int) -> int:
        ''' use external index() '''
        return index(self.primes, val)

    def get_primes_less_than(self, val: int) -> list:
        ''' get a list of primes less than given value '''
        _max = self.primes[-1]
        _min = self.primes[0]
        if val > _max or val < _min:
            print('[ERROR] out of bound')
            return None
        if val == _min:
            return [2]
        (p, _) = self.search_between_idx(val)
        if p is None:
            print('[ERROR] cannot operate')
            return None
        # ????
        plist = self.primes[:p+1]
        return plist

    def bisect_between_idx(self, val: int) -> tuple:
        '''
        use bisect to search value in list return index for lower, upper bound
        '''
        if self.primes is None:
            print('[FAIL] predefined data not available')
            return (None, None)
        i = index(self.primes, val)
        if i != -1:
            return (i, None)
        # not exactly prime, search lower, upper bound
        a = self.primes
        x = val
        try:
            _, p = find_le(a, x)
            _, q = find_ge(a, x)
            return (p, q)
        except ValueError:
            print(f'something wrong for {x}, OOB?')
            return (None, None)


    def search_between_idx(self, val):
        '''
        search value within primes, return index for lower, upper bound
        '''
        if self.primes is None or self.primes == []:
            print('[FAIL] predefined data not available')
            return (None, None)
        if val in self.primes:
            return (val, None)
        if val < self.primes[0]:
            print(f'{val} is smaller than lower bound')
            return (None, None)
        if val > self.primes[-1]:
            print(f'{val} is larger than upper bound')
            return (None, None)

        # start to binary search
        _max = len(self.primes) - 1
        _min = 0
        _mid = 0
        _cnt = 0
        while True:
            _cnt += 1
            _mid = (_min + _max) // 2
            if self.primes[_mid] > val:
                _max = _mid
            else:
                _min = _mid
            if _min > _max or _min == _max - 1:
                break
            if _cnt > 20:
                print('exceed count')
                break
        return (_min, _max)


    def at(self, idx):
        ''' get value at index '''
        try:
            return self.primes[idx]
        except (IndexError, TypeError):
            return None

    @staticmethod
    def show(v, p, q):
        ''' show '''
        if p is None and q is None:
            return
        if q is None:
            print(f'{v} is a prime {p}')
        else:
            lhs = abs(v - p)
            rhs = abs(v - q)
            if lhs <= rhs:
                arrow = "<-----"
            else:
                arrow = "----->"
            print(f'{v} is between ({p} {arrow} {q})')

    def query_value(self, v: int):
        ''' test '''
        (p, q) = self.bisect_between_idx(v)
        if p is None:
            print('\tno answer for this')
            return
        self.show(v, self.at(p), self.at(q))

    def test_redis(self, v: int):
        ''' for current version of py-redis, no lpos() available '''
        #r = self.redis.lpos(self.key, v)
        cmd = f'lpos {self.key} {v}'
        r = self.redis.execute_command(cmd)
        if r:
            print(f'{v} in the pos {r} of list')
        else:
            # cannot query it from database, use native python list to query
            print(f'{v} is not a prime number (not found in redis)...')
            self.query_value(v)


    def list_nearby(self, v: int) -> list:
        ''' print primes nearby v '''
        (p, q) = self.bisect_between_idx(v)
        #print('p, q:', p, q)
        if p is None:
            print('\tno answer for this')
            return None
        begin = 0
        count = 4
        if p > count:
            begin = p - count
        if q is None:   # pos p is a prime
            end = p + count + 1
        else:
            end = p + count + 2
        arr = self.primes[begin:end]
        return arr

def main():
    ''' main '''
    sol = StorePrimeToRedis()
    print('[INFO] Running tests...')
    print('-' * 50)
    REPEAT = 10
    start = time.time()
    for _ in range(REPEAT):
        sol.test_redis(randint(10e5, 49999999))
        print('-' * 50)
    during = time.time() - start
    print(f'[INFO] takes {during} sec to query {REPEAT} times')

if __name__ == '__main__':
    main()
