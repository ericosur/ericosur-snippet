#!/usr/bin/perl

use strict;

my %hash = qw{ Allen 85 Cathy 34 Paul 73 };

my @keys;

@keys = keys(%hash);
for (@keys)  {
	print "$_ => $hash{$_}\n";
	$hash{$_} = $hash{$_} ** 2;
}

