#!/usr/bin/env python3

'''
Test for method_bisect function
'''

import bisect


def method_bisect_buggy(a, b, c):
    ''' bisect in - original buggy version '''
    b.sort()
    for i, x in enumerate(a):
        index = bisect.bisect_left(b, x)
        if index < len(a) and x == b[index]:  # BUG: should be len(b)
            c[i] = 1

def method_bisect_fixed(a, b, c):
    ''' bisect in - fixed version '''
    b.sort()
    for i, x in enumerate(a):
        index = bisect.bisect_left(b, x)
        if index < len(b) and x == b[index]:  # FIXED: check len(b)
            c[i] = 1

def test_method_bisect():
    '''Test the bisect method'''
    # Test case 1: simple case where a is smaller than b
    a = [1, 3, 5]
    b = [1, 2, 3, 4, 5, 6]
    c_buggy = [0] * len(a)
    c_fixed = [0] * len(a)
    
    print("Test 1: a=[1,3,5], b=[1,2,3,4,5,6]")
    print("Expected c=[1,1,1] (all values exist in b)")
    
    try:
        method_bisect_buggy(a, b.copy(), c_buggy)
        print(f"Buggy result: {c_buggy}")
    except IndexError as e:
        print(f"Buggy version crashed: IndexError - {e}")
    
    method_bisect_fixed(a, b.copy(), c_fixed)
    print(f"Fixed result: {c_fixed} ✓")
    
    # Test case 2: when len(a) != len(b)
    print("\nTest 2: a=[10,20,30,40,50], b=[5,15,25]")
    a = [10, 20, 30, 40, 50]
    b = [5, 15, 25]
    c_buggy = [0] * len(a)
    c_fixed = [0] * len(a)
    
    print("Expected c=[0,0,0,0,0] (no values from a exist in b)")
    
    try:
        method_bisect_buggy(a, b.copy(), c_buggy)
        print(f"Buggy result: {c_buggy}")
    except IndexError as e:
        print(f"Buggy version crashed: IndexError - {e}")
    
    method_bisect_fixed(a, b.copy(), c_fixed)
    print(f"Fixed result: {c_fixed} ✓")
    
    # Test case 3: normal case where len(a) == len(b)
    print("\nTest 3: a=[1,2,3], b=[2,3,4]")
    a = [1, 2, 3]
    b = [2, 3, 4]
    c_buggy = [0] * len(a)
    c_fixed = [0] * len(a)
    
    print("Expected c=[0,1,1]")
    
    method_bisect_buggy(a, b.copy(), c_buggy)
    print(f"Buggy result: {c_buggy}")
    
    method_bisect_fixed(a, b.copy(), c_fixed)
    print(f"Fixed result: {c_fixed} ✓")

if __name__ == '__main__':
    test_method_bisect()
