#!/usr/bin/env python
# coding: utf-8

'''
http://projecteuler.net/problem=14
'''

import pickle

class SnowBall():
    ''' class to calculate snow ball numbers '''
    def __init__(self):
        self.cnt = 0
        self.not_included_cnt = 0
        self.snow_dict = {1:[1], 2:[2, 1]}
        self.snow = {}

    def snow_number_seq(self, n):
        '''
        original method to calculate snow number by loop
        '''
        seq = []
        while n > 1:
            self.cnt += 1
            if n & 1:   # n is odd
                n = 3 * n + 1
            else:
                n = n / 2
            seq.append(n)
        return seq

    def snowball(self, n):
        '''
        recursive method to calculate snow number, and
        it will save the calculated sequence
        '''

        self.cnt += 1
        if self.cnt > 1e4:
            print("to many recursive and stop...")
            return

        if n != 1 and n in self.snow_dict:
            self.snow.extend(self.snow_dict[n])
            return

        self.snow.append(n)

        if not n in self.snow_dict:
            self.not_included_cnt += 1

        if n <= 1:
            return

        if n % 2: # n is odd
            #print 'o',
            self.snowball(3 * n + 1)
        else:
            #print 'o',
            self.snowball(n / 2)


    def action(self):
        ''' action '''
        data_file = 'snowball.p'
        storage = True  # save into pickle file or not

        # it takes long time if upperlimit is large
        upperlimit = 1000000
        i = upperlimit // 2

        print('upperlimit:', upperlimit)

        if storage:
            try:
                with open(data_file, 'rb') as inf:
                    self.snow_dict = pickle.load(inf)
            except IOError:
                print('data file not opened, init snow_dict')

        print('size of snow_dict:', len(self.snow_dict))
        maxlen = 0
        maxidx = 0
        i = 0
        while i < upperlimit:
            i += 1
            self.snow = []
            self.cnt = 0
            self.snowball(i)
            if len(self.snow) > maxlen:
                maxlen = len(self.snow)
                maxidx = i

            #print i,'cnt', cnt,'len', len(snow) #,'snow', snow
            if i not in self.snow_dict:
                self.snow_dict[i] = self.snow

        #print 'snow_dict key', snow_dict.keys()
        print('not_included_cnt', self.not_included_cnt)
        print('max len is', maxlen, 'max idx: ', maxidx)

        # store into pickle file
        if storage:
            with open(data_file, 'wb') as ouf:
                pickle.dump(self.snow_dict, ouf)


def main():
    ''' main '''
    snowb = SnowBall()
    snowb.action()

if __name__ == '__main__':
    main()
