#!/usr/bin/env python

import xlsxwriter

DEMO_XLSX = 'demo.xlsx'

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook(DEMO_XLSX)
sheet1 = workbook.add_worksheet("hello")
sheet2 = workbook.add_worksheet("world")

for r in range(25):
    for c in range(5):
        sheet1.write(r, c, r+2*c)

for r in xrange(1,25):
    beg = 'A' + str(r)
    end = 'E' + str(r)
    formula = "=sum(" + beg + ':' + end + ")"
    res = 'F' + str(r)
    sheet1.write(res, formula)

workbook.close()
