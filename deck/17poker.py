#!/usr/bin/python

# use shuffle_array() in fisher_yates_shuffle.py
from fisher_yates_shuffle import shuffle_array

'''
Var 'card' stands for a card, which is a list contains
[suit, point]. 'Suit' means 'heart', 'spade', 'club' and 'diamond'.
'Point' is in the range of 1 to 13.

Simply init a pile of cards by order and deal 5 cards to 4 players.
'''


def init_deck(foo):
	card = []
	for suit in xrange(1,5):
		for point in xrange(1,14):
			card = [suit, point]
			foo.append(card)

def show_deck(foo):
	for cc in foo:
		dir(cc)
		print show_one_card(cc),

def show_one_card(card):
	'''
	'x': joker, 'S': spade, 'H': heart, 'D': diamond, 'C': club
	'''
	#print 'card', card[0]
	suit = ['x','S','H','D','C']
	return '(' + suit[card[0]] + str(card[1]) + ')'

'''
def deal_cards(pile, num):
	deal_cards = []
	for i in xrange(num):
		deal_cards.append(pile.pop())
	return deal_cards
'''

mycards = []
init_deck(mycards)
#show_deck(mycards)

# show total cards
'''
print '-------------------'
#shuffle_array(mycards)
show_deck(mycards)
print '-------------------'
'''

players = [[],[],[],[]]
for pp in xrange(5):	# deal 5 cards
	one = []
	for cc in xrange(4):	# here are 4 players
		#print 'cc',cc
		players[cc].append( mycards.pop() )

for pp in players:
	show_deck(pp)
	print

