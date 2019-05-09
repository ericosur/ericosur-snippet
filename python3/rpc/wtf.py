#!/usr/bin/env python3
# coding: utf-8
#


import statistics


def main():
    arr = []
    fn = 'data.txt'
    try:
        with open(fn, 'rt') as ifile:
            for ln in ifile:
                val = float(ln.strip())
                arr.append(val)
    except IOError:
        print('IOError')
        return

    print('there are {} elements'.format(len(arr)))
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    stdev = statistics.stdev(arr)
    print('mean: {:.3f}\nmedian: {:.3f}\nstdev: {:.3f}\n'.format(mean, median, stdev))


if __name__ == '__main__':
    main()
