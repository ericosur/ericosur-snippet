#!/usr/bin/env perl

use strict;
use warnings;

use 5.010;
use Perl6::Junction qw(all);
use Data::Dump qw(dump);

sub load_file($)
{
	my $vebose = 0;
	my $file = shift;
	my %prime_factor = ();

	open my $fh, $file or die;
	while ( <$fh> )  {
		my $ln = $_;
		$ln =~ s/[\r\n]//;
		print $ln,"\t" if $vebose;
		while ( m/(\d+) \^ (\d+)/g )  {
			print "<$1>\t" if $vebose;
			$prime_factor{$1} ++;
		}
		print "\n" if $vebose;
	}
	close $fh;
	return %prime_factor;
}

# only list the number of which factors are all larger than ''$condition''
# I notice that every number has a prime factor < 100. (no-sense)
# Because 100*100=10000, here all numbers < 10000. Only primes have factors 
# more than 100. 
sub show_large_factor($)
{
	my $file = shift;
	my $condition = 50;
	my ($num,$fac) = (0,0);
	my @fcs;
	my $match_cnt = 0;

	open my $fh, $file or die;
	while ( <$fh> )  {
		my $ln = $_;
		@fcs = ();

		$ln =~ s/[\r\n]//;	# remove new line
		$ln =~ s/\^ \d+//g;	# remove power of factor
		$ln =~ s/\s+//g;	# remove spaces
		#say $ln;
		$ln =~ m/^(\d+)=(.*)/;
		$num = $1;
		$fac = $2;
		@fcs = split /\*/,$fac;
		#dump(@fcs);
		if ( all(@fcs) > 50 )  {
			$match_cnt ++;
			say $num,":",join('*',@fcs);
		}		
	}
	say "matched num: $match_cnt";
	close $fh;
}

sub main()
{
=pod
	my %pf = ();
	%pf = load_file('not_prime.txt');
	
	foreach my $kk (sort {$a <=> $b} keys %pf)  {
		print "$kk >>> $pf{$kk}\n";
	}
=cut
	show_large_factor('not_prime.txt');
}

main;

