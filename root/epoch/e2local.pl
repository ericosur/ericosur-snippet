#!/usr/bin/perl

# from given epoch time 'from `date +%s`'
# to parsed YYYY-MM-DD hh:mm:ss

use strict;
use Time::Local;
#use v5.10;

my ($ss,$mm,$hh,$mdd,$mmm,$year,$wday,$yday,$isdst) = ();

sub readable_epoch($)
{
    my $ep = shift;
    ($ss,$mm,$hh,$mdd,$mmm,$year,$wday,$yday,$isdst) = localtime($ep);
    printf("epoch: %d\n", $ep);
    printf("%04d/%02d/%02d\t",($year+1900),($mmm+1),$mdd);
    printf("%02d:%02d:%02d\n", $hh, $mm, $ss);
}

sub main()
{
    my $epoch = 1305617116;
    print("call localtime by assigning epoch\n");
    readable_epoch($epoch);

    print("epoch from 'date +\%s'\n");
    $epoch = `date +%s`;
    readable_epoch($epoch);

    print("epoch from time()\n");
    $epoch = time();
    readable_epoch($epoch);
}

main;
