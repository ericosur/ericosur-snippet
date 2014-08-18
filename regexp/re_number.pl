#!/usr/bin/perl
#
# RegEx to match numbers
#

use strict;

while (<DATA>)  {
	s/\n//;
	if ( /([+-]?\d+)(?:\.\d)? *([CcFf])?/ )  {
		print "$_\n";
		print "1: $1\n" if $1;
		print "2: $2\n" if $2;
		print "3: $3\n" if $3;
	}
	print "\n";
}

__DATA__
23.39283 c
3.1415926 F
-3829.283 C
+998.82
