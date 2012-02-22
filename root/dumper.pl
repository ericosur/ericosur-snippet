#!/usr/bin/perl
#
# Data::Dumper
#
# 2007/01/10 by ericosur

use Data::Dumper;

sub sep
{
	print '-' x 70, "\n";
}

my $foo = "123456780";

print Dumper($foo);
sep();

my @arr = qw(dog easy hill victory);
print Data::Dumper->Dump(\@arr);
sep();

__END__;

use Dumpvalue;
#use Rasmus;
require "gcd.pl";

my $dmp = Dumpvalue->new("DumpPackages" => 1);
$dmp->dumpvars('gcd.pl');
sep;

