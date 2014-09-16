#!/usr/bin/perl

#
# this text file is encoding as UTF-8
#

use strict;
use warnings;
use Encode qw(from_to);

sub shex($)
{
	# %#02x or %02x
	print join(" ", map { sprintf "%02x", $_ }
		unpack('W*', shift));
}

sub main()
{
    binmode STDOUT;

    # 許蓋功 (BIG5 encoding)
    print "big5 encoding: ";
    my $str = pack('H12', "b35cbb5ca55c");
    shex($str);
    print "\n";
    print $str,"\n";

    #from_to($string, "Shift_JIS", "GB2312");

    print "utf8 encoding: ";
    from_to($str, "BIG5", "UTF8");
    shex($str);
    print "\n";
    print $str,"\n";

    print "gb2312 encoding: ";
    from_to($str, "UTF8", "GBK");
    shex($str);
    print "\n";
    print $str,"\n";

    #
    # pack("CCC",0xef,0xbb,0xbf); ==> EF BB BF
    # pack("H6", "EFBBBF") ==> EF BB BF
    #
}

main;
