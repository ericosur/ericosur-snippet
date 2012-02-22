#!/usr/bin/perl
=pod

=head1 NAME

alpha.pl - to translate characters into communication way

=head1 SYNOPSIS

alpha.pl B<string>

=begin html

The output would be:<br>

<hello>
Hotel   Echo    Lima    Lima    Oscar

=end html

=head1 DESCRIPTION

A stupid script translates input word into military communication
alpha table. It will output "Hello world" if no argument input.

2006/12/27 by ericosur
2007/12/05 by ericosur using hash table
2008/02/19 added warning and reviewed

=cut

use strict;
use warnings;
use Data::Dump qw(dump);

my @alpha_list = qw{Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India
					Juliet Kilo Lima Mike November Oscar Papa Quebec Romeo
					Sierra Tango Uniform Victor Whiskey Xray Yankee Zulu};

#
# input one character here
# look up from alpha_list table
#
sub show_alpha($)
{
	my $ch = uc(shift);
	return "undef" if length($ch) != 1;

	my $num = ord($ch) - ord('A');
	return ($num > 26 || $num < 0) ? "undef" : $alpha_list[$num];
}

sub main()
{
	my $str = $ARGV[0] || "Hello world";
	print "<$str>\n";

	my @result = ();
	@result = map { show_alpha($_) } split //,$str;
	dump(@result);
}

main;

