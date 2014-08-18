#!/usr/bin/perl
#
# an easy percent decoding translation example
#
# so could the quote-print do
#
# NOTICE: this script should be store as UTF8 format

use strict;
use warnings;

use Encode qw(from_to);

sub dec_str($)
{
	my $r = shift;

	$r =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	return $r;
}

sub enc_str($)
{
	my $r = shift;

	#from_to($string, "Shift_JIS", "GB2312");
	$r =~ s/(\W)/sprintf("%%%02X",unpack("C",$1))/eg;

	return $r;	# it is UTF8
}

sub main()
{
	my $r;

	#$r = "%e4%bc%91%e9%96%92";	# 休閒 in utf-8
	$r = "許蓋功";	#" notice this script should be store as UTF8 format

	$r = enc_str($r);
	printf "enc_str = %s\n", $r;
	print '-' x 30, "\n";

	$r = dec_str($r);
	printf "(utf-8) dec_str = %s\n", $r;

	from_to($r, "UTF-8", "big5");
	printf "(big5) dec_str = %s\n", $r;
}

main;
