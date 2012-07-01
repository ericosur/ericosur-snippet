#!/usr/bin/perl

use strict;
use warnings;
use Storable;
use v5.10;

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

	# try to factorize from the smallest prime
	for ($idx = 1; $idx <= $max_index && $val > 1; ++ $idx)  {
		$fac = $prime{$idx};
		last if ($fac > $upper);
		while (($val > $fac) && ($val % $fac == 0))  {
			printf "%d\t", $fac;
			++ $res{$fac};
			$val /= $fac;
		}
	}
	# still cannot be factorized, should be a prime
	if ($val > 1)  {
		++ $res{$val};
	}
}


sub main
{
	# load data from storage file
	if (-e $store_file)  {
		print STDERR "load from stored data file\n";
		%prime = %{ retrieve($store_file) };   # direct to hash
	} else  {
		print STDERR "load from plain text file\n";
		load_prime_table();
	}
	$max_index = scalar(keys(%prime));
	$max_prime = $prime{$max_index};
	#printf "max_index = %d, max_prime = %d\n", $max_index, $max_prime;

	# to filter
	my $idx = 1;
	my $cnt = 0;
	while ($idx < $max_index)  {
		my $num = $prime{$idx++};
		next if $num < 1000;
		last if $num > 9999;
		say $num;
		$cnt ++;
	}
	say STDERR "four digit primes count: ", $cnt;
}

main;
