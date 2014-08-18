#!/usr/bin/perl

use Math::BigInt try => 'GMP';

my $debug = 0;

sub get_config($)
{
	my $ini = shift;
    print "get_config: $ini\n" if $debug;
    open my $fh, $ini or die;
    while ( <$fh> )  {
		next if /^$/;
		next if /^#/;
		s/\n//;
		eval($_);
		print "get_config: $_\n" if $debug;
    }
    close $fh;
}

sub doit()
{
	$ans = 0;
	$bb = Math::BigInt->new($nn);
	for (1 .. $repeat)  {
		$ans = $bb->bmodpow($pw, $mm);
	}
}

sub main()
{
	get_config('test.conf');

	doit();
}

main;
