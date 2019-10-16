#!/usr/bin/env perl

#
# demo DateTime delta_days
#

use strict;
use DateTime;
use 5.010;

my $dt1 = DateTime->new( year => 2012, month => 2, day => 10 );
my $dt2 = DateTime->new( year => 2014, month => 10, day => 14 );
my $days = $dt1->delta_days($dt2)->delta_days;
# $days becomes 365
say "from date: ", $dt1;
say "  to date: ", $dt2;
say " are ", $days, " days";
