#!/usr/bin/perl
# unpack_string.pl
#
# unpack char into array
#
# 2007/01/10 by ericosur

my @ascii = unpack("C*", 'ABCXYZabcxyz');

foreach (@ascii)
{
	printf "%x ", $_;
}
print "\n";

