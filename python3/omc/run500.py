#!/usr/bin/python3
# coding: utf-8

'''
500 meter runway
A 60 m/m
B 50 m/m
every 200m take rest 1 min
'''

import math

class Run500():

    ROUND_LIMIT = 500.0
    REST_LIMIT = 200.0

    def __init__(self):
        self.a = {'name': 'A', 'pos': 0, 'accu': 0,
            'rest': 0, 'inc': 60.0, 'stop': 0}
        self.b = {'name': 'B', 'pos': 0, 'accu': 0,
            'rest': 0, 'inc': 50.0, 'stop': 0}
        self.verbose = True
        self.a_first = False
        self.b_first = False
        self.t = 0

    def take_a_rest(self, player):
        p = player
        if self.verbose:
            if p['name'] == 'A':
                opp = self.b
            else:
                opp = self.a
        print(f"{self.t}: {p['name']} take a rest at pos:{p['pos']:.3f} ({opp['name']}: {opp['pos']:.3f})")
        p['rest'] += 1
        p['stop'] = 2
        p['accu'] = 0

    def check_rest(self, player):
        p = player
        accu = p['accu']
        if abs(accu - self.REST_LIMIT) < 0.00001:
            self.take_a_rest(player)
            return True
        return False


    def update_pos(self, player):
        p = player
        tmp_pos = p['pos']
        forward_length = p['inc'] / 3.0
        tmp_pos += forward_length

        # move forward and reach rest point
        if tmp_pos >= self.ROUND_LIMIT:
            if self.verbose:
                print(f"{self.t}: {p['name']} runs accross the start point")
            tmp_pos -= self.ROUND_LIMIT
        p['pos'] = tmp_pos
        p['accu'] += forward_length


    def update(self, player):
        p = player
        tmp_pos = p['pos']
        if p['stop'] > 0:
            #print(f"{self.t}: {p['name']} pass {p['stop']} at {tmp_pos:.3f}...")
            p['stop'] -= 1
            return

        self.update_pos(player)
        self.check_rest(player)

    def show_dist(self):
        a = self.a['pos']
        aa = self.a['accu']
        ap = self.a['stop']
        b = self.b['pos']
        bb = self.b['accu']
        bp = self.b['stop']
        if a > b:
            self.a_first = True
        if b > a:
            self.b_first = True
        if abs(a - b) < 9.0:
            print(f"{self.t}= {a:.3f}/{aa:.3f} vs {b:.3f}/{bb:.3f}")
        elif ap > 0 or bp > 0:
            print(f"{self.t}: {a:.3f}/{aa:.3f} vs {b:.3f}/{bb:.3f}")
        else:
            print(f"{self.t}: {a:.3f}/{aa:.3f} vs {b:.3f}/{bb:.3f}")

    def run(self):
        for i in range(299):
            self.t += 1
            self.update(self.a)
            self.update(self.b)
            self.show_dist()

def main():
    run500 = Run500()
    run500.run()

if __name__ == '__main__':
    main()
