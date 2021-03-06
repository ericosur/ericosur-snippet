#!/usr/bin/env perl

#
# [OEIS A005117](https://oeis.org/A005117)
# Squarefree numbers: numbers that are not divisible by a square greater than 1.
# (Formerly M0617)
#
# 1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31,
# 33, 34, 35, 37, 38, 39, 41, 42, 43, 46, 47, 51, 53, 55, 57, 58, 59, 61, 62,
# 65, 66, 67, 69, 70, 71, 73, 74, 77, 78, 79, 82, 83, 85, 86, 87, 89, 91, 93,
# 94, 95, 97, 101, 102, 103, 105, 106, 107, 109, 110, 111, 113

use strict;

my @prm = qw(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97);
my $max = 65535;

sub getsquarefree($)
{
	my $v = shift;
	my @dig = reverse(split(//,$v));
	my $r = 1;
	my $j = 0;
	foreach my $i (@dig) {
		#printf("i:%d === ", $i);
		#printf("<%d>", $prm[$j] ** $i);
		if ($i) {
			$r = $r * $prm[$j] ** $i;
		}
		$j ++;
	}
	printf("[%d]: %d %s\n", $v, $r, ($r<=$max?"":"nok"));
}

sub main()
{
	for (my $i=0; $i<0b1111010; $i++) {
		my $seq = sprintf("%b", $i);
		printf("%d ", $i);
		getsquarefree($seq);
	}
}

main;
