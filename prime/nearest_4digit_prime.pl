#!/usr/bin/env perl

use strict;
use warnings;
use Storable;
use 5.010;

# arg: file name with prime numbers
# file format: one prime number each line
# returns an array with loaded primes
sub load_prime_table($)
{
	my $plain_file = shift;
	my @primes = ();

	# load from plain text file
	open my $ifh, $plain_file or die;

	my $count = 0;
  LINE:
	while (<$ifh>)  {
		next LINE if ( m/^$/ || m/^#/ );
		s/[\r\n]//;
		if (m/(\d+)/)  {
			push @primes, $1;
			++ $count;
		}
	}
	close $ifh;

	printf STDERR "%d prime numbers parsed from text file\n", $count;
	# and store it into data file
	my $store_file = 'fourdigit.dat';
	store(\@primes, $store_file);
	say STDERR "stored into $store_file";

	return @primes;
}


# input (upper, lower)
# output one random number with (upper, lower)
sub get_one_rand_number($$)
{
	my ($upper, $lower) = @_;

	my $range = $upper - $lower + 1;
	my $num;

	$num = int(rand($range)+$lower);
	return $num;
}


sub main()
{
	my $pfile = '4digitprime.txt';
	my @fprime = ();

	if ( -e $pfile )  {
		@fprime = load_prime_table($pfile);
	}
	else  {
		say "no $pfile, exit...";
		return;
	}

	# try 10 times
	for ( 1 .. 1)  {
		my $nn = get_one_rand_number(9999, 1000);
		find_nearest_prime($nn, \@fprime);
		say "nn: ", $nn;
	}
}

# num: one number to find
# array: reference to an array which contains primes
# returns nearest prime with gived number
sub find_nearest_prime($$)
{
	my $num = shift;
	my $refprm = shift;
	my @prm = @$refprm;
	my $size = scalar(@prm); 	# size of array
	my $idx = $size / 2;
	my $dist = -1;
	my ($prev, $test) = (0,0);

	# try binary search
	my $cnt = 0;
	while ( $idx >= 0 || $idx < $size )  {
		last if $cnt > 20;
		$test = $prm[$idx];
		printf("(%d) try idx: %d => %d\t", $cnt, $idx, $test);
		$cnt ++;
		if ($prev == $test)  {  # repeats...
			say "repeats... exit...";
			last;
		}
		$prev = $test;
		$dist = $num - $test;
		say "dist: ", $dist;
		if ($dist == 0)  {	# it is a prime
			say $num, " is a prime";
			return $num;
		}
		elsif ($dist > 0)  {  # number > test
			$idx = ($idx + $size) / 2;
		}
		elsif ($dist < 0)  {  # number < test
			$idx = $idx / 2;
		}
	}
	say "dist: ", $dist;
	say "num: ", $num;
	say "test: ", $test;
}

main;
