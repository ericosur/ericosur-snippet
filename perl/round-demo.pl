#!/usr/bin/perl
#
# round-demo.pl
#

use strict;
use warnings;

use Math::Round qw(:all);

#
# reference from: http://www.perl.com/doc/FAQs/FAQ/oldfaq-html/Q4.13.html
# Does perl have a round function? What about ceil() and floor()?
#
sub foo_round($)
{
    my($number) = shift;
#    return int($number + .5);	# buggy if the input is negative
    return int($number + .5 * ($number <=> 0));
}

sub show($)
{
	my $val = shift;
	printf "%.1f => %.1f\t%.1f\n", $val, round($val), foo_round($val);
}

sub main()
{
	my @foo = qw(2.4 2.5 -2.4 -2.5);

	foreach my $nn (@foo)  {
		show($nn);
	}
}

main();

=pod

=head1 NAME

round-demo.pl

=head1 SYNOPSIS

round-demo.pl

=head1 DESCRIPTION

Demo the usage of "Math::Round".

=cut
