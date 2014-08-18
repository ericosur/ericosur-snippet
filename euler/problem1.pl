#!/usr/bin/perl

# problem: http://projecteuler.net/problem=1

use strict;
use v5.10;

sub assert($$$)
{
	my ($msg, $mm, $nn) = @_;
	if ($mm != $nn) {
		die $msg;
	}
}

sub find_max_multiple($$)
{
	my $max = shift;
	my $multi = shift;
	my $nn = $max - 1;
	while ($nn > 0) {
		if ($nn % $multi == 0) {
			return $nn;
		}
		$nn --;
	}
	return 1;
}

sub sum_up($$$)
{
	my ($first, $least, $items) = @_;
	printf("sum_up(): first:%d,least:%d,items:%d\n",$first,$least,$items);
	my $sum = ($first + $least) * $items / 2;
	return $sum;
}

sub my_add_15()
{
	my $ceiling = 1000;
	my $sum = 0;
	for(my $i=1;$i<$ceiling;$i++){
		if (($i % 3 == 0) && ($i % 5 != 0)) {
			$sum += $i;
		} elsif (($i % 5 == 0) && ($i % 3 != 0)) {
			$sum += $i;
		} elsif ($i % 15 == 0) {
			$sum += $i;
		}
	}
	return $sum;
}

sub main()
{
	my $ceiling = 1000;
	my $l3 = find_max_multiple($ceiling, 3);
	my $l5 = find_max_multiple($ceiling, 5);
	my $l15 = find_max_multiple($ceiling, 15);
	#say "l3:",$l3;
	say "l15:",$l15;
	my $sum3 = sum_up(3,$l3,(($l3-3)/3+1));
	my $sum5 = sum_up(5,$l5,(($l5-5)/5+1));
	my $sum15 = sum_up(15,$l15,(($l15-15)/15+1));
	say "sum3:",$sum3;
	say "sum5:",$sum5;
	say "sum15:",$sum15;

	my $answer = $sum3 + $sum5 - $sum15;
	say "answer:", $answer;

	my $sum=my_add_15();
	say "sum:",$sum;
	assert("not equal", $sum, $answer);
}

main;
