#!/usr/bin/env perl

# just load bash history file into hash and
# display it by ascending

use strict;
use warnings;

sub Ascending($$) 
{
	my ($a, $b) = @_;
	$a <=> $b;
}

sub show($)
{
	my $ref = shift;
	foreach my $kk (sort Ascending keys %$ref)  {
		printf "hist{%s} = %s\n", $kk, $$ref{$kk};
	}
}

sub check_file($)
{
	my $f = shift;
	if ( not -e $f )  {
		my $hm = $ENV{'HOME'};
		$f = $hm . '/' . $f;
	}
	return $f;
}

sub main()
{
	my $file = '.bash_history';
	my %hist = ();
	my $cnt = 0;

	$file = check_file($file);
	open my $fh, $file or die;

	while ( <$fh> )  {
		s/[\r\n]//;
		$hist{$cnt} = $_;
		++ $cnt;
	}
	close $fh;

	show(\%hist);
}

main();

