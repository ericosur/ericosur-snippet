#!/usr/bin/perl
#
# invoke 'cmd /c dir /q'
# and parse the file size column
# and sum the sizes up
#
# refer to space.pl
#
# Jun 9 2005 by ericosur


use strict;
use warnings;


my $res = `cmd /c dir /q`;
my @lines = split /\n/, $res;
my $size;
my $total = 0;
my $count = 0;

LOOP:
foreach (@lines)
{
#	print 'x:', $_, "\n";
	next LOOP if ( m[<DIR>] );		# skip the <dir> name

	if ( m/^[\d\/]+\s+\d\d\:\d\d\s+([\d,]+)\s+/ )
	{
		$size = $1;
		$size =~ s/,//;		# chop the '',''
		print $size, "\t";
		$total += $size;
		++ $count;
	}
}

printf "\nTotal %d files, size = %d bytes\n", $count, $total;
