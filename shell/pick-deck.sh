#!/bin/bash
# pick-card.sh

# from: https://www.ing.iac.es/~docs/external/bash/abs-guide/randomvar.html
# This is an example of choosing a random element of an array.


# Pick a card, any card.

Suites="Clubs
Diamonds
Hearts
Spades"

Denominations="2
3
4
5
6
7
8
9
10
Jack
Queen
King
Ace"

suite=($Suites)                # Read into array variable.
denomination=($Denominations)

num_suites=${#suite[*]}        # Count how many elements.
num_denominations=${#denomination[*]}

echo -n "${denomination[$((RANDOM%num_denominations))]} of "
echo ${suite[$((RANDOM%num_suites))]}


# $bozo sh pick-cards.sh
# Jack of Clubs


# Thank you, "jipe," for pointing out this use of $RANDOM.
exit 0
