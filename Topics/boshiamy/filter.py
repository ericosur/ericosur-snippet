#!/usr/bin/python3
# coding: utf-8

'''
read liu.json
3400..4DBF; CJK Unified Ideographs Extension A

'''

import json
from unicode_blocks import UnicodeBlock

def check_cjk_b(items):
    ''' check '''
    cnt = 0
    c = 0
    for i in range(0x20000, 0x2a6df + 1):
        cnt += 1
        s = str(i)
        if s in items:
            c += 1
        else:
            print('missing: {:06x}'.format(i))
    print('cnt:', cnt)
    print('c:', c)

def main():
    ''' main '''
    fn = 'liu.json'
    data = json.load(open(fn))
    ub = UnicodeBlock()
    cjk_blocks = ub.get_cjkblocks()
    subset = dict()
    cnt = 0
    for k in data.keys():
        try:
            cp = int(k)
            cnt += 1
            for start, end, name in cjk_blocks:
                if not name in subset:
                    subset[name] = list()
                if start <= cp <= end:
                    subset[name].append(k)
        except TypeError:
            print("err: {} at {}".format(e, k))
        except ValueError as e:
            print("err: {} at {}".format(e, k))

    print('processed cnt:', cnt)
    print('len of subset: {}'.format(len(subset)))
    for category in sorted(subset.keys()):
        print('category {}: {}'.format(category, len(subset[category])))
    # ofn = 'cjks.json'
    # with open(ofn, 'wt') as of:
    #     of.write(json.dumps(subset, indent=2, sort_keys=True))

    print('len of cjk_b:', len(subset['CJK Unified Ideographs Extension B']))
    check_cjk_b(subset['CJK Unified Ideographs Extension B'])

if __name__ == '__main__':
    main()
