#!/usr/bin/perl
#
# using ''openssl'' to determine a prime number
#

use strict;
use warnings;

my $ofile = "prime.txt";

my $lower = 994000;
my $upper = 994500;

# method 1
my @primes = qw(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59
	61 67 71 73 79 83 89 97);
# method 2
my $ifile = q(basic_prime.txt);
die "need $ifile\n" if not -e $ifile;
@primes = ();
open my $ifh, $ifile or die;
@primes = <$ifh>;
close $ifh;

#
# a silly sub to see whether the value is prime or not
#
sub is_basic_prime($)
{
	my $val = shift;
	my $sq = sqrt($val);

	foreach my $nn (@primes)  {
		if (($val % $nn == 0) && ($val != $nn))  {	# has factor?
			return 0;
		}
		last if ($nn > $sq);
	}

	return 1;
}

sub main
{
	my @array = ();
	my $cnt = 0;
	my $call_ssl_cnt = 0;
	my $ret;

	# using brute force to find primes between $lower to $upper
	LINE:
	for my $ii ($lower..$upper)  {
		if ( (is_basic_prime($ii) == 1) )  {
			if (sqrt($ii) > $primes[-1])  {
				# call 'openssl prime' for further checking
				$ret = `openssl prime $ii`;
				++ $call_ssl_cnt;
				next LINE if $ret =~ /not/;
			} else  {
				print '.';
			}
		}
		else  {
			next LINE;
		}
		print "$ii is prime\n";
		push @array, $ii;
		++ $cnt;
		print STDERR "$cnt\r";
	}
	printf "\nbetween %d to %d, there are %d primes\n", $lower, $upper, $cnt;
	print "openssl was called by $call_ssl_cnt times\n";

	open my $fh, "> $ofile" or die;
	print $fh join "\n", @array;
	close $fh;
	print "and output to $ofile\n";
}


main;
#my $num = 97;
#print is_prime_silly($num) ? "yes" : "no";
