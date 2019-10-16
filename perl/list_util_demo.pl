#!/usr/bin/perl
#
# list_util_demo.pl
#
# 2007/12/16 by ericosur


use List::Util qw(first max maxstr min minstr reduce shuffle sum);

my @list = qw{Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India
					Juliet Kilo Lima Mike November Oscar Papa Quebec Romeo
					Sierra Tango Uniform Victor Whiskey Xray Yankee Zulu};

show( maxstr @list );

my $sum = sum 1..100;
show($sum);

my $foo = reduce { $a gt $b ? $a : $b } 'A'..'Z';
show($foo);

sub show
{
	my $str = shift;
	print $str,"\n";
}

=pod

=head1 NAME

	list_util_demo.pl
	Demo for ''use List::Util"

=head1 DESCRIPTION

perldoc for List::Util
	http://perldoc.perl.org/List/Util.html

idea from: __Perl Best Practice__
	D.1. Recommended Core Modules

=cut
