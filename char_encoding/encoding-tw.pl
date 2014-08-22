#!/usr/bin/perl
use lib '../../root/';
use Ericosur;

use Encode qw/encode decode/;

sub main()
{
	$utf8 = "中文abc";
	#$utf8 = "\x{fffeb48c}";

    print "utf8: $utf8\n";
    hexdump($utf8);
    sep();

    print "output big5 char...\n";
	$big5 = encode("big5", $utf8); # loads Encode::TW implicitly
	show($big5);
	hexdump($big5);
	sep();

    print "output big5 char again...\n";
	$utf8 = decode("big5", $big5); # ditto
	show($utf8);
	hexdump($utf8);
	sep();
}

main();
