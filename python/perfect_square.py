#!/usr/bin/env python
#

import csv

OUTPUT_CSV = 'perfect_s.csv'

with open(OUTPUT_CSV, 'wb') as csvfile:
    fieldnames = ['index', 'n', 'value']
    sw = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',',
                    quotechar='"', quoting=csv.QUOTE_ALL)
    sw.writeheader()
    lower = 31
    upper = 99
    cnt = 0
    for n in xrange(lower, upper):
        cnt = cnt + 1
        sw.writerow({'index': cnt, 'n':n, 'value':n*n})

