#!/usr/bin/perl
use strict;
use warnings;

use Encode;
use lib 'd:/ericosur-google';
use Ericosur;

sub shex($)
{
	print join(" ", map { sprintf "%#02x", $_ }
		unpack('W*', shift));
}

sub main()
{
	my $fh;
	open $fh, "big5.txt" or die;
	#binmode $fh;

	my @data = <$fh>;
	my $whole = join '', @data;

	close $fh;

	my $copy = $whole;
	hexdump($copy);
	sep();
	$copy = $whole;
	chn_dump($copy);
	sep();
}

sub chn_dump()
{
	my $foo = shift;

	printf "len: %d, foo: %s\n", length($foo), $foo;

	my $dec = decode('big5', $foo);
	printf "after decode big5 =>\nlen: %d, dec: %s\n", length($dec), $dec;

	print "and then split by char =>\n";
	my @words = split //, $dec; # 中文字算是一個字元，所以會被切開
	for my $xx (@words)	# now $xx is unicode char
	{
		printf "%02x ", ord($xx);
	}
	print "\n";
	sep();

	# 切回去之前的模式，中文字兩個字元
	print "map encode big5 =>\n";
	map {$foo = encode('big5', $foo)} @words;
	printf "len: %d, foo: %s\n", length($foo), $foo;
	sep();

	#hexdump($foo);
	shex($foo);
}

main();
