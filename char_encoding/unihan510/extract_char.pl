#!/usr/bin/perl
#
# extract big5 items from:
# http://www.unicode.org/Public/UNIDATA/Unihan.zip
#
# nonsense script, use ''grep kBigFive' to extract
# 13063 big5 han char (unicode 5.1.0)
#
# 2014/8/18 update: tested against unihan 7.0.0
# Unihan_OtherMappings.txt
# still works and will get same result
#

use strict;
use warnings;
use Compress::Zlib;

require "../charutil.pl";


# arg1: search tag
# arg2: input file name (in gzipped format)
# arg3: output file name
# arg4: true: output char, false: output hex number
sub proc($$$$)
{
    my ($tag, $iff, $off, $aschar) = @_;

    print "search for tag: $tag\n";
    print "input: $iff\n";
    print "output: $off\n";

    print "read data from $iff\n";
    my $gz = gzopen($iff, "rb")
         or (print "Cannot open $iff: $gzerrno\n"
            && next);

    open my $ofh, ">", $off or die;

    binmode $ofh;
    binmode STDERR;

    my $ccnt = 0;
    my $total = 0;

    while ($gz->gzreadline($_))  {
    	next if ( m/^#/ or m/^$/ );
    	++ $total;
    	s/\n//;
    	#last if $total > 500000;
    	#print STDERR;
    	if ( m/(.*)\t($tag)\t(.*)/ )  {
    		++ $ccnt;

    		my ($a, $b, $c) = ($1, $2, $3);
    		print $ofh $1, "\t", $3, "\t";
    		if ($aschar) {
    		    print $ofh charutil::write_char($3), "\n";
    		} else {
    		    print $ofh charutil::write_hex($3), "\n";
    		}
    	}
    	print STDERR "$ccnt / $total\r";
    }

    die "Error reading from $iff: $gzerrno\n"
        if $gzerrno != Z_STREAM_END ;

    $gz->gzclose() ;

    close $ofh;

    print STDERR "\n";
    print STDERR "ccnt = $ccnt\n";

}

sub main()
{
    # USE q(Unihan_OtherMappings.txt) FOR UNIHAN 7.0.0 data file
    # it is smaller and quick to parse
    my $ifile = q(../Unihan700/Unihan_OtherMappings.txt.gz);
    # Unihan510.txt is big and slower
    #my $ifile = q(Unihan510.txt);

    my $ofile = q(extract_big5.txt);
    my $bigfive_tag = 'kBigFive';
    proc($bigfive_tag, $ifile, $ofile, 1);

    my $gb0_tag = "kGB0";
    $ofile = q(extract_gb0.txt);
    proc($gb0_tag, $ifile, $ofile, 0);
}

main;
