#!/usr/bin/perl
#
# a stupid script for Inline::Files
#
# ideas from perl cookbook
#

use strict;
use warnings;

use Inline::Files;

my @data = <DATA>;
my @foo = <FOO>;
my @bar = <BAR>;

for (@data)
{
	print;
}

for (@foo)
{
	print;
}

for (@bar)
{
	print;
}


__END__

__DATA__
apple
ball
cat
duck
__FOO__
one
two
three
four
__BAR__
alpha
bravo
charlie
delta