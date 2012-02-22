#!/usr/bin/perl

use strict;

my @score = qw( 1 1 );
my @chars = qw( a );

foreach my $i (2..10)  {
	$score[$i] = $score[-1] + $score[-2];
	$chars[@chars+1] = ++ $chars[-1];
}

print "\nWhole array:\n";
foreach (@score)  {
	print "$_\t";
}
print "\n";

print "\nWhole chars array:\n";
foreach (@chars)  {
	print "$_\t";
}
print "\n";

