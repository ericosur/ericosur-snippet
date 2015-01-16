# guessing game
use strict;
use feature qw(switch say);

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
