#!/usr/bin/perl

# from given epoch time 'from `date +%s`'
# to parsed YYYY-MM-DD hh:mm:ss

use strict;
use Time::Local;
#use 5.010;

#my $epoch = 1305617116;
my $epoch = `date +%s`;

my ($ss,$mm,$hh,$mdd,$mmm,$year,$wday,$yday,$isdst) = localtime($epoch);

printf("current epoch: %d\n", $epoch);
printf("%04d-%d-%02d\t",($year+1900),($mmm+1),$mdd);
printf("%02d:%02d:%02d\n", $hh, $mm, $ss);
