#!/usr/bin/env python3

'''
Unit test for test_exist.py methods
Tests the three list membership checking methods: in, set, bisect
'''

import bisect
import random
import time


def method_in(a, b, c):
    ''' list in '''
    start_time = time.time()
    for i, x in enumerate(a):
        if x in b:
            c[i] = 1
    return time.time() - start_time

def method_set_in(a, b, c):
    ''' set in '''
    start_time = time.time()
    s = set(b)
    for i, x in enumerate(a):
        if x in s:
            c[i] = 1
    return time.time() - start_time

def method_bisect(a, b, c):
    ''' bisect in '''
    start_time = time.time()
    b.sort()
    for i, x in enumerate(a):
        index = bisect.bisect_left(b, x)
        if index < len(b) and x == b[index]:
            c[i] = 1
    return time.time() - start_time

def test_correctness():
    '''Test that all three methods produce the same correct results'''
    print("=" * 60)
    print("CORRECTNESS TESTS")
    print("=" * 60)
    
    test_cases = [
        {
            'name': 'All elements match',
            'a': [1, 2, 3, 4, 5],
            'b': [1, 2, 3, 4, 5],
            'expected': [1, 1, 1, 1, 1]
        },
        {
            'name': 'No elements match',
            'a': [1, 2, 3],
            'b': [10, 20, 30],
            'expected': [0, 0, 0]
        },
        {
            'name': 'Partial match',
            'a': [1, 2, 3, 4, 5],
            'b': [2, 4, 6],
            'expected': [0, 1, 0, 1, 0]
        },
        {
            'name': 'Duplicates in b',
            'a': [1, 2, 3],
            'b': [1, 1, 2, 2, 3, 3],
            'expected': [1, 1, 1]
        },
        {
            'name': 'Unordered lists',
            'a': [5, 1, 3],
            'b': [3, 2, 1],
            'expected': [0, 1, 1]
        },
    ]
    
    for test_case in test_cases:
        print(f"\nTest: {test_case['name']}")
        print(f"  a = {test_case['a']}")
        print(f"  b = {test_case['b']}")
        print(f"  Expected: {test_case['expected']}")
        
        # Test method_in
        c1 = [0] * len(test_case['a'])
        method_in(test_case['a'], test_case['b'].copy(), c1)
        print(f"  method_in:    {c1}", "✓" if c1 == test_case['expected'] else "✗ FAIL")
        
        # Test method_set_in
        c2 = [0] * len(test_case['a'])
        method_set_in(test_case['a'], test_case['b'].copy(), c2)
        print(f"  method_set:   {c2}", "✓" if c2 == test_case['expected'] else "✗ FAIL")
        
        # Test method_bisect
        c3 = [0] * len(test_case['a'])
        method_bisect(test_case['a'], test_case['b'].copy(), c3)
        print(f"  method_bisect:{c3}", "✓" if c3 == test_case['expected'] else "✗ FAIL")

def test_performance():
    '''Test performance of the three methods on larger lists'''
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTS (on N=5000)")
    print("=" * 60)
    
    N = 5000
    a = list(range(N))
    random.shuffle(a)
    b = list(range(N))
    random.shuffle(b)
    
    # Test method_in
    c1 = [0] * len(a)
    t1 = method_in(a, b.copy(), c1)
    print(f"method_in:     {t1:.4f} sec")
    
    # Test method_set_in
    c2 = [0] * len(a)
    t2 = method_set_in(a, b.copy(), c2)
    print(f"method_set:    {t2:.4f} sec")
    
    # Test method_bisect
    c3 = [0] * len(a)
    t3 = method_bisect(a, b.copy(), c3)
    print(f"method_bisect: {t3:.4f} sec")
    
    # Verify all methods got the same result
    if c1 == c2 == c3:
        print("\n✓ All methods produced identical results")
    else:
        print("\n✗ FAIL: Methods produced different results!")
    
    # Show speedup ratios
    print("\nSpeedup relative to method_in:")
    print(f"  set   / in = {t1/t2:.2f}x")
    print(f"  bisect/ in = {t1/t3:.2f}x")

if __name__ == '__main__':
    test_correctness()
    test_performance()
