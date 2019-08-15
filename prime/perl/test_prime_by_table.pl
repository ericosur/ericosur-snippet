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


sub isprime($)
{
	my $val = shift;
	my $upper = sqrt($val);
	my $idx;
	my $fac;

	# try to factorize from the smallest prime
	for ($idx = 1; $idx <= $max_index && $val > 1; ++ $idx)  {
		$fac = $prime{$idx};
		last if ($fac > $upper);
		if (($val > $fac) && ($val % $fac == 0))  {
			$val = 1;
			last;
		}
	}
	# still cannot be factorized, should be a prime
	if ($val > 1)  {
		return 1;
	}
	return 0;
}

sub find_last_num($)
{
	my $f = shift;
	my $rollback_len = 32;

	open my $fh, "+>>", $f or die;
	my $end = tell($fh);	# get end pos of file

	seek $fh, $end-$rollback_len, 0;
	my $r = read($fh, my $buf, $rollback_len);
	print "r: $r\n";

	my $last_num = 0;
	while ( $buf =~ m/(\d{10})/g )  {
		$last_num = $1;
	}
	close $fh;
	print "last_num: $last_num\n";
	return $last_num;
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

	my $last_num = find_last_num("rr.txt");
	my $from = 1_000_000_000;
	my $to = 9_999_999_999;
	my $n;

	if ($last_num > $from)  {
		$n = $last_num + 2;
	} else  {
		$n = $from;
	}

	my $of = "rr.txt";
	open my $afh, ">>", $of or die;	# open for appending
	print "append to $of\n";
	my $c = 0;
	while (1)  {
		if ($n == 0 || $n > $to)  {
			last;
		}
		elsif (sqrt($n) > $max_prime)  {
			print "$n is too large, skip...\n";
			last;
		}
		if ( isprime($n) )  {
			print $afh $n,"\n";
			++ $c;
			if ($c && (($c % 10000)==0) )  {	# msg every 10K
				my $dd = `date +%c`;
				print "$c primes found: $n at $dd";
			}
		}
		$n += 2;
	}
	close $afh;
}

main;
