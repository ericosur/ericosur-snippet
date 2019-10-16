#!/usr/bin/perl
#@ test for reversing STDIN strings
# 2007/11/16 by ericosur
#
# reverse array and string

use strict;
use warnings;

sub print_sep
{
	print "\n", '-' x 40, "\n";
}

my @array = qw(alpha beta charlie delta);

# reverse an array
print join ' ', reverse @array;
print_sep;

# reverse a string
my $str = "yamada takatoshi";

print "str = ", $str;
print "\n";
print reverse $str;	# here nothing changed ???
print_sep;

print "str = ", $str;
print "\n";
my $rev = reverse $str;	# it works fine
print $rev, "\n";
print_sep;

