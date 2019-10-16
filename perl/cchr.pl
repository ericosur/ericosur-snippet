#!/usr/bin/perl
=pod

=head1 NOTE

To count the repeat time of each character.

reference from ptt.cc
=cut

$str = q(aaaagggddeedkdkdkslsllllaxjdjslaald);

# ¯}Ãa©Ê
$_ = $str;
printf "count a = %d\n", $cnt = tr/a//;

# «D¯}Ãa©Ê
my %cnt = ();
$cnt{$_}++ for split //, $str;
printf "count g = %d\n", $cnt{'g'};
# list all
foreach my $kk (sort keys %cnt)  {
	printf "%s: %d\n", $kk, $cnt{$kk};
}
