#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Var 'card' stands for a card, which is a list contains
[suit, point]. 'Suit' means 'heart', 'spade', 'club' and 'diamond'.
'Point' is in the range of 1 to 13.

Simply init a pile of cards by order and deal 5 cards to 4 players.
'''

from deckutil import init_deck, show_deck
from fisher_yates_shuffle import shuffle_array


def main():
    ''' main '''
    perform_shuffle = True
    mycards = []
    init_deck(mycards)
    show_deck(mycards)

    # show total cards
    '''
    print '-------------------'
    #shuffle_array(mycards)
    show_deck(mycards)
    print '-------------------'
    '''
    if perform_shuffle:
        shuffle_array(mycards)
    else:
        print('WARNING: no shuffled')

    players = [[], [], [], []]
    for _ in range(5):    # deal 5 cards
        for pp in players:    # here are 4 players
            #print 'cc',cc
            pp.append(mycards.pop())

    for pp in players:
        show_deck(pp)
    #print()

if __name__ == '__main__':
    main()
