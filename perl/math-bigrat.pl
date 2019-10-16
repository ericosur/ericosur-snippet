#!/usr/bin/perl
#
# by ericosur
#

use strict;
use warnings;

use Math::BigRat;

sub show($);

my $x = Math::BigRat->new('3/7');
show($x);
$x += 1;
show($x);

show($x->bstr());

# to calculate 32!
my $num = 32;
print "$num! = ", Math::BigRat->new($num)->bfac(),"\n";

sub show($)
{
	my $value = shift;
	print "==> $value\n";
}
