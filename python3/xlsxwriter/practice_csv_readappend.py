#!/usr/bin/env python3

'''
A simple CSV practice by using python module csv
'''

import csv
import random


def get_ten_numbers():
    ''' get_ten_numbers '''
    TEN = 10
    arr = [random.randint(0, 99) for _ in range(TEN)]
    return arr

def write_csv(csvfn):
    ''' write csv '''
    with open(csvfn, 'wt', encoding='utf8') as csvfile:
        sw = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        for _ in range(1, 10):
            sw.writerow(get_ten_numbers())
    csvfile.close()

def append_csv(ifn, ofn):
    ''' append_csv '''
    with open(ifn, 'rt', encoding='utf8') as csvin, open(ofn, 'wt', encoding='utf8') as csvout:
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


def main():
    ''' main '''
    RANDOM_CSV = 'random.csv'
    OUTCOME_CSV = 'outcome.csv'
    print('generate random numbers and output to ' + RANDOM_CSV)
    write_csv(RANDOM_CSV)
    print('read' + RANDOM_CSV + ' sum up and output to ' + OUTCOME_CSV)
    append_csv(RANDOM_CSV, OUTCOME_CSV)

if __name__ == '__main__':
    main()
