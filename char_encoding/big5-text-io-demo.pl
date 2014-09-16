#!/usr/bin/perl
#
# the 3rd way to deal with "big5" file IO
#

use encoding 'big5', STDIN => 'big5', STDOUT => 'big5';
use open ":encoding(big5)";
use lib '../root/';
use Ericosur;

sub main()
{
	my $fh;

	open $fh, "data/big5.txt" or die "please run gen_big5.pl if you have no such data file";

	my @lines = <$fh>;
	my $whole = join '', @lines;

	show('whole', $whole);
	hexdump($whole);
	sep();

	close $fh;

	@words = split //, $whole;	# 中文字length會變成 1
	for my $xx (@words)
	{
		my $val = ord($xx);
		printf "%02x", $val;
		#print $xx;		# warning: wide character in print
		test_chr($xx) if $val > 31;
		print " ";
	}
	print "\n";
}

sub test_chr()
{
	no encoding;
	use Encode;

	my $foo = shift;
	my $bar = encode('big5', $foo);	# encode back to big5

	printf "(%s)", $bar;
}


main();
