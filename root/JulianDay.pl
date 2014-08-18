#!/usr/bin/perl

# to demo Time::Julianday

use strict;
use Time::JulianDay;

my $seconds_since_1970 = time;	# unix epoch time

my $jd = local_julian_day($seconds_since_1970);
print $jd,"\n";

$jd = gm_julian_day($seconds_since_1970);
print $jd,"\n";

my ($year, $month_1_to_12, $day) = inverse_julian_day($jd);
print "y($year)\tm($month_1_to_12)\td($day)\n";

my $dow = day_of_week($jd);
print "the dow is ", qw(Sun Mon Tue Wed Thu Fri Sat)[$dow],"\n";
