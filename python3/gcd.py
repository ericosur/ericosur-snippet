#!/usr/bin/env python3
# -*- coding: utf-8 -*-


''' provide a recursive version of gcd '''

import sys

__version__ = '1.0.0'

def gcd(m, n):
    '''
    calculate gcd number by rescursive
    '''
    if n == 0:
        return m
    return gcd(n, m % n)

def read_from_stdin():
    ''' read from stdin '''
    args = []
    for line in sys.stdin:
        l = line.strip()
        vs = l.split(' ')
        args.extend(vs)
        #args.append(line.strip())
    main(args)

def main(argv):
    ''' main function '''
    vals = []
    if argv == []:  # no arguments
        print('demo values ====>')
        vals = [1280, 1024]
    else:
        try:
            for a in argv:
                vals.append(int(a))
        except ValueError:
            print("not a numeric value")
            sys.exit()
        except:
            print("unexpected error:", sys.exc_info()[0])
            raise

    if len(vals) == 2:
        # pylint: disable=unbalanced-tuple-unpacking
        [a, b] = vals
    else:
        print('something wrong: ', vals)
    if a == 0 or b == 0:
        print("cannot be zero")
        sys.exit(-1)

    gcd_num = gcd(a, b)
    print("gcd(%d, %d) = %d" % (a, b, gcd_num))
    print("(%d : %d) = (%d : %d)" % (a, b, a/gcd_num, b/gcd_num))


if __name__ == '__main__':
    if len(sys.argv) == 1:  # no arguments
        print("MUST input two number by argument")
        main([])
    if len(sys.argv) == 2:  # not enough arguments?
        if sys.argv[1] == '-' or sys.argv[1] == '--':
            read_from_stdin()
            sys.exit(0)
        else:
            print("NOT enough arguments, need 2, given 1")
            sys.exit(-2)
    if len(sys.argv) == 3:
        main(sys.argv[1:])
