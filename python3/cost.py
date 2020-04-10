#!/usr/bin/python3
# coding: utf-8

''' get new cost and avg '''

import sys

def main(argv):
    ''' main '''
    mm = list()
    if argv == []:
        mm = [27.41, 29209, 24.49, 1000]

    for aa in argv:
        mm.append(float(aa))
    if len(mm) == 3:
        mm.append(1000)

    nstock = mm[1] + mm[3]
    total = mm[0] * mm[1] + mm[2] * mm[3]
    old_avg = mm[0]
    avg = total / nstock
    print('total: {:.2f}'.format(total))
    print('nstock:{:.0f} -> {:.0f}, avg: {:.2f} -> {:.2f}'.format(mm[1], nstock, old_avg, avg))


if __name__ == '__main__':
    print('old price, old stocks, new price, add stocks')
    if len(sys.argv) < 1:
        main([])
    elif 3 < len(sys.argv) <= 4:
        main(sys.argv[1:])
