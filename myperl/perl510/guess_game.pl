#!/usr/bin/env perl
#
# how to supress warning for given, when
# https://stackoverflow.com/questions/43376193/how-to-mute-that-when-and-given-are-experimental-in-perl

# list of experimental
# https://metacpan.org/pod/experimental

# guessing game
use strict;
use feature qw(switch say);
no if $] >= 5.018, warnings => qw( experimental::smartmatch );

my @guessed;
my $num = int(rand 100)+1;
say "input your guess...";
while (my $guess = <STDIN>)  {
    chomp $guess;
    given($guess)  {
        when (/\D/)     { say "give me an integer" }
        when (@guessed) { say "you've tried that" }
        when ($num)     { say "you got it!"; last }
        when ($_ < $num)    { say "too low"; continue }
        when ($_ > $num)    { say "too high"; continue }
        push(@guessed, $_);
    }
}
