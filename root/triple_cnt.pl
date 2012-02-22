#!/usr/bin/perl
#
# �p�y�P���i��ĳ���p��
# ���D #5, 12�ɨ�q�l���A�T��Ʀr�ۦP�����Ʀ��X���H
# �q�l�����|��Ʀr 12:00 -> 11:59
#
# �����D�O�۳s���T��Ʀr�Aregexp �ݭn��
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

