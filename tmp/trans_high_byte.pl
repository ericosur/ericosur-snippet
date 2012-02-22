#!/usr/bin/perl

use strict;

my $file = "filelist.txt";
open FH, $file or die;

while (<FH>)
{
#	print $_;
	translate_line($_);
}

close FH;


sub translate_line()
{
	my $line = shift;
	my @arr = split //, $line;
	foreach (@arr)
	{
		my $ch = $_;
		my $asc = ord($ch);

		if ($asc <= 0x20 || $asc >= 0x7f)
		{
			printf "%%%02x", $asc;
		}
		else
		{
			print $ch;
		}
	}
	print "\n";
}

