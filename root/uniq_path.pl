#!/usr/bin/perl

use strict;
use warnings;

use Env qw(@PATH $PATH);

sub uniq(@)
{
	my %seen = ();
	my @result = grep { ! $seen{$_} ++ } @_;

	while ( my ($k,$v) = each(%seen) )  {
		print STDERR "==> duplicated: ", $k, "\n" if $v > 1;
	}
	return @result;
}

sub main
{
	print STDERR "==> before count: ", $#PATH+1, "\n";
	#@PATH = map { shorten_path($_) } @PATH;
	#print STDERR "==> after count: ", $#PATH+1, "\n";
	#print STDERR join(';', @newp), "\n";

	@PATH = uniq(@PATH);
	print STDERR "==> after count: ", $#PATH+1, "\n";
	#print $#PATH, "\n";

	foreach (@PATH) {
		print $_,"\n";
	}
}

main;
