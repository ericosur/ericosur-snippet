#!/usr/bin/perl
use strict;
use warnings;


my @vob = qw(apple ball cat);
my @array = ();

# an array with ref to hash
# if $_ is modified in map{} context, the
# source array would be modified too.
@array = map { getValue($_) } @vob;

print $#array + 1,"\n";	# array length
print @array,"\n";	# the array dump

# show all elements
for my $rr (@array)  {
	for my $rh (keys %$rr)  {
		print $rh, "=>", $rr->{$rh}, "\n";
	}
}


#
# getValue()
#
# input: a string
# output: a reference to a hash contains {"input string" => calculated value}
# the value is the hex number sum of each character from the input string
#
sub getValue($)
{
	my $arg = shift;
	my $result = 0;
	my %tmp = ();

	for (split //,$arg)  {
		$result += ord($_);
	}

	$tmp{$arg} = $result;
	return \%tmp;
}
