#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
use shuffle_array() in fisher_yates_shuffle.py
from fisher_yates_shuffle import shuffle_array
'''

import random

from deckutil import init_deck, print_sep, show_deck

'''
Var 'card' stands for a card, which is a list contains
[suit, point]. 'Suit' means 'heart', 'spade', 'club' and 'diamond'.
'Point' is in the range of 1 to 13.

Simply init a pile of cards by order and deal 5 cards to 4 players.
'''


def faro_shuffle(cards):
    '''Shuffles the deck using a perfect faro shuffle.'''
    r = []
    for (a, b) in zip(cards[0:26], cards[26:]):
        r.append(a)
        r.append(b)
    return r


def fisher_yates_shuffle(cards):
    ''' fisher yates shuffle '''
    n = len(cards)
    r = cards
    while n > 1:
        k = random.randint(0, n-1)
        n = n - 1
        r[n], r[k] = r[k], r[n]
    return r


def demo_faro_shuffle():
    ''' demo faro shuffle '''
    print("demo for faro shuffle after 8 times:")
    mycards = []
    init_deck(mycards)
    show_deck(mycards)
    print_sep()
    for _ in range(0, 8):
        mycards = faro_shuffle(mycards)
    print('you will see the same cards order')
    show_deck(mycards)


def demo_fisher_shuffle():
    ''' demo fisher shuffle '''
    print("demo for fisher yates shuffle:")
    mycards = []
    init_deck(mycards)
    show_deck(mycards)
    print_sep()
    mycards = fisher_yates_shuffle(mycards)
    show_deck(mycards)


def demo_deal_cards():
    ''' demo deal cards '''
    print("demo for dealing cards to 4 players:")
    mycards = []
    init_deck(mycards)
    #show_deck(mycards)
    print()
    players = [[], [], [], []]
    for pp in range(5):    # deal 5 cards
        for cc in range(4):    # here are 4 players
            #print 'cc',cc
            players[cc].append(mycards.pop()) # pop from tail

    for pp in players:
        show_deck(pp)


if __name__ == '__main__':
    demo_faro_shuffle()
    print_sep()
    demo_fisher_shuffle()
    print_sep()
    demo_deal_cards()
