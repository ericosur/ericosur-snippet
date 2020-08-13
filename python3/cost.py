#!/usr/bin/python3
# coding: utf-8

''' get new cost and avg '''

import sys
from myutil import get_python_version

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

    def printOut():
        ''' print out '''
        ver = float(get_python_version())
        if ver >= 3.6:
            print('total: {total:.2f}')
            print('nstock:{mm[1]:.0f} -> {nstock:.0f}, avg: {old_avg:.2f} -> {avg:.2f}')
        else:
            print('total: {:.2f}'.format(total))
            print('nstock:{:.0f} -> {:.0f}, avg: {:.2f} -> {:.2f}'.format(mm[1], nstock, old_avg, avg))

    printOut()

if __name__ == '__main__':
    print('old price, old stocks, new price, add stocks')
    if len(sys.argv) <= 1:
        main([])
    elif 3 < len(sys.argv) <= 4:
        main(sys.argv[1:])
