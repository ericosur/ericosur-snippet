#!/usr/bin/perl

=pod

To grep p-values colume from sts result file.
As SP800-22rev1a.pdf section 4.2.2 described, count p-values as 0.1/0.2/...
as ten groups. To know if these p-values are uniform distribution.

If it is uniform distribution, all values would be near 18.8.


=cut

use strict;
use v5.10;

my $file = 'finalAnalysisReport.txt';

sub show($)
{
	my $rfa = shift;
	foreach (@$rfa) {
		say $_;
	}
}

sub mysillychi($$)
{
	my $ref = shift;
	my $total = shift;

	my @o = @$ref;
	my @e = ();

	for (my $i=0; $i<scalar(@o); $i++) {
		$e[$i] = $total / scalar(@o);
	}
	say "expect: ";
	show(\@e);
	say "observed: ";
	show(\@o);

	my $chisq = 0.0;
	for (my $j=0; $j<scalar(@o); $j++) {
		my $tmp = (($o[$j] - $e[$j])**2) / $e[$j];
		say $tmp;
		$chisq += $tmp;
	}
	say "chisq: $chisq";
}

sub main()
{
	my @arr = qw(0 0 0 0 0 0 0 0 0 0);
	my $cnt = 0;

# 92 119  99 104 108  82  99  93  94 110  0.337688    993/1000    Frequency
	open my $fh, $file or die;
	while (<$fh>) {
		s/[\r\n]//;
		if ( m/^[\s\d]+(0\.\d{6})/ ) {
			$cnt ++;
			my $val = $1;
			$val *= 10;
			$arr[$val] += 1;
		}
	}
	close $fh;

#	say "cnt: $cnt";
#	show(\@arr);

	mysillychi(\@arr, $cnt);
}

main;

=pod

example output:

15
20
18
19
18
20
22
21
17
18

I use "CHITEST()" in excel, against 18.8 series, get 0.991468.

=cut
