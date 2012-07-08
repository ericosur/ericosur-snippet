#!/usr/bin/perl

use strict;

# demo to associate two array to a hash

my @key = qw( kitty mouse pony goat );
my @value = qw( 61 11 37 49 83 );
my %hash;

for ( my $i = 0; $i < @key; $i++ )  {
	$hash{$key[$i]} = $value[$i];
}

while ( my ($k, $v) = each(%hash) )  {
	print "$k => $v\n";
}
