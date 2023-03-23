#!/usr/bin/python3
# coding: utf-8

'''
provide a basic interface/class for load/save/search primes

need redis service running

Compares to text file, pickle, and redis

---------------------------------------------------------------------
The size of primelist is 3 million numbers.

Time to read/parse a text file and store into list: 5.773188352584839 sec
Time to store prime list into redis one-by-one: 439.2567970752716 sec
Time to load a list from redis (LRANGE) :
    14.280343770980835 sec
    15.271966218948364 sec

Time to save python list slice (200_000 elements) bulkly to redis:
    7.947754621505737 sec

'''

import os
import re
import sys
import time
from random import randint

# if hiredis is installed as well, it will improve the query speed a lot
# pylint: disable=import-error
try:
    import redis
except ImportError:
    print("ImportError: import redist")

# local modules
from findlist_func import index, find_le, find_ge
from myutil import read_jsonfile, get_home

class StorePrimeToRedis():
    ''' class will help to handle read pickle file '''
    def __init__(self):
        #print('__init__')
        # init values
        self.txtfile = 'large.txt'
        self.primes = []
        self.redis = None
        self.key = 'primelist'
        self.test_key = "primelist-test"
        self._connect()
        self._test_primes_in_redis()

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

    def _test_primes_in_redis(self):
        try:
            r = self.redis.exists(self.key)
            if r == 1:
                print(f'[INFO] yes, {self.key} exists in redis server...')
                r = self.redis.llen(self.key)
                print(f"[INFO] there are {r} values in {self.key} from redis")
                # load primes from redis to local list

                print('[INFO] load primes from database...')
                start = time.time()
                r = self.redis.lrange(self.key, 0, -1)
                during = time.time() - start
                print(f'redis.lrange need: {during} sec')

                start = time.time()
                self.primes = [ int(v) for v in r ]
                during = time.time() - start
                print(f'convert str to int: {during} sec')
            else:
                print(f'{self.key} not found... load from text file instead...')
                self.load_text()
        except redis.exceptions.ConnectionError as e:
            print('Need redis server running\n', e)
            sys.exit(1)

        print('[INFO] the last prime number is:', self.primes[-1])

    def _test_store(self):
        '''
        if test_key exists, remove it and then store list into redis
        '''
        if self.redis.exists(self.test_key):
            print(f"test: yes {self.test_key} exists, will unlink it...")
            self.redis.unlink(self.test_key)

        self.store_wholelist_to_redis(self.test_key)

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
        self.store_wholelist_to_redis(self.key)


    def store_list_to_redis(self, redis_key: str) -> None:
        ''' store the primelist into redis
        [INFO] It takes 439.2567970752716 sec to store a list into redis
        '''
        start = time.time()
        for v in self.primes:
            self.redis.rpush(redis_key, v)
        during = time.time() - start
        print(f'[INFO] It takes {during} sec to store a list into redis')

    def store_wholelist_to_redis(self, redis_key: str) -> None:
        ''' store the primelist into redis
            if the len of list = 3M, cannot store it at one time
            so store it batchly
            [INFO] It takes 7.790482997894287 sec to store (slice_size=500k)
        '''
        SLICE_SIZE = 500000
        start = time.time()

        left_cnt = len(self.primes)
        pivot_start = 0
        pivot_end = pivot_start + SLICE_SIZE
        ssize = SLICE_SIZE
        while True:
            send_primes = self.primes[pivot_start:pivot_end]
            self.redis.rpush(redis_key, *send_primes)
            left_cnt -= ssize
            print('left cnt:', left_cnt)
            if left_cnt <= 0:
                break
            if left_cnt < SLICE_SIZE:
                ssize = left_cnt
            pivot_start += ssize
            pivot_end = pivot_start + ssize

        during = time.time() - start
        print(f'[INFO] It takes {during} sec to store a list into redis ({redis_key})')

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

    @staticmethod
    def check_by_small_primes(v: int) -> bool:
        ''' use small primes to filter out non-prime numbers '''
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                73, 79, 83, 89, 97]

        for p in small_primes:
            if v <= p:  # ==: small primes, <: no need to test more
                return True
            if v % p == 0:
                return False
        # pass small primes test
        return True

    def test_redis(self, v: int):
        ''' for current version of py-redis, no lpos() available '''
        USE_LOCAL_FILTER = False
        if USE_LOCAL_FILTER:
            r = self.check_by_small_primes(v)
            if not r:   # pass the small prime test
                print(f'{v} cannot pass easy prime test, not a prime')
                return
        # before py-reids 4.0.0, there is no redis.lpos()
        ver = redis.__version__ # got 3.5.3
        ver.replace('.', '')    # got 353
        if int(ver) >= 400:
            r = self.redis.lpos(self.key, v)
        else:
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

def demo(sol):
    ''' demo '''
    print()
    print('[INFO] Running tests...')
    print('-' * 50)
    REPEAT = 20
    start = time.time()
    for _ in range(REPEAT):
        sol.test_redis(randint(10e5, 49999999))
        print('-' * 50)
    during = time.time() - start
    print(f'[INFO] takes {during} sec to query {REPEAT} times')

def main():
    ''' main '''
    sol = StorePrimeToRedis()
    demo(sol)

if __name__ == '__main__':
    main()
