#!/usr/bin/perl

use strict;
use Math::BigFloat;

sub try($)
{
    my $val = shift;
    my $tryval = Math::BigFloat->new($val);
    my $target = Math::BigFloat->new("0.000001002003004005006007008009010");
	my $res = Math::BigFloat->bone();
	$res->bdiv($tryval);
	$res->bsub($target);
	return $res->babs();
}

sub main()
{
	my $lower = Math::BigFloat->new("0");
	my $upper = Math::BigFloat->new("999_999");
	my $distance = Math::BigFloat->bone();
	my $lasttry;
	my $cnt = 0;
	my $maxtry = 99;
	my $gap = Math::BigFloat->bzero();

	while (1) {
		my $dist_low = try($lower);
		my $dist_upp = try($upper);
		$gap = $upper - $lower;
		if ($gap < 1) {
			print "gap smaller than 1\n";
			print "answer is ", $lower->bceil()->bstr(), "\n";
			last;
		}
		my $middle = $lower + $gap / 2;
		if ($dist_low > $dist_upp) {
			$lower = $middle;
		} else {
			$upper = $middle;
		}
		$cnt ++;
		if ($cnt > $maxtry) {
			print "reach max try\n";
			last;
		}
		$distance = try($middle);
		printf("%s ---> %s <--- %s  [%s]\n",
			$lower->bstr(),
			$middle->bstr(),
			$upper->bstr(),
			$distance->bstr());
	}
	printf("cnt: %d\n", $cnt);
}

main;
