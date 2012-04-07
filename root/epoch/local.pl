#!/usr/bin/perl

# print epoch time

use strict;
use Time::Local;

# get time from localtime
my ($sec,$min,$hours,$mday,$month,$year,$wday,$yday,$isdst) = localtime;
# get time using timelocal
my $time = timelocal($sec,$min,$hours,$mday,$month,$year+1900);

#my ($year, $month, $mday, $hours, $min, $sec) = (2009, 4, 15, 16, 0, 0);
foreach my $ii (localtime)  {
	print $ii,"\t";
}
print "\n";
print "timelocal = ", $time, "\n";
print "time = ", time(), "\n";	# same as ''date +%s''
print 'date +%s: ' . `date +%s` . "\n";

