#!/usr/bin/python3
# coding: utf-8

'''
check Readme.md
'''

from itertools import combinations

def output_list_to_file(output_file, cclist):
    ''' output list to file '''
    with  open(output_file, "w") as text_file:
        cnt = 0
        for cc in cclist:
            text_file.write(str(cc)+'\n')
            cnt = cnt + 1
    print("output to file {0}, total {1} items".format(output_file, cnt))


def output_list(result_list):
    ''' print list '''
    for ii in result_list:
        print(ii)

def perfrom_stupid_filter(cclist):
    ''' cclist is complete combination list '''
    allmiss = []
    onehit = []
    twohit = []
    answer = set(range(1, 13))
    cnt = 0
    for cc in cclist:
        cnt += 1
        union_set = set(cc) & answer
        if len(union_set) == 0:
            allmiss.append(cc)
        elif len(union_set) == 1:
            onehit.append(cc)
        elif len(union_set) == 2:
            twohit.append(cc)

    def show(msg, values):
        print(msg)
        MAX_LEN = 40
        print('value list length: {}'.format(len(values)))
        if len(values) > MAX_LEN:
            print('list too long to show... consider output to file...')
        else:
            output_list(values)

    print('>>> total combination checked: {}'.format(cnt))

    show('>>> allmiss', allmiss)
    show('>>> onehit', onehit)
    show('>>> twohit', twohit)


def main():
    ''' main '''
    #output_file = 'out.txt'
    # a = [1,2,3,...,22,23,24]
    a = range(1, 25)
    # ii = C(24, 12)
    ii = combinations(a, 12)
    #output_list_to_file(output_file, ii)
    perfrom_stupid_filter(ii)


if __name__ == '__main__':
    main()
