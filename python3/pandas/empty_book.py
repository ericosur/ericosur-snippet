#!/usr/bin/python3
# coding: utf-8

''' xlsx practice '''

import sys
try:
    from openpyxl import Workbook
    #from openpyxl.utils import get_column_letter
except ImportError:
    print('cannot import openpyxl, quit...')
    sys.exit(1)

def main():
    ''' main '''
    wb = Workbook()
    fn = 'empty_book.xlsx'
    ws1 = wb.active
    ws1.title = "multiple"
    for row in range(1, 20):
        for col in range(1, 20):
            v = row * col
            ws1.cell(column=col, row=row, value=v)

    # ws2 = wb.create_sheet(title='Pi')
    # ws2['F5'] = 3.141592653589793238462643383279502884

    # ws3 = wb.create_sheet(title='Data')
    # for row in range(10, 20):
    #     for col in range(27, 54):
    #         _ = ws3.cell(column=col, row=row, value='{}'.format(get_column_letter(col)))
    # print(ws3['AA10'].value)

    wb.save(filename=fn)

if __name__ == '__main__':
    main()
