#!/usr/bin/perl
#
# extract big5 items from:
# http://www.unicode.org/Public/UNIDATA/Unihan.zip
#
# nonsense script, use ''grep kBigFive' to extract
# 13063 big5 han char (unicode 5.1.0)

use strict;
use warnings;

require "../charutil.pl";

sub main()
{
    my $bigfive_tag = 'kBigFive';
    my $ifile = q(Unihan510.txt);
    my $ofile = q(extract_big5.txt);

    print "input: $ifile\n";
    print "output: $ofile\n";

    open my $ifh, "<:utf8", $ifile or die;
    open my $ofh, ">", $ofile or die;

    binmode $ofh;
    binmode STDERR;

    my $big5 = 0;
    my $total = 0;

    while (<$ifh>)  {
    	next if ( m/^#/ or m/^$/ );
    	++ $total;
    	s/\n//;
    	#last if $total > 500000;
    	#print STDERR;
    	if ( m/(.*)\t($bigfive_tag)\t(.*)/ )  {
    		++ $big5;

    		my ($a, $b, $c) = ($1, $2, $3);
    		print $ofh $1, "\t", $3, "\t";
    		print $ofh charutil::write_char($3),"\n";
    	}
    	print STDERR "$big5 / $total\r";
    }

    close $ifh;
    close $ofh;

    print STDERR "\n";
    print STDERR "big5 = $big5\n";
}

main;
