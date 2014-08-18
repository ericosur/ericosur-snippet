#!/usr/bin/perl

#@ useful for split path tokens
#
# also refer to cenv.pl for the other way
#

use strict;
use warnings;

=pod
# method #1, the tokens would be stored into an array
# or ``use Env qw(@PATH)''

my $path = $ENV{"PATH"};
my @array = split /;/, $path;

foreach (@array)
{
	print "$_\n";
}
=cut

#
# method #2, for your eyes only
#
my $foo = $ENV{"PATH"};

if ($^O eq 'MSWin32')  {
	$foo =~ s/;/\n/g;
}
else  {
	$foo =~ s/:/\n/g;
}

print $foo,"\n";

