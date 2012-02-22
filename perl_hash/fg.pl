#!/usr/bin/perl

use strict;
use warnings;

my %hash = ();
my $ch = 'A';

foreach (1..6)  {
	$hash{$ch} = $_ ** 3;
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
