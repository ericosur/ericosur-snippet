#!/usr/bin/perl
﻿#
# gen_big5.pl
# generate a table with big5 chars
#
# references: http://pcfarm.sinica.edu.tw/old/docs/utf8-big5-comparison/report.html
#

use strict;
use warnings;

my $count = 0;
my $total = 0;

sub is_ok($$)
{
	my ($hi, $lo) = @_;

	if ($hi == 0xA3)  {
		return 0 if ($lo >= 0xC0 && $lo <= 0xE0);
		return 0 if ($lo >= 0xE1 && $lo <= 0xFE);
	}
	if ($hi >= 0xFA && $hi <= 0xFE)  {
		return 0 if ($lo >= 0x40 && $lo <= 0xFE);
	}
	if ($hi >= 0x8E && $hi <= 0xA0)  {
		return 0 if ($lo >= 0x40 && $lo <= 0xFE);
	}
	if ($hi >= 0x81 && $hi <= 0x8D)  {
		return 0 if ($lo >= 0x40 && $lo <= 0xFE);
	}

# extra addition
# I don't understand that I could see the following big5 characters
# in my firefox browser, but I could not ''iconv'' these byte sequence.
#
# reference:
# http://ash.jp/code/cn/big5tbl.htm
#
# c840 - c875 russian
	if ($hi == 0xC8)  {
		return 0 if ($lo >= 0x40 && $lo <= 0xB4);
	}
	if ($hi == 0xC7)  {
		return 0 if ($lo >= 0xF3 && $lo <= 0xFF);
	}
	if ($hi == 0xC6)  {
		return 0 if ($lo >= 0xDE && $lo <= 0xDF);
	}
	if ($hi == 0xC8)  {
		return 0 if ($lo >= 0xB5 && $lo <= 0xFE);
	}

	return 1;
}

sub follow_range($$$$$)
{
	my ($fh, $hmin, $hmax, $lmin, $lmax) = @_;
	for (my $ii = $hmin; $ii <= $hmax; ++$ii)  {
		for (my $jj = $lmin; $jj <= $lmax; ++$jj)  {
			++ $total;
			if ( is_ok($ii, $jj) )  {
				printf $fh "%X%X\t", $ii, $jj;
				print $fh chr($ii), chr($jj), "\n";

				++ $count;
			}
			print STDERR "$count / $total\r";
		}
	}
}

my $ofile = "big5.txt";
my $ofh;

open $ofh, "> $ofile" or die;
binmode $ofh;
print STDERR "ofile = $ofile\n";

# big5 range
# high byte: A1~FE, 8E~A0, 81~8D
# low byte: 40~7E, A1~FE
# it seems that more characters need to be excluded
follow_range($ofh, 0xA1, 0xFE, 0x40, 0x7E);
follow_range($ofh, 0xA1, 0xFE, 0xA1, 0xFE);
follow_range($ofh, 0x8E, 0xA0, 0x40, 0x7E);
follow_range($ofh, 0x8E, 0xA0, 0xA1, 0xFE);
follow_range($ofh, 0x81, 0x8D, 0x40, 0x7E);
follow_range($ofh, 0x81, 0x8D, 0xA1, 0xFE);

print STDERR "\n";
close $ofh;

my $uft8_file = "utf8-iconv.txt";
system "iconv -f BIG5-2003 -t UTF-8 $ofile > $uft8_file";
