#coding:utf-8

'''
bopo list
'''

from functools import cmp_to_key
import re
import sys
from random import randint
from typing import List
from idiom_list import BOPOMOFO_LIST, BOPOMOFO_TONE, IDIOM_BOPOMOFO
# from rich.console import Console
# console = Console()
# logd = console.log
from loguru import logger
logd = logger.debug

LIST_START = 50
TONE_START = 1
BP_DEFAULT = 999


class BopoIndex():
    ''' bopo index '''
    def __init__(self):
        self.bopo = BOPOMOFO_LIST.copy()
        self.tone = BOPOMOFO_TONE.copy()

    def lookup_list(self, c: str, the_default: int=TONE_START) -> int:
        '''
        look up in the list,
        return default is not found
        tone would be 10,20,30,40
        ㄅ will start from 50 (LIST_START)
        '''
        if c in self.bopo:
            i = self.bopo.index(c) + LIST_START
            return i
        if c in self.tone:
            i = (self.tone.index(c))
            return i
        return the_default

    @staticmethod
    def ensure_len4(n: List) -> List:
        ''' if len(n) < 4, fill BP_DEFAULT till len==4 '''
        # check input first
        if not isinstance(n, list):
            raise TypeError("input of ensure_len4 is not a list")
        if len(n) == 0:
            raise ValueError("length of input list is 0, check the input")
        tmp = n.copy()
        if len(tmp) == 0:
            logd(f'wtf??? {n=} {tmp=}')
            raise ValueError("wtf len of input is zero?")
        while len(tmp) < 4:
            try:
                tail = tmp[-1]
                #logd(f"{tail=}")
                if 0<tail<10 or tail==BP_DEFAULT:
                    tmp.append(BP_DEFAULT)
                else:
                    tmp.append(TONE_START)
            except IndexError as e:
                logd(f'ensure_len4: {tmp=}, {e}')
                sys.exit(1)
        return tmp

    def get_value_of_word(self, w: str) -> List[List]:
        '''
        given bopomofo ㄅㄨˋ ㄒㄩㄝˊ ㄨ ㄕㄨˋ
        '''
        total = []
        inner = []
        for c in list(w):
            if c == ' ':
                if len(inner) == 0:
                    logd(f'why? the len is zero: {w=}')
                total.append(self.ensure_len4(inner))
                inner = []
                continue
            r = self.lookup_list(c)
            inner.append(r)
        if inner:
            r = self.ensure_len4(inner)
            total.append(r)

        #logd(f'{total=}')
        return total

    def get_bopo_narray_from_idiom(self, w: str) -> List[List]:
        '''
        given ㄅㄨˋ ㄒㄩㄝˊ ㄨ ㄕㄨˋ
        get a list of list
        '''
        t = []
        r = self.get_value_of_word(w)
        t.extend(r)
        #logd(f'add_word: {t}')
        return t

def cast_to_list(x) -> List:
    ''' cast to a list '''
    t = list(x)
    return t

def cmp_idiom(x: List, y: List) -> int:
    ''' cmp for list of list '''
    #logd(f'cmp_idiom: {x=}\n{y=}')
    m = cast_to_list(x[1]).copy()
    n = cast_to_list(y[1]).copy()
    if len(m) != len(n):
        raise IndexError(f"length is different: {x} vs {y}")
    r = 0
    while len(m) > 0:
        r = cmp_gt(m.pop(0), n.pop(0))
        if r != 0:
            break
    #logd(f"ret:{r}")
    return r

def dump_to_file(ans, fn):
    ''' dump ans '''
    logd(f'output to {fn}')
    with open(fn, "wt", encoding="utf-8") as fobj:
        for i in ans:
            print(f'"{i[0]}","{i[1]}"', file=fobj)

def translate_sorted_to_dict(the_sorted):
    ''' change the structure '''
    d = []
    for i in the_sorted:
        l = []
        m = re.match(r'([^,]+),([^\,]+)', i[0])
        if m:
            l.append(m[1])
            l.append(m[2])
        else:
            logd(f'not matched: {i[0]}')
        #l.append(i[1])
        #logd(f'local: {l=}')
        d.append(l)
    return d

def test():
    ''' test '''
    #gg = IDIOM_BOPOMOFO.copy()
    # gg.append(IDIOM_BOPOMOFO[179])
    # gg.append(IDIOM_BOPOMOFO[149])
    gg = []
    for i in IDIOM_BOPOMOFO:
        if len(i[0])==4:  # only 4-word idioms
            gg.append(list(i))

    bo = BopoIndex()
    idioms = {}
    for i in gg:
        k = i[0]+','+i[1]
        # v is List of List
        v = bo.get_bopo_narray_from_idiom(i[1])
        idioms[k] = v
    #logd(idioms)
    # after this step, the structure of ans is:
    # [(str,[elem of 4 lists]),(...)]
    # ref: {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    the_sorted = sorted(idioms.items(), key=cmp_to_key(cmp_idiom))
    ans = translate_sorted_to_dict(the_sorted)
    # the content will be similar to "idiom_bopo2.csv",
    # but sorted and grepped
    dump_to_file(ans, "bopo-output.csv")
    #logd('ans:', ans)

def is_tone(v: int) -> bool:
    ''' is tone '''
    return 0<v<9
def is_phone(v: int) -> bool:
    ''' is phoetic '''
    return 50 <= v < 90
def is_valid(v: int) -> bool:
    if is_tone(v) or is_phone(v) or v==BP_DEFAULT:
        return True
    raise ValueError(f"value {v} is out of range: 0<v<9; 50<=v<90; v==999")
def my_cmp(x: int, y: int) -> int:
    ''' my own cmp '''
    if x < y:
        return -1
    if x == y:
        return 0
    if x > y:
        return 1

def do_nothing(*args):
    pass

def cmp_gt(mm: List, nn: List) -> int:
    '''
    Like cmp(a, b) x<y ret -1, x==y ret 0 , x>y ret 1
    '''
    m = mm.copy()
    n = nn.copy()
    logd = do_nothing
    #logd(f'cmp_gt: {m} vs {n}')
    if len(m) != len(n):
        raise IndexError(f"length is different: {m} vs {n}")
    ret = False
    while len(m) > 0:
        x = m.pop(0)
        y = n.pop(0)
        #logd(f'{x=} vs {y=}')
        if isinstance(x, int) and isinstance(y, int):
            if is_valid(x) and is_valid(y):
                pass
            if is_tone(x):
                if is_tone(y):
                    logd("tone vs tone")
                    ret = my_cmp(x, y)
                elif is_phone(y):
                    logd("T vs P")
                    ret = -1
                elif y == BP_DEFAULT:
                    logd("T vs null")
                    ret = -1
                else:
                    logd("fatal error")
                    ret = None
                    sys.exit(1)
                break
            elif is_phone(x):
                if is_tone(y):
                    logd("Ph vs T")
                    ret = 1
                    break
                elif is_phone(y):
                    ret = my_cmp(x,y)
                    logd(f"Ph vs Ph, ret={ret}")
                    if ret != 0:
                        break
                elif y == BP_DEFAULT:
                    logd("Ph vs null")
                    ret = -1
                    break
            elif x == BP_DEFAULT:
                if is_tone(y) or is_phone(y):
                    logd("null vs T/P ")
                    ret = -1
                else:
                    ret = 0
                break
            else:
                logd("falal error")
                sys.exit(1)
        else:
            raise ValueError("element should be int")
        # will continue if not true
    logd(f'cmp_gt {mm} vs {nn} ret={ret}')
    return ret

def verify():
    ''' verify '''
    assert cmp_gt([1],[4])<0
    assert cmp_gt([2],[2])==0
    assert cmp_gt([3],[2])==0
    assert cmp_gt([3],[55])<0
    assert cmp_gt([3],[999])<0
    assert cmp_gt([76],[1])==0
    assert cmp_gt([76],[76])==0
    assert cmp_gt([76],[80])<0
    assert cmp_gt([999],[1])==0
    assert cmp_gt([999],[61])==0
    assert cmp_gt([999],[999])==0
    # https://rich.readthedocs.io/en/stable/appendix/colors.html
    logd("[bright_red]verify pass")

def verify_except():
    ''' verify except '''
    try:
        assert cmp_gt([35], [4])==False
    except ValueError as e:
        logd("exception caught:", e)
    try:
        assert cmp_gt([4], [10])==True
    except ValueError as e:
        logd("exception caught:", e)
    try:
        assert cmp_gt([], [10])==True
    except IndexError as e:
        logd("exception caught:", e)
    logd("[bright_red]verify pass")

if __name__ == "__main__":
    #verify()
    #verify_except()
    test()
