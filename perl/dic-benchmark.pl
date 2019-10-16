#!/usr/bin/env perl

# example to use 'timethis' to calculate time during while
# running some function

use strict;
use warnings;
use Benchmark qw(:hireswallclock);
use Data::Dump qw(dump);

sub gen_dic()
{
	my $upper_limit = 100;
	my %dic = ();
	for my $i (1 .. $upper_limit)  {
		$dic{$i} = $i ** 2;
	}
	return %dic;
}

sub swap_dic($)
{
	my $ref = shift;
	my %Dic = %{ $ref };
	my %IDic = ();
	while ( my ($kk, $vv) = each %Dic )  {
		$IDic{$vv} = $kk;
	}
	return %IDic;
}

sub test_dic()
{
	my %dic = gen_dic();
	swap_dic(\%dic);
}

sub main()
{
	timethis( 1e5, "test_dic()" );
}

main;
