#!/usr/bin/python
# -*- coding: utf-8 -*-

# use shuffle_array() in fisher_yates_shuffle.py
#from fisher_yates_shuffle import shuffle_array

import random

'''
Var 'card' stands for a card, which is a list contains
[suit, point]. 'Suit' means 'heart', 'spade', 'club' and 'diamond'.
'Point' is in the range of 1 to 13.

Simply init a pile of cards by order and deal 5 cards to 4 players.
'''


def init_deck(foo):
    card = []
    for suit in xrange(1,5):         # 1..4
        for point in xrange(1,14):   # 1..13
            card = [point, suit]
            foo.append(card)


def show_deck(foo):
    cnt = 0
    for cc in foo:
        if cnt!=0 and cnt%13==0:
            print
            cnt = 0
        #dir(cc)
        print show_one_card(cc),' ',
        cnt += 1


def show_one_card(card):
    '''
    'x': joker, 'S': spade, 'H': heart, 'D': diamond, 'C': club
    '''
    #print 'card', card[0]
    #st = ['x','H','C','D','S']
    st = ['x','♥','♣','♦','♠']

    if card[0] == 1:
        pt = 'A'
    elif card[0] == 11:
        pt = 'J'
    elif card[0] == 12:
        pt = 'Q'
    elif card[0] == 13:
        pt = 'K'
    else:
        pt = str(card[0])

    return pt + st[card[1]]


def faro_shuffle(cards):
    '''Shuffles the deck using a perfect faro shuffle.'''
    r = []
    for (a, b) in zip(cards[0:26], cards[26:]):
        r.append(a)
        r.append(b)
    return r


def fisher_yates_shuffle(cards):
    n = len(cards)
    r = cards
    while (n > 1):
        k = random.randint(0, n-1)
        n = n - 1
        r[n], r[k] = r[k], r[n]
    return r

'''
def deal_cards(pile, num):
    deal_cards = []
    for i in xrange(num):
        deal_cards.append(pile.pop())
    return deal_cards
'''


'''
print '-------------------'
#shuffle_array(mycards)
show_deck(mycards)
print '-------------------'
'''
def demo_faro_shuffle():
    print "demo for faro shuffle after 8 times:"
    mycards = []
    init_deck(mycards)
    show_deck(mycards)
    print '-------------------'
    for i in range(0,8):
        mycards = faro_shuffle(mycards)
    # you will see the same order
    show_deck(mycards)


def demo_fisher_shuffle():
    print "demo for fisher yates shuffle:"
    mycards = []
    init_deck(mycards)
    show_deck(mycards)
    print '-------------------'
    mycards = fisher_yates_shuffle(mycards)
    show_deck(mycards)


def demo_deal_cards():
    print "demo for dealing cards to 4 players:"
    mycards = []
    init_deck(mycards)
    #show_deck(mycards)
    print
    players = [[],[],[],[]]
    for pp in xrange(5):    # deal 5 cards
        one = []
        for cc in xrange(4):    # here are 4 players
            #print 'cc',cc
            players[cc].append( mycards.pop() ) # pop from tail

    for pp in players:
        show_deck(pp)
        print


if __name__ == '__main__':
    demo_faro_shuffle()
    print "--------------------"
    demo_fisher_shuffle()
    print "--------------------"
    demo_deal_cards()