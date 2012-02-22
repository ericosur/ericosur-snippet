#!/usr/bin/perl

use strict;

my %hash;

while ( <> )
{
	#print $_;
	$hash{$1} = $2 if ( /(\w*)\s*=\s*(\w*)/ );
}

while ( my ($key, $value) = each(%hash) )  {
	print "$key => $value\n";
}
