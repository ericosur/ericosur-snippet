#!/usr/bin/perl

use strict;

my $file = "InstalledApps_-1.txt";

sub list_install_app($)
{
    my $f = shift;
    my $start = 0;
    my $flag = 0;
    my $cnt = 0;

    open my $fh, $f or die;

    while (<$fh>) {
        if ( m/USER applications/ ) {
            $start = 1;
            next;
        }
        if ($start) {
            if ( m/^([a-zA-Z \.\-0-9]+):/ ) {
                print;
                $flag = 1;
            } elsif ($flag == 1) {
                if ( m/^(\S+)/ ) {
                    print $1,"\n";
                    $cnt ++;
                }
                $flag = 0;
            }
        }
    }

    close $fh;
    print "cnt: $cnt\n";
}

sub main()
{
    list_install_app($file);
}

main;
