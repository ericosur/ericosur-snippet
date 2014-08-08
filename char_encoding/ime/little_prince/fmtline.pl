#!/usr/bin/perl

use strict;
use warnings;

sub main()
{
    my $inf = $ARGV[0] // "birdgame.txt";
    my $outf = "outf.txt";

    if (-e $outf)  {
        unlink $outf;
    }

    print "inf: $inf\n";
    print "outf: $outf\n";

    open my $ifh, $inf or die;
    open my $ofh, "> $outf" or die;

    binmode($ifh, ":utf8");
    binmode($ofh, ":utf8");

    my $firstline = <$ifh>;
    print $ofh $firstline;

    my $cnt = 0;
    while (<$ifh>) {
#        print $ofh $_;
        s/[\r\n]//g;
        my @ar = split(//,$_);
        my $lar = scalar(@ar);
        my $cc;
        for (my $i = 0; $i < $lar; $i++) {
            $cc = $ar[$i];
            if ($cnt >= 18) {
                print $ofh "$cc\n";
                $cnt = 0;
            } else {
                print $ofh $cc;
                $cnt ++;
            }
        }
    }

    close $ifh;
    close $ofh;
}

main();

