#!/usr/bin/perl

use strict;

#while ( <> )
my $i;
my @key = {};
my @value = {};

for ($i = 0; <> ; $i++)
{
	#print $_;
	if ( /(\w*)\s*=\s*(\w*)/ )  {
		$key[$i] = $1;
		$value[$i] = $2;
	}
}

print "total items = $i\n";

for ($i = 0; $i < @key; $i++)  {
	printf "%s = %s\n", $key[$i], $value[$i];
}

print "\nmap function test...\n";
my @addpoint = map { sqrt($_) * 10 } @value;

print join ', ', @addpoint;
foreach (@addpoint)  {
	print "$_\n";
}
