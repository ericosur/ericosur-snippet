#!/usr/bin/perl

#
# reference from http://plog.longwin.com.tw/my_note-programming/2009/05/21/regex-check-range-1-99-2009
#
# an regular expression to match 1-99 without leading 0
#

use strict;
use warnings;

my $rep = qr(^([1-9][0-9]?|)$);
my @test = qw(1 01 2 03 5 8 13 21 34 101);	# 01, 03, 101 not matched

foreach (@test)  {
	print $_, "\t";
	if ( m/$rep/ )  {
		print "matched and $1\n";
	}
	else  {
		print "not matched\n";
	}
}
