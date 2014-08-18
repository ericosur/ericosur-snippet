#!/usr/bin/perl

# problem described at http://projecteuler.net/index.php?section=problems&id=12
# What is the value of the first triangle number to have over five hundred divisors?

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

# to factorize the input number, result stored at %res
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
			#printf "%d\t", $fac;
			++ $res{$fac};
			$val /= $fac;
		}
	}
	# still cannot be factorized, should be a prime
	if ($val > 1)  {
		++ $res{$val};
	}
}

# to calculate triangle number
sub get_triangle_num($)
{
	my $nn = shift;
	if ($nn < 1) {
		die "no such number";
	} elsif ($nn == 1) {
		return 1;
	} else {
		my $sum = (1 + $nn) * $nn / 2;
		return $sum;
	}
}


sub main
{
	# load data from storage file
	if (-e $store_file)  {
		print "load from stored data file\n";
		%prime = %{ retrieve($store_file) };   # direct to hash
	} else  {
		print "load from plain text file\n";
		load_prime_table();
	}
	$max_index = scalar(keys(%prime));
	$max_prime = $prime{$max_index};
	printf "max_index = %d, max_prime = %d\n", $max_index, $max_prime;

	my $beg = 20;
	my $end;
	my $limit = 500;
	for (my $i=$beg; ; $i++) {
		my $tar = get_triangle_num($i);
		print "#",$i,"\t",$tar,"\t";
		%res = ();
		lookup($tar);
		#print "\n";
		# output the factors
		my $sum = 1;
		foreach my $ky (sort {$a <=> $b} keys %res)  {
			#printf "%d^%d\t", $ky, $res{$ky};
			$sum = $sum * ($res{$ky} + 1);
		}
		say "$sum";
		if ($sum > $limit) {
			say "have more than $limit factors!";
			last;
		}
	}

}

main;
