#!/usr/bin/perl

use strict;
use v5.10;

# a way to create fib list

sub show($)
{
    my $rarr = shift;
    foreach (@$rarr) {
        print "$_,";
    }
}

sub create_fib()
{
    my @vector = qw(1 1);
    foreach my $i (2..10) {
        $vector[$i] = $vector[-1] + $vector[-2];
    }
    show(\@vector);
}


sub main()
{
    create_fib();
    say;
}

main;
