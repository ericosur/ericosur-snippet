#!/usr/bin/perl

# to demo a simple hash usage

use strict;
use warnings;

my %hash = ();
my $ch = 'A';

foreach my $n (1..6)  {
	$hash{$ch} = $n ** 3;
	$ch ++;
}

#while ( my ($key, $value) = each (%hash) )  {
#	print "$key => $value\n";
#}

print "keys ==>\n";

# notice: it would not displayed by order
my @keys = keys(%hash);
for (@keys)  {
	print "$_ => $hash{$_}\n";
}

print "\n";
print "values ==>\n";

my @values = values(%hash);
for (@values)  {
	print "$_\n";
}

