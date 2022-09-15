#!/usr/bin/perl
#
# example for Roman <-> arabic numbers
#

use strict;
use Roman;

sub show($$)
{
	my ($lhs, $rhs) = @_;
	printf("%s => %s\n", $lhs, $rhs);
}

sub getYear()
{
	my ($ss,$mm,$hh,$mdd,$mmm,$year,$wday,$yday,$isdst) = localtime();

	#printf("%04d-%d-%02d    ",($year+1900),($mmm+1),$mdd);
	#printf("%02d:%02d:%02d\n", $hh, $mm, $ss);
	return $year+1900;
}

sub main()
{
	my $arabic = 2009;
	my $roman = Roman($arabic);
	#$roman = roman($arabic);
	show($arabic, $roman);

	$roman = "mcmxciii";
	$arabic = arabic($roman) if isroman($roman);
	show($roman, $arabic);

	printf("This year: \n");
	show(getYear(), roman($arabic));
	show(getYear(), Roman($arabic));
}

main;
