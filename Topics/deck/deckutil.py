#!/usr/bin/env python3
# coding: utf-8

'''
utility for showing deck
'''

def print_sep():
    ''' print sep '''
    print('-' * 40)


def init_deck(cards):
    ''' init deck '''
    card = []
    for suit in range(1, 5):
        for point in range(1, 14):
            card = [suit, point]
            cards.append(card)

def show_one_card(card):
    '''
    'x': joker, 'S': spade, 'H': heart, 'D': diamond, 'C': club
    '''
    #print 'card', card[0]
    #st = ['x','H','C','D','S']
    st = ['x', '♥', '♣', '♦', '♠']
    pt = card[1]
    if pt == 1:
        pt = 'A'
    elif pt == 11:
        pt = 'J'
    elif pt == 12:
        pt = 'Q'
    elif pt == 13:
        pt = 'K'
    pt = str(card[1])
    return st[card[0]] + ' ' + pt

def show_deck(cards):
    ''' show deck '''
    MAX_CARD_PER_LINE = 10
    for ii, cc in enumerate(cards):
        if ii and ii % MAX_CARD_PER_LINE == 0:
            print()
        print(show_one_card(cc), end=' ')
    print()
