#!/usr/bin/perl

use strict;
use warnings;
use Storable;

my $plain_file = "prime_100k.txt";	# prime_(100k|1M).txt
my $store_file = "prime.dat";
#my $index_file = "idx.dat";
my $max_index = 0;
my $max_prime = 2;
my %prime = ();
my @idx = ();
my %res = ();

sub load_prime_table();
sub main;
#sub build_index;
sub lookup($);

sub load_prime_table()
{
	# load from plain text file
	open my $ifh, $plain_file or die;

	my $count = 0;
  LINE:
	while (<$ifh>)  {
		next LINE if ( m/^$/ || m/^#/ );
		if (m/(\d+)\s+(\d+)/)  {
			$prime{$1} = $2;
			++ $count;
		}
	}

	printf "%d prime numbers parsed from text file\n", $count;
	# and store it into data file
	store(\%prime, $store_file);
	close $ifh;
}


sub lookup($)
{
	my $val = shift;
	my $upper = sqrt($val);
	my $idx;
	my $fac;
	my $debug = 0;

	# try to factorize from the smallest prime
	for ($idx = 1; $idx <= $max_index && $val > 1; ++ $idx)  {
		$fac = $prime{$idx};
		last if ($fac > $upper);
		while (($val > $fac) && ($val % $fac == 0))  {
			printf "%d\t", $fac if $debug;
			++ $res{$fac};
			$val /= $fac;
		}
	}
	# still cannot be factorized, should be a prime
	if ($val > 1)  {
		++ $res{$val};
	}
	print "\n" if $debug;
}


sub main
{
	my $verbose = 0;
	# load data from storage file
	if (-e $store_file)  {
		print "load from stored data file\n" if $verbose;
		%prime = %{ retrieve($store_file) };   # direct to hash
	} else  {
		print "load from plain text file\n" if $verbose;
		load_prime_table();
	}
	$max_index = scalar(keys(%prime));
	$max_prime = $prime{$max_index};
	if ($verbose) {
		printf "max_index = %d, max_prime = %d\n", $max_index, $max_prime;
	}

	# accept input from user
	for (my $i=2; $i<=10; $i++) {
		%res = ();
		lookup($i);
		# output the factors
		foreach my $ky (sort {$a <=> $b} keys %res)  {
			printf "%d^%d\t", $ky, $res{$ky};
		}
		print "\n";
	}
}

main;
