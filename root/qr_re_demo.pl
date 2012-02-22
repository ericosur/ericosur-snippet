#!/usr/bin/perl
#
# 2006/12/27 by ericosur
#

my @str = (
	qq(The pi value is 3.1415926),
	qq(square root of two would be sqrt(2)),
);
my $reg = qr{(\d+(\.?(\d*)))};

for my $z (@str)
{
	printf "#: %s\n", $z;
	my ($a, $b, $c) = $z =~ $reg;
	printf "_%s_\n_%s_\n_%s_\n", $a, $b, $c;
}

