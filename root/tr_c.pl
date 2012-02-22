#!/usr/bin/perl
#
# some data structure test
#
# 2006/12/27 by ericosur

use strict;
use warnings;


my $test_str = q(Je tiens qu'a toi 'what');

printf "";

$_ = $test_str;
print $_, "\n";


tr['][*];
print;
print "\n";

# two
my $a = qq(­^¶¯);
if ($a =~ /\Q­^\E/)
{
	print "matched\n";
}

#three
my @hash;
$hash[0]{"name"} = 'smith';
$hash[0]{"number"} = 93;
$hash[1]{"name"} = "mary";
$hash[1]{"number"} = 32;

foreach (keys %{$hash[0]})
{
	print "$_\n";
}
