#!/usr/bin/perl

use strict;
use warnings;
use v5.10;

=pod

http://en.wikipedia.org/wiki/Collatz_conjecture

f(n)=
n/2 if n===0 (mod 2)
3n+1 if n===1 (mod 2)

=cut

my $cnt = 0;

sub f($);

sub f($)
{
	my $n = shift;

	++ $cnt;
	return 1 if $n == 1;

	if ($n % 2)  {
		$n = $n * 3 + 1;
	}
	else  {
		$n = $n / 2;
	}
	say $n;
	f($n);
	return $n;
}

=pod
    function collatz(n)
        while n > 1
            show n
            if n is odd then
                set n = 3n + 1
            else
                set n = n / 2
            endif
        endwhile
    show n
=cut

sub collatz($)
{
	my $n = shift;
	while ($n > 1)  {
		say $n;
		if ($n % 2 ==  1)  {
			$n = 3 * $n + 1;
		}
		else  {
			$n = $n / 2;
		}
	}
	say $n;
}

sub main()
{
	my $nn = $ARGV[0] || 99;
	f($nn);
	say "cnt = $cnt";

	collatz($nn);
}

main;
