#!/usr/bin/env python3
## coding: utf-8

'''
dump snow dict
'''

import pickle

def main():
    ''' main '''
    #cond = False
    data_file = 'snowball.p'
    snow_dict = {}
    #cnt = 0
    #miss_list = []

    try:
        with open(data_file, 'rb') as inf:
            snow_dict = pickle.load(inf)
    except IOError:
        print("cannot load", data_file)
        return

    print('beg: len', len(snow_dict))
    #print(snow_dict.keys())

    # for kk in snow_dict.keys():
    #     for vv in snow_dict[kk]:
    #         cnt += 1
    #         if vv not in snow_dict:
    #             snow_dict[vv] = snow_dict[kk][snow_dict[kk].index(vv):]
    #print('cnt', cnt)

    print('end: len', len(snow_dict))
    result = list(snow_dict.keys())
    result.sort()
    for kk in result:
        for vv in snow_dict[kk]:
            if vv not in snow_dict:
                print(vv)

    # store into pickle file
    # with open(data_file, 'wb') as ouf:
    #     pickle.dump(snow_dict, ouf)


if __name__ == '__main__':
    main()
