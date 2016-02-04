#!/usr/bin/env perl

#
# script to print last commits in one week for each repo
#

use strict;
use Time::Local;

my $one_week_sec = 7 * 24 * 60 * 60;

sub date_distance($$$$$$)
{
    my ($YYYY, $MM, $DD, $hh, $mm, $ss) = @_;
    my $current_time = time();
    #printf("%d %d %d  %d %d %d\n", $ss,$mm,$hh,$DD,$MM-1,$YYYY);
    my $input_time = timelocal($ss,$mm,$hh,$DD,$MM-1,$YYYY);
    #print "time: ", $input_time, "\n";
    if ( abs($input_time - $current_time) < $one_week_sec ) {
        return 1;
    } else {
        return 0;
    }
}

sub main()
{
    my $file = "/tmp/repo_commits.txt";

    my $cmd = sprintf("repo forall -p -c ten > %s", $file);
    system $cmd;

    my @block = ();
    my $has_content = 0;

    open my $fh, $file or die;
    while (<$fh>) {
        my $ln = $_;

        if (m/^project/) {
            if ($has_content) {
                foreach (@block) {
                    print $_;
                }
                print "\n";
                @block = ();
                $has_content = 0;
            } else {
                @block = ();
            }

            push @block, $ln;

        } elsif ( m/^$/ ) {
            #print;
        } elsif ( m/(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})/ ) {
            # 2016-01-20 23:15:37
            my ($YYYY, $MM, $DD, $hh, $mm, $ss) = ($1, $2, $3, $4, $5, $6);
            #printf("y:%d, m:%d, d:%d h:%d m:%d s:%d\n", $YYYY, $MM, $DD, $hh, $mm, $ss);
            if ( date_distance($YYYY, $MM, $DD, $hh, $mm, $ss) ) {
                $has_content = 1;
                #print $ln;
                push @block, $ln;
            }
        }
    }
    close $fh;
    unlink $file;
}

main;
