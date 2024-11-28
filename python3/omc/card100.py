#!/usr/bin/env python3

'''
card 100
not 3's multiple, nor not 7's multiple
'''

def main():
    ''' main '''
    cards = list(range(1, 101))
    t3 = []
    for c in cards:
        if c % 3 == 0:
            continue
        t3.append(c)
    t7 = []
    for c in t3:
        if c % 7 == 0:
            continue
        t7.append(c)
    print(t7)


if __name__ == '__main__':
    main()
