#!/usr/bin/perl
# factor.pl

use strict;

my @primes;

my $ifile = q(basic_prime.txt);
die "need $ifile\n" if not -e $ifile;
@primes = ();
open my $ifh, $ifile or die;
while (<$ifh>)  {
	s/[\r\n]//;
	push @primes, $_;
}
close $ifh;

my @factor = ();
my %ff = ();
my $cnt = 0;

sub factorize($)
{
	my $val = shift;
#	my $sq = sqrt($val);

	if ($val <= 1)  {
		return;
	}
	++ $cnt;
	print ">>>>>>> $cnt, arg=$val\n";

	foreach my $nn (@primes)  {
		if ($val == $nn)  {
			return;
		}
		if (($val % $nn) == 0)  {
			push @factor, $nn;
			++ $ff{$nn};
			#print $val," / ", $nn,"\n";
			$val = $val / $nn;
			#print $val,"\n";
			if ($val != 1)  {
				print "factorize($val) >>>\n";
				factorize($val);
			}
		}
	}
}


factorize(100);

print '-' x 40,"\n";
foreach my $kk (keys %ff)  {
	printf "%d ^ %d\n", $kk, $ff{$kk};
}
