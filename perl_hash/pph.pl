#!/usr/bin/perl

use strict;

open FH, "< birth.txt" or die "cannot open $!\n";

my %hash;

LOOP: while ( <FH> )
{
	next LOOP if /^#/;
	if ( /(\w*)\s*=>\s*(.*)/ )  {
		if (exists $hash{$1})  {
			print "$1 already exists, skipped\n" ;
			next LOOP;
		}
		else  {
			$hash{$1} = $2;
		}
	}
}

close FH;

while ( my ($k, $v) = each(%hash) )  {
	print "$k => $v\n";
}

print "\n Print out matched items\n";
my @match = grep {$_ gt '1980'}  values(%hash);

for (@match)  {
	print "$_\n";
	print "$hash{$_}\n";
}

