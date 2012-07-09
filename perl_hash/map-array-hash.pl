#!/usr/bin/perl

# use map to associate two array into hash

use strict;
use v5.10;

sub show($)
{
    my $rarr = shift;
    my @arr = @$rarr;
    foreach (@arr) {
        say $_;
    }
}

sub main()
{
    my @array = qw( 2 3 5 7 11);

    my %hash = map { $_ => $_*2 } @array;
    say "print out new hash:";
    while ( my ($k, $v) = each (%hash) )  {
    	say "$k => $v";
    }

    my @newarray = map { $_ * 2 } @array;
    say "print out new array:";
    show(\@newarray);

    # you may see the array become double size
    my @newarray2 = map { $_ => $_ * 2 } @array;
    say "print out new array2:";
    show(\@newarray2);
}

main;
