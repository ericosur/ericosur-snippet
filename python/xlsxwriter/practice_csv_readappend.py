#!/usr/bin/env python

'''
A simple CSV practice by using python module csv
'''

import csv
import random

RANDOM_CSV = 'random.csv'
OUTCOME_CSV = 'outcome.csv'

def getTenNumbers():
    ten = 10
    arr = []
    for i in xrange(ten):
        arr.append(random.randint(0, 99))
    return arr

def writeCsv(csvfn):
    with open(csvfn, 'wb') as csvfile:
        sw = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        for i in xrange(1,10):
           sw.writerow(getTenNumbers())
    csvfile.close()

def appendCsv(input_fn, output_fn):
    with open(input_fn, 'rb') as csvin, open(output_fn, 'wb') as csvout:
        cin = csv.reader(csvin, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        cout = csv.writer(csvout, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        for row in cin:
            mysum = 0
            for rr in row:
                mysum = mysum + int(rr)
            row.append(mysum)
            cout.writerow(row)

    csvin.close()
    csvout.close()


if __name__ == "__main__":
    print 'generate random numbers and output to', RANDOM_CSV
    writeCsv(RANDOM_CSV)
    print 'read', RANDOM_CSV, 'sum up and output to', OUTCOME_CSV
    appendCsv(RANDOM_CSV, OUTCOME_CSV)
