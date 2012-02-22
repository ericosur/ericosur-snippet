#!/usr/bin/perl

use strict;
use warnings;
use Storable;

my $plain_file = "prime_1M.txt";	# prime_(100k|1M).txt
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

	my $limit = 2000000;
	my $sum = 0;
	for (my $i=1; ;$i++) {
		my $val = $prime{$i};
		if ($val > $limit) {
			last;
		}
		$sum += $prime{$i};
	}
	print "sum: ", $sum, "\n";
}

main;
