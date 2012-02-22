#!/usr/bin/perl
#
# 雷頓與不可思議之小鎮
# 謎題 #5, 12時制的電子鐘，三位數字相同的次數有幾次？
# 電子鐘有四位數字 12:00 -> 11:59
#
# 本問題是相連的三位數字，regexp 需要改
#
# 2007/09/26 by ericosur

use strict;
use warnings;


my $hh = 11;
my $mm = 59;

sub main()
{
	my $triple = 0;

	# init values for increase_hour()
	my $cnt = 0;
	my $total = 24*60;
	# init values for increase_hour()


	while ($cnt < $total)
	{
		++ $cnt;
		$_ = increase_hour(\$hh,\$mm);
		if ( /(\d)\1:(\1\d|\d\1)/ or /(\d)\d:\1\1/ or /\d(\d):\1\1/)
		{
			print;
			print "\t";

			$triple ++;
		}
	}


	print "\ncount for triple same digits: $triple\n";
}

#####################################################################
# a function to count like a 12-hour clock
#####################################################################
sub increase_hour()
{
	my $time_str;

	++$mm;
	if ($mm >= 60)
	{
		$mm = 0;
		++ $hh;
	}

	if ($hh > 12)
	{
		$hh = 1;
	}

	$time_str = sprintf "%02d:%02d", $hh, $mm;

	return $time_str;
}
#####################################################################

main;

