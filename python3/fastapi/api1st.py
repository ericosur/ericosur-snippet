#!/usr/bin/env python
# coding: UTF-8

'''
fastapi first try

launch: fastapi dev api1st.py
open link: http://localhost:8000/docs")
'''

import sys
from time import time
from typing import Union, List, Optional

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import numpy_financial as npf

app = FastAPI()

sys.path.insert(0, "../")
sys.path.insert(0, "python3/")
from myutil import prt
sys.path.insert(0, "../../prime/")
from is_prime import is_prime
sys.path.insert(0, "../datetime/")
sys.path.insert(0, "../datetime/dooms/")
sys.path.insert(0, "python3/datetime/dooms/")
from dooms_day import DoomsDay
from be_prepared import prepare_values

@app.get("/")
def read_root():
    ''' just say hello '''
    return {"hello": "world"}

@app.get("/doomsday/{year}")
def doomsday(year: int):
    ''' return the doomsday magic number from given year '''
    ans = None
    if year < 1600:
        ans = "year need gt 1600"
        return {"func": "doomsday", "year": year, "ans": ans}
    try:
        ans = DoomsDay.get_doom_num(year)
    except ValueError:
        ans = "error"
    return {"func": "doomsday", "year": year, "ans": ans}

class GivenValueAbc(BaseModel):
    ''' give year and abc '''
    value: int  # required field
    after: Optional[int] = 0   # optional field
    before: Optional[int] = 0
    context: Optional[int] = 0

@app.put("/dooms/{item_id}")
def doomyears(item_id: int, years: GivenValueAbc):
    ''' given years and abc '''
    ret = {"item_id": item_id, "func": "doomyears", "input": years, "output": None}
    yy = prepare_values(years.value, after=years.after, before=years.before, radius=years.context)
    dt = {}
    for y in yy:
        dt[str(y)] = DoomsDay.get_doom_num(y)
    ret["output"] = dt
    return ret

@app.put("/getprimes/{item_id}")
def get_primes(item_id: int, given: GivenValueAbc):
    ''' give value and abc '''
    ret = {"item_id": item_id, "func": "get_primes", "input": given, "output": None}
    vals = prepare_ints(given.value, after=given.after, before=given.before, radius=given.context)
    primes = []
    for i in vals:
        if is_prime(i):
            primes.append(i)
    ret["checked_length"] = len(vals)
    ret["output_length"] = len(primes)
    ret["output"] = primes
    return ret

@app.put("/getafterprimes/{item_id}")
def get_no_primes_after(item_id: int, given: GivenValueAbc):
    ''' give value and abc, here only __after__ is used,
        will return the number of primes after the given number,
        for example, give value=1000, after=20, will return
        20 prime numbers after 1000
    '''
    ret = {"item_id": item_id, "func": "getafterprimes", "input": given, "output": None}
    primes = []
    ulimit = given.after if given.after > 0 else 1
    i = given.value if given.value > 0 else 1
    # due to some limitation of async/concurrent, cannot move the while
    # loop into another function
    while len(primes) < ulimit:
        if is_prime(i):
            primes.append(i)
        i += 1
    ret["the_last_i"] = i
    ret["output_length"] = len(primes)
    ret["output"] = primes
    return ret

@app.put("/getaroundprimes/{item_id}")
def get_no_of_primes_around(item_id: int, given: GivenValueAbc):
    ''' give __value__ and __context__
        will return the number of primes around the given number,
        for example, give value=500, context=11, will return
        22 prime numbers after/before 500
    '''
    ret = {"item_id": item_id, "func": "getaroundprimes", "input": given, "output": None}
    # do wanna infinite loop
    ulimit = given.context if given.context > 0 else 1
    aftp = []
    i = given.value if given.value > 0 else 1
    while len(aftp)<ulimit:
        if is_prime(i):
            aftp.append(i)
        i += 1
    befp = []
    j = given.value if given.value > 0 else 1
    while len(befp)<ulimit:
        if is_prime(j):
            befp.append(j)
        j -= 1
        if j < 1:
            break
    ret["the_last_i"] = i
    ret["the_last_j"] = j
    primes = befp.copy()
    primes.extend(aftp)
    primes.sort()
    ret["output_length"] = len(primes)
    ret["output"] = primes
    return ret

class GivenNumbers(BaseModel):
    ''' data class '''
    numbers: List[int]

@app.put("/checkprime/{item_id}")
def check_prime(item_id: int, given: GivenNumbers):
    ''' return prime or composite after checking given number '''
    ret = {"item_id": item_id, "func": "check_prime", "primes": []}
    for i in given.numbers:
        if is_prime(i):
            ret["primes"].append(i)
    ret['checked_length'] = len(given.numbers)
    return ret

class NormDist(BaseModel):
    ''' data class '''
    mu: float
    sigma: float
    no: int

@app.put("/normdist/{item_id}")
def gen_normdist(item_id: int, given: NormDist):
    ''' generate random normal distribution '''
    ret = {"item_id": item_id, "func": "gen_normdist", "input": given, "output": None}
    rng = np.random.default_rng(int(time()))
    arr = given.mu + given.sigma * rng.standard_normal(size=given.no)
    ret["output"] = arr.tolist()
    return ret

def prepare_ints(v: int, after: int=None, before: int=None, radius: int=None) -> List[int]:
    ''' prepare ints '''
    after = 0 if after is None else after
    before = 0 if before is None else before
    radius = 0 if radius is None else radius
    if radius!=0:
        after, before = radius, radius
    upper = v + after
    lower = v - before
    if lower>upper:
        lower,upper = upper,lower
    vals = []
    for y in range(lower,upper+1):
        vals.append(y)
    return vals

class PmtItem(BaseModel):
    ''' data class '''
    rate: float
    nper: int
    pv: int

@app.put("/pmt/{item_id}")
def pmt(item_id: int, the_pmt: PmtItem):
    ''' calculate pmt '''
    rets = {"item_id": item_id, "func": "pmt", "input": the_pmt, "payment": 0}
    # Calculate the monthly payment
    payment = npf.pmt(the_pmt.rate/12.0/100.0, the_pmt.nper, the_pmt.pv)
    rets['payment'] = payment
    return rets

@app.get("/isprime/{item_id}")
def the_isprime(item_id: int, q: Union[str, None] = None):
    '''
    if item_id is 33865, check the prime number from parameter
    '''
    ans = None
    if item_id == 33865:
        try:
            v = int(q)
            ans = "prime" if is_prime(v) else "composite"
        except ValueError:
            ans = "NAN"
    else:
        ans = "ok"

    return {"item_id": item_id, "q": q, "ans": ans}


if __name__ == "__main__":
    prt(f"try this: fastapi dev {sys.argv[0]}")
    prt("and the browser: http://localhost:8000/docs")
