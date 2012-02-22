#!/usr/bin/perl

# just a studid perl script that pick one name 
# from name list
# Jan 28 2005 by ericosur

use strict;
use warnings;

# names from Penguins
my @name_list = qw(
	allen chris clive horse jojo patty rasmus
	robin ob david tom neil stanley winson sam
	tony henry eric mary joe maggie bob alice
	patty arthur patrick vincent bill john
	woody
);

my $len = @name_list;
#print "There are $len persons in the list\n";

print "pick one is: ";
#for my $i (1..20) {
	print $name_list[int(rand($len))] . "\n";
#}

print '$len = ', $len, "\n";
print '$#name_list = ', $#name_list, "\n";
printf "length(\@name_list) = %d\n", length(@name_list);

