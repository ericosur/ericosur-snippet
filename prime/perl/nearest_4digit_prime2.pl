#!/usr/bin/env perl

use strict;
use warnings;
use Storable;
use v5.10;

# arg1: file name with prime numbers
# file format: one prime number each line
# arg2: file name that stored dat
# returns an array with loaded primes
sub load_prime_table($$)
{
	my $plain_file = shift;
	my $store_file = shift;
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
	my $store_file = 'fourdigit.dat';
	my @fprime = ();

	if ( -e $store_file )  {
		print STDERR "load from stored data file\n";
		@fprime = @{ retrieve($store_file) };   # direct to hash
	}
	elsif ( -e $pfile )  {
		@fprime = load_prime_table($pfile, $store_file);
	}
	else  {
		say "no $pfile, exit...";
		return;
	}

	# try 10 times
	for ( 1 .. 1000)  {
		my $nn = get_one_rand_number(9999, 1000);
		find_nearest_prime($nn, \@fprime);
		#say "nn: ", $nn;
	}
=pod
	for my $nn ( 1003 .. 1109 )  {
		find_nearest_prime($nn, \@fprime);
		say '-' x 40;
	}
=cut
}

# num: one number to find
# array: reference to an array which contains primes
# returns nearest prime with gived number
sub find_nearest_prime($$)
{
	my $num = shift;
	my $rf = shift;
	my @prm = @$rf;
	my $size = scalar @prm;
	my ($res,$old) = (0,0);
	my ($max, $min) = ($prm[$size-1], $prm[0]);

	say "num: ", $num;
	#say "max: ", $max;
	#say "min: ", $min;

	if ($num > $max)  {
		say "$num is bigger than $max" ;
		$res = $max;
		goto output;
	}
	if ($num < $min)  {
		say "$num is smaller than $min" ;
		$res = $min;
		goto output;
	}

	my $flag = 0;
	for ( my $idx = 0; $idx < $size; $idx++ )  {
		my $tt = $prm[$idx];
		if ($tt == $num)  {	# the same
			$res = $tt;
			last;
		}
		elsif ($tt > $num) {
			if ($flag == 0)  {
				$flag = 1;
				#say "upper: ", $tt;
				$res = $tt;
				last;
			}
		}
		elsif ($tt < $num) {
			$old = $tt;
		}
	}

output:
	if ($old)  {
		printf "%d %s %d %s %d\n",
			$old, ($old == $num ? '=' : '<'),
			$num, ($res == $num ? '=' : '<'),
			$res;
	}
	else  {
		printf "< %d %s %d\n",
			$num, ($res == $num ? '=' : '<'),
			$res;
	}
	return $res;
}

main;
