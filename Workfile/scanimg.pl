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

my %imgfl = ();
my %basefl = ();
my $cnt = 0;
my $repfn = "report.csv";
my $rep_fh;
my $rep_cnt = 0;

sub scan_qml()
{
    chdir "../YOSE_GUI/YOSE_QML";
    my $qml_list = `find ./ -type f -iname '*.qml'`;
    my @arr = ();
    #print $qml_list;
    while ( $qml_list =~ m/(\S+)/g ) {
        push @arr, $1;
    }
    return @arr;
}

sub list_img_in_one_qml($)
{
    my $qml = shift;
    my $is_fn_shown = 0;
    my $show_stdout = 0;

    #print "[", $fn, "]\n";
    open my $fh, $qml or die;
    my $ln = 0;
    while (<$fh>) {
        $ln ++;
        while ( m/\"([^\"]+\.(jpg|png))\"/g ) {
            #print $_;
            my $ifn = $1;  # relative path + filename
            my $bfn = basename($ifn);    # only basename
            my $dn = dirname($ifn);
            #print "$ln: ", $1, "\n";
            $cnt ++;
            $imgfl{$ifn} ++;
            if ($basefl{$bfn} && $basefl{$bfn} ne $dn) {
                if ($show_stdout) {
                    if (not $is_fn_shown) {
                        print "in QML file: ", $qml, "\n";
                        $is_fn_shown = 1;
                    }
                    printf("duplicated? bfn: %s\n", $bfn);
                    printf("here path =========> %s\nrecorded path =====> %s\n", $dn, $basefl{$bfn});
                    print "\n";
                }

                my $rep = sprintf("\"%s\",\"%s\",\"%s\",\"%s\"\n", $qml, $bfn, $dn, $basefl{$bfn});
                #print $rep;
                print $rep_fh $rep;
                $rep_cnt ++;
            } else {
                $basefl{$bfn} = dirname($ifn);
            }

        }
    }
    close $fh;
    #print "cnt: ", $cnt, "\n";
    #print "len(\%imgfl) = ", (scalar keys(%imgfl)), "\n";
}

sub main()
{
    my @qml = ();
    @qml = scan_qml();
    open $rep_fh, "> $repfn" or die;
    foreach my $fn (@qml) {
        list_img_in_one_qml($fn);
    }
    close $rep_fh;
    printf("report count: %d\n", $rep_cnt);
}

main;
