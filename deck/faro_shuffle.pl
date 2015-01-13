#!/usr/bin/env perl
# File:  faro_shuffle.pl
# Usage:  perl faro_shuffle.pl
# Purpose:  To discover how many out-faro shuffles are required to
#           revert a deck of 52 cards back to its original order.
# http://en.wikipedia.org/wiki/Faro_shuffle

use strict;
use warnings;

# Given an input of 52 elements (cards), returns them
# as if they where shuffled with an out-faro shuffle:
sub faroShuffle
{
   # Verify that there are exactly 52 inputs:
   use Carp;
   croak "faroShuffle() requires 52 elements"  unless @_ == 52;

   return map { @_[$_, $_+26] } (0 .. 25);
}

# Define a deck in new-deck order that we will use for comparison:
my @originalDeck = qw(
   AH  2H  3H  4H  5H  6H  7H  8H  9H 10H  JH  QH  KH
   AC  2C  3C  4C  5C  6C  7C  8C  9C 10C  JC  QC  KC
   KD  QD  JD 10D  9D  8D  7D  6D  5D  4D  3D  2D  AD
   KS  QS  JS 10S  9S  8S  7S  6S  5S  4S  3S  2S  AS
);

# Create a deck that we will repeatedly faro-shuffle:
my @shuffledDeck = @originalDeck;

foreach my $i (1 .. 1000)
{
   @shuffledDeck = faroShuffle(@shuffledDeck);

   if ("@shuffledDeck" eq "@originalDeck")
   {
      print "The deck is back in new-deck order after $i out-faro shuffles.\n";
      last;
   }
}

__END__
