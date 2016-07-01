#!/usr/bin/perl

# a demo to load %hash from a "key = value" text file

use strict;

sub main()
{
	my %hash;

	while ( <> )
	{
		#print $_;
		$hash{$1} = $2 if ( m/(\w+)\s*=\s*(\w+)/ );
	}

	while ( my ($key, $value) = each(%hash) )  {
		print "$key => $value\n";
	}
}

main;

