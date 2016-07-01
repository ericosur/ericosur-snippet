#!/usr/bin/perl

# useless ?

use strict;
use Unicode::String qw(utf8 latin1 utf16);
use utf8;
use v5.10;


# http://blog.wu-boy.com/2009/07/perl-with-utf-8-mode/

sub test_string($)
{
	my $a = shift;
	printf "length = %d\n", length($a);

	for (my $i = 0; $i < length($a); $i++)  {
		printf "%x ", ord(substr($a, $i, 1));
	}
	print "\n";

	say "[$a] is utf8? ", utf8::is_utf8($a) ? "yes" : "no";
}

sub main()
{
    binmode(STDIN, ':encoding(utf8)');
    binmode(STDOUT, ':encoding(utf8)');
    binmode(STDERR, ':encoding(utf8)');

	my $a = "abc";
	test_string($a);
	$a = "許蓋功";
	test_string($a);
}

main;

