#!/usr/bin/env perl

#
# mygrep will remove some messy lines from original main.txt
#

use strict;
use utf8;
use Storable;
use JSON;

sub read_config($)
{
    my $jsonf = shift;
    my $json_text;

    open my $fh, $jsonf or die;
    while (<$fh>) {
        $json_text = $json_text . $_;
    }
    close($fh);
    #print $jsontext;

    my $hash = from_json($json_text);
    my $ifile = $hash->{'common'}->{'ifile'};
    my $ofile = $hash->{'common'}->{'ofile'};
    my $datafile = $hash->{'common'}->{'datafile'};

    printf("read_config:\nifile:%s\nofile:%s\ndatafile:%s\n",$ifile, $ofile, $datafile);

    return ($ifile, $ofile, $datafile);
}

sub process($$$)
{
    my $ifile = shift;
    my $ofile = shift;
    my $datafile = shift;

    open my $fh, $ifile or die "$ifile not found";
    binmode($fh, ':encoding(utf8)');
    open my $ofh, "> $ofile" or die;
    binmode($ofh, ':encoding(utf8)');
    my $cnt = 0;
    my $total = 0;
    my %hash = ();
    #printf("ifile:%s\nofile:%s\n", $ifile, $ofile);

    LOOP:
    while (<$fh>) {
        #s/[\r\n]//;
        $total ++;
        if ( m/^[0-9a-zA-Z]+/ ) {
            next LOOP;
        }
        if ( m/^[一二三四五六七八九○１２３４５６７８９]+/ ) {
            next LOOP;
        }
        if ( length($_) > 4 ) {
            next LOOP;
        }

        $cnt ++;
        print $ofh $_;

        s/[\r\n]//;
        $hash{$_} = 1;
    }

    close $fh;
    close $ofh;

    #printf("outfile cnt: %d\n", $cnt);

    my @arr = keys(%hash);
    $cnt = scalar(@arr);
    printf("total: %d\nfiltered out: %d\nkept: %d\n", $total, $cnt, ($total-$cnt));
    store(\@arr, $datafile);
    #printf("data file stored: %s\n", $datafile);
}

sub main()
{
    my ($ifile, $ofile, $datafile) = read_config('setting.json');
    #printf("if: %s\nof: %s\ndf: %s\n", $ifile, $ofile, $datafile);
    process($ifile, $ofile, $datafile);
}

main();
