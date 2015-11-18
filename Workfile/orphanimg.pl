#!/usr/bin/env perl

#
# how to run:
# $ cd /src/gmui_git/yosemite/scripts
# $ perl scanimg.pl
#
# and report.csv will be generated at
# /src/gmui_git/yosemite/YOSE_GUI/YOSE_QML
#
# may use 'excel' or text editor to open it
#

use strict;
use File::Basename qw(dirname basename);

my $TOP = "/src/gmui_git/yosemite/";
my %qrcfl = ();
my %imgfl = ();

my $cnt = 0;
my $repfn = "report.csv";
my $rep_fh;
my $rep_cnt = 0;

sub find_qml()
{
    chdir $TOP;
    chdir "YOSE_GUI/YOSE_QML/";
    my $qml_list = `find ./ -type f -iname '*.qml'`;
    my @arr = ();
    #print $qml_list;
    while ( $qml_list =~ m/(\S+)/g ) {
        push @arr, $1;
    }
    return @arr;
}

sub find_qrc()
{
    chdir $TOP;
    chdir "YOSE_GUI/";
    my $qml_list = `find ./ -type f -iname '*.qrc'`;
    my @arr = ();
    #print $qml_list;
    while ( $qml_list =~ m/(\S+)/g ) {
        #print "qrc: ", $1, "\n";
        push @arr, $1;
    }
    return @arr;
}

sub list_img_in_one_qml($)
{
    my $qml = shift;
    my $is_fn_shown = 0;
    my $show_stdout = 0;

    #print "[", $qml, "]\n";
    open my $fh, $qml or die;
    my $ln = 0;
    while (<$fh>) {
        $ln ++;
        while ( m/\"([^\"]+\.(jpg|png))\"/g ) {
            #print $_;
            my $ifn = $1;  # relative path + filename
            $ifn =~ s/\.\.\///;
            #my $bfn = basename($ifn);    # only basename
            #my $dn = dirname($ifn);
            #print "$ln: ", $1, "\n";
            $cnt ++;
            $imgfl{$ifn} ++;
        }
    }
    close $fh;
    #print "cnt: ", $cnt, "\n";
    #print "len(\%imgfl) = ", (scalar keys(%imgfl)), "\n";
}

sub process_qrc($)
{
    my $fn = shift;
    my $cnt = 0;
    open my $ifh, $fn or die;
    while (<$ifh>) {
        $cnt ++;
        if ( m/<file>(.+)<\/file>/) {
            my $ff = $1;
            $ff =~ s/YOSE_QML\///;
            if ( $ff =~ m/\.(jpg|png)/ ) {
                if ($qrcfl{$ff}) {
                    print "why ?", $ff, "\n";
                } else {
                    $qrcfl{$ff} ++;
                }
            }
            #print "=====>", $1, "<=====\n";

        }
        # if ($cnt > 10) {
        #     last;
        # }
    }
    close $ifh;
}

sub main()
{
    my @qml = ();
    @qml = find_qml();
    foreach my $fn (@qml) {
        list_img_in_one_qml($fn);
    }

    my @qrc = ();
    @qrc = find_qrc();
    foreach my $f (@qrc) {
        #print $f,"\n";
        process_qrc($f);
    }

    my $ofh;

    # list all images record in qml
    print "imgfl:\n";
    print "imgfl size: ", scalar(keys(%imgfl)), "\n";
    print "output to imgfl.txt";
    open $ofh, "> imgfl.txt" or die;
    foreach my $ii (sort keys %imgfl) {
        print $ofh  $ii,"\n";
    }
    close $ofh;

    print "#" x 80,"\n";

    # list all images record in qrc
    print "qrcfl:\n";
    print "qrcfl size: ", scalar(keys(%qrcfl)), "\n";
    print "output to qrcfl.txt";
    open $ofh, "> qrcfl.txt" or die;
    foreach my $jj (sort keys %qrcfl) {
        print $ofh  $jj,"\n";
    }
    close $ofh;

    print "=" x 60, "\n";
    my @diff = diff_of_array(keys(%imgfl),keys(%qrcfl));
    print "diff size: ", scalar(keys(@diff));
    open $ofh, "> diff.txt" or die;
    print "-" x 20, "\n";
    foreach my $dd (@diff) {
        #list_img_in_one_qml($dd);
        print $ofh  $dd,"\n";
    }
    print "-" x 20, "\n";
    close $ofh;
}

main;

sub diff_of_array(@@)
{
    my (@thumb, @large) = @_;

    my @union = ();
    my @intersection = ();
    my @difference = ();
    my %count = ();
    my $element;

    foreach $element (@thumb, @large)  {
        $count{$element}++;
    }
    foreach $element (keys %count)  {
        push @union, $element;
        push @{ $count{$element} > 1 ? \@intersection : \@difference }, $element;
    }
    return @difference;
}
