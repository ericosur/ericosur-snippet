#!/usr/bin/python3
# coding: utf-8

''' get new cost and avg '''

import sys
from myutil import require_python_version

def main(argv: list) -> None:
    ''' main '''
    mm = []
    if argv == []:
        mm = [27.41, 29209, 24.49, 1000]

    print(mm)
    for aa in argv:
        mm.append(float(aa))
    if len(mm) == 3:
        mm.append(1000)

    nstock = mm[1] + mm[3]
    total = mm[0] * mm[1] + mm[2] * mm[3]
    old_avg = mm[0]
    avg = total / nstock

    def printOut() -> None:
        ''' print out '''
        if require_python_version(3, 6):
            print(f'total: {total:.2f}')
            print(f'nstock:{mm[1]:.0f} -> {nstock:.0f}, avg: {old_avg:.2f} -> {avg:.2f}')
        else:
            print(f'total: {total:.2f}'.format(total))
            print(f'nstock:{mm[1]:.0f} -> {nstock:.0f}, avg: {old_avg:.2f} -> {avg:.2f}')

    printOut()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        main([])
    elif 3 < len(sys.argv) <= 5:
        main(sys.argv[1:])
    else:
        print('old price, old stocks, new price, add stocks')
