#!/usr/bin/perl

use strict;
use warnings;
use v5.10;

sub test_num($)
{
    my $num = shift;
    my $res = $num % 6;
    if ( $res == 5 )  {
        say "$num -";
        return 1
    } elsif ( $res == 1 )  {
        say "$num +";
        return 1;
    } else  {
        return 0;
    }
}

sub main()
{
    my $min = 1001;
    my $max = 9999;
    my $cnt = 0;
    for (my $nn = $min; $nn <= $max; ++$nn)  {
        my $res = test_num($nn);
        ++ $cnt if $res == 1;
    }
    say "cnt: $cnt";
}

main;
