#!/usr/bin/perl

use strict;
use v5.10;

# create hash from a qw list
my %hash = qw{ Allen 85 Cathy 34 Paul 73 };

foreach ( keys(%hash) )  {
	say $_, " => ", $hash{$_};
	$hash{$_} = $hash{$_} ** 2; # alter value
	say $hash{$_};
}
