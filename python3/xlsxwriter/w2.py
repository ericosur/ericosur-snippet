#!/usr/bin/env python3
# coding: utf-8

'''
practice
'''

import itertools as it
import sys
try:
    import xlsxwriter
except ImportError:
    print('cannot import module xlsxriter')
    sys.exit(1)

def main():
    ''' main '''
    DEMO_XLSX = 'demo.xlsx'

    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(DEMO_XLSX)
    sheet1 = workbook.add_worksheet("hello")

    for (r, c) in it.product(list(range(25)), list(range(5))):
    #for r in range(25):
        #for c in range(5):
        sheet1.write(r, c, r+2*c)

    for r in range(1, 25):
        beg = 'A' + str(r)
        end = 'E' + str(r)
        formula = "=sum(" + beg + ':' + end + ")"
        res = 'F' + str(r)
        sheet1.write(res, formula)

    sheet2 = workbook.add_worksheet("world")
    sheet2.write('A1', 'sheet2')

    workbook.close()

if __name__ == '__main__':
    main()
