#!/usr/bin/perl

use strict;
use v5.10;

sub show($)
{
    my $rarr = shift;
    foreach (@$rarr) {
        print "$_,";
    }
	say;
}

sub test()
{
	my $i;
	#my @kk = qw(a b c d e);
	my @vv = qw(apple ball cat duck egg);

	#show(\@vv);
	say "map function test...";
	# if statement as:
	# $_ = '[' . $_ . ']'
	# the @vv would be changed as well
	my @addpoint = map { 
		'[' . $_ . ']'	# would not chage @vv
	} @vv;
	say "show addpoint...";
	show(\@addpoint);
	#show(\@vv);

	say "map as hash...";
	# in perl, substr could be lvalue
	my %hash = map {
		substr($_, 0, 1) => '<' . $_ . '>';
	} @vv;
	while ( my ($k,$v) = each(%hash) ) {
		say "$k => $v";
	}
}

test();

