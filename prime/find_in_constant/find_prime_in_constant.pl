#!/usr/bin/perl
#
# 找出在 pi 或是 e 小數點後連續十位數字是質數
# 需要 e/pi 以及質數的資料檔
#
# also refer to:
# https://www.hanshq.net/eprime.html
#

use strict;
use warnings;
use Storable;
use Getopt::Std;

my $store_file = "prime.dat";
my $e_file = 'loge_giga.txt';	# e
my $pi_file = 'pi_giga_digits.txt';	# pi
my $CHECKLEN = 10;
my $debug = 0;

my %prime = ();
my $max_index = 0;
my $max_prime = 2;
my $last_pos = 0;

sub check_digits($)
{
	my $buf = shift;
	my $len = length($buf);
	my $sp = 0;
	my $check;
	my $ch_len;

	while (1)  {
		$check = substr($buf, $sp, $CHECKLEN);
		++ $sp;
		$ch_len = length($check);
		last if ($ch_len != $CHECKLEN);

		#print $check,"\n" if $debug;
		if ( substr($check, $ch_len-1, 1) =~ m/[24680]/ )  {
			#print "e" if $debug;
			next;
		}
		if ( isprime($check) )  {
			return $check;
		}
	}
	return 0;
}

sub load_largefile($)
{
	my $file = shift;
	print "check digits from: ", $file, "\n";
	open my $ifh, $file or die;

	my $buf_size = 1024;
	my $fpos = 0;
	my $buf;
	my $flag = 0;
	my $c = 0;
	my $rr = 0;

	while (1)  {
		my $real_read = read $ifh, $buf, $buf_size;
		++ $c;
		if ($real_read < $buf_size)  {
			$flag = 1;
		}

		$rr = check_digits($buf);
		last if $rr != 0;

		last if $flag == 1;
		$fpos = $fpos + $real_read - 9;
		print "move to ", $fpos,"\n";
		seek $ifh, $fpos, 0;
		#last if $c > 2;
	}
	$last_pos = tell $ifh;
	close $ifh;

	return $rr;
}

sub load_prime_table()
{
	# 100K 的質數表，可以協助判別到 9,999,999,999 的數字沒有問題
	my $plain_file = "prime_100k.txt";	# prime_(100k|1M).txt
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

	# process line argument and settings
	my %opts = ();
	my $load_file;
	getopts("el:", \%opts);
	$load_file = ( $opts{e} ? $e_file : $pi_file );

	my $rr = load_largefile($load_file);
	print "result prime: ", $rr, "\n";
	#print "last pos: ", $last_pos,"\n";
}

main;

=pod

=head1 NOTE

To determine the 10 consequenced digits from e and pi is
prime or not, we need a table with 8500 prime (87553), and
pi/e table with 1024 digits. The answer shows up not far
away the beginning.

=cut

