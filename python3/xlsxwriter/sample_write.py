#!/usr/bin/env python3
# coding: utf-8

'''
# A simple example of some of the features of the XlsxWriter Python module.
#
# Copyright 2013-2016, John McNamara, jmcnamara@cpan.org
#
# https://xlsxwriter.readthedocs.io/example_demo.html#ex-demo
'''

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
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    worksheet.write('A1', 'Hello')

    # Text with formatting.
    worksheet.write('A2', 'World', bold)

    # Write some numbers, with row/column notation.
    worksheet.write(2, 0, 123)      # A3
    worksheet.write(3, 0, 123.456)  # A4

    # Insert an image.
    worksheet.insert_image('A5', 'logo.jpg')

    workbook.close()

    print('output to', DEMO_XLSX)

if __name__ == '__main__':
    main()
