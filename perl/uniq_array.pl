#!/usr/bin/perl
#
# uniq_array.pl
#

use strict;

sub uniq(@)
{
	my %seen = ();
	my @result = grep { ! $seen{$_} ++ } @_;
	return @result;
}

sub uniq_sort(@)
{
	my %seen = ();
	my %seen = map { $_ => 1 } @_;
	my @result = sort keys %seen;
	return @result;
}

sub main
{
	my @test = qw(email mms sms smil cm ems sms);

	print "original data =>\n";
	print join("\t", @test), "\n";

	my @dup = uniq(@test);
	print "uniq(@test) =>\n";
	print join("\t", @dup), "\n";

	my @dup2 = uniq_sort(@test);
	print "uniq_sort(@test) =>\n";
	print join("\t", @dup2), "\n";
}

main;

=pod

=head1 NAME

uniq_array.pl

=head1 SYNOPSIS

Run C<uniq_array.pl> to see the result.
Provide B<uniq()> and B<uniq_sort()>.

=head1 NOTE

A simple demo how to unique an array.
C<uniq()> makes a unique array, and C<uniq_sort()> makes
a unique and sorted array.

=cut
