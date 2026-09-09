#!/usr/bin/env python3

''' run test3 from run_gcd '''

from run_gcd import test3


def main():
    ''' main function '''
    print("Running test3...")
    r = test3()
    print(f"Result length: {len(r)}")
    print("type:", type(r))

if __name__ == "__main__":
    main()
