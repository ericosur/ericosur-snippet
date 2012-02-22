#!/usr/bin/perl
use Encode;
use lib 'd:/ericosur-google';
use Ericosur;


sub main()
{
	my $lines = "¿é¤Jªº¬Outf8";

	show('parse_big5()');
	parse_big5($lines);
	sep();
	show('parse_utf8()');
	parse_utf8($lines);
}

sub parse_big5()
{
	my $lines = shift;
	my $big5 = "[\xA1-\xF9][\x40-\x7E\xA1-\xFE]";
	my @words = $lines=~/($big5|\x0d\x0a|[\x21-\x7e]|\s+)/g;

	for my $xx (@words)
	{
		#my $bar = encode('big5', $xx);
		#print '(', $bar, ')';
		print '(', $xx, ')';
	}
	print "\n";
}

sub parse_utf8()
{
	use Unicode::String qw(utf8);

	my $lines = shift;
	my $foo = utf8($lines);

	print length($foo), "=>", $foo, "\n";
	my @words = split //, $foo;
	for my $yy (@words)
	{
		print "(", $yy, ")";
	}
	print "\n";
}


main();
