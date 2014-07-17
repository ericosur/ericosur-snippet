#!/usr/bin/perl

use strict;
use File::Basename;

my $fl = "filelist.txt";

sub open_flist($)
{
    my $flist = shift;
    open my $fh, $flist or die;
    while (<$fh>) {
        s/[\r\n]//g;
        my $ff = $_;
        printf("check_file: %s\n", basename($ff));
        #check_file($ff);
    }
    close $fh;
    #printf("%d files checked\n", $cnt);
}

sub main()
{
    open_flist($fl);
}

main;
