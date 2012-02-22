#!/usr/bin/perl

# print epoch time

use strict;
use Time::Local;

my ($sec,$min,$hours,$mday,$month,$year,$wday,$yday,$isdst) = localtime;

my $time = timelocal($sec,$min,$hours,$mday,$month,$year+1900);

print "timelocal = ", $time, "\n";
print "time = ", time(), "\n";	# same as ''date +%s''
#my ($year, $month, $mday, $hours, $min, $sec) = (2009, 4, 15, 16, 0, 0);
foreach my $ii (localtime)  {
	print $ii,"\t";
}
print "\n";

