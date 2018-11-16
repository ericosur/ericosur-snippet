#!/usr/bin/env perl
#

use strict;
#use utf8;

my $ipodlog_fn = 'ipod.log';
my $ipodsdk_fn = 'ipodsdk.log';
my $lhs_fn = '/tmp/lhs.log';
my $rhs_fn = '/tmp/rhs.log';
my $merged_fn = 'merged.log';

sub epoch_hhmmss($)
{
    my $tm = shift;
    my $epoch = 0;
    my $seconds = 0;
    if ( $tm =~ /(\d+):(\d+):(\d+)\.(\d+)/ ) {
        $seconds = (($1 * 60) + $2) * 60 + $3;
        $epoch = $seconds * 1000 + $4;
        #printf("%d  %d  %d  %d => %d\n", $1, $2, $3, $4, $epoch);
        return $epoch;
    } else {
        #print "??????";
        return 0;
    }
}


sub normalize_ipodlog($)
{
    my $fn = shift;
    if ( not -e $fn ) {
        printf(STDERR "=====> %s not found!\n", $fn);
        return;
    }
    print STDERR "=====> normalize $fn\n";

    open my $fh, $fn or die;
    #binmode($fh, ':encoding(utf8)');
    open my $ofh, "> $rhs_fn" or die;
    #binmode($ofh, ':encoding(utf8)');
    my $total = 0;
    my $match_cnt = 0;
    my $notmatch_cnt = 0;
    my $last_time = 5;
    while (<$fh>) {
        $total ++;
        s/[\r\n]//;
        my $line = $_;
        my $msg;
        if ( m/^\[(\S+)\](\[.*]\[.*\])/ ) {
            $match_cnt ++;
            my $t = epoch_hhmmss($1);
            $last_time = $t;
            $msg = sprintf("[%d][ipod] %s\n", $t, $line);
        } else {
            #printf("%s %s\n", $last_time, $_);
            $notmatch_cnt ++;
            $msg = sprintf("[%d][ipod] %s\n", $last_time, $line);
        }
        print $ofh $msg;
    }
    close $fh;
    close $ofh;

    # printf(STDERR "=====> ok lines: %d\nnot matched lines: %d\ntotal lines:%d\n",
    #        $match_cnt, $notmatch_cnt, $total);
    printf(STDERR "=====>    total lines: %d\n", $total);
}

sub normalize_sdklog($)
{
    my $fn = shift;
    if ( not -e $fn ) {
        printf("%s not found!\n", $fn);
        return;
    }
    print STDERR "=====> normalize $fn\n";

    open my $fh, $fn or die;
    #binmode($fh, ':encoding(utf8)');
    open my $ofh, "> $lhs_fn" or die;
    #binmode($ofh, ':encoding(utf8)');
    my $total = 0;
    my $match_cnt = 0;
    my $notmatch_cnt = 0;
    my $last_time = 1;
    my $msg;
    LOOP:
    while (<$fh>) {
        $total ++;
        s/[\0\r\n]//g;
        my $line = $_;
        if ( m/^$/ ) {
            next;
        }
        if ( m/^\d{2}-\d{2}\s+(\d+:\d+:\d+\.\d{3}):.:/ ) {
            $match_cnt ++;
            my $t = epoch_hhmmss($1);
            $last_time = $t;
            $msg = sprintf("[%d][sdk] %s\n", $t, $line);
        } else {
            #printf("=====> [%d] %s ===== %s\n", $total, $last_time, $_);
            $notmatch_cnt ++;
            $msg = sprintf("[%d][sdk] %s\n", $last_time, $line);
        }
        print $ofh $msg;
    }
    close $fh;
    close $ofh;

    # printf("=====>  ok lines: %d\nnot matched lines: %d\ntotal lines:%d\n",
    #        $match_cnt, $notmatch_cnt, $total);
    printf(STDERR "=====>    total lines: %d\n", $total);
}

sub read_log_into_array($)
{
    my $fn = shift;
    my @arr;
    open my $fh, $fn or die;
    while (<$fh>) {
        s/[\r\n]//;
        push @arr, $_;
    }
    close $fh;
    return @arr;
}

sub get_id($)
{
    my $ll = shift;
    if ( $ll =~ m/^\[(\d+)\]/ ) {
        return $1;
    } else {
        return 0;
    }
}

sub merge_log()
{
    my @lhs = read_log_into_array($lhs_fn);
    my @rhs = read_log_into_array($rhs_fn);
    my $cnt = 0;

    #print STDERR "size lhs:", scalar @lhs,"\n";
    #print STDERR "size rhs:", scalar @rhs,"\n";
    print STDERR "=====> output to merged.log\n";
    open my $ofh, "> $merged_fn" or die;
    #binmode($ofh, ':encoding(utf8)');

LOOP:
    # lhs is empty
    if ( scalar(@lhs) == 0) {
        #print STDERR "pop all rhs\n";
        while (@rhs) {
            print $ofh shift(@rhs), "\n";
            $cnt ++;
        }
        printf(STDERR "=====>  total lines: %d\n", $cnt);
        return;
    }
    # rhs is empty
    if ( scalar(@rhs) == 0) {
        #print STDERR "pop all lhs\n";
        while (@lhs) {
            print $ofh shift(@lhs), "\n";
            $cnt ++;
        }
        printf(STDERR "=====>  total lines: %d\n", $cnt);
        return;
    }

    #print STDERR "lhs:", scalar @lhs,"\t";
    #print STDERR "rhs:", scalar @rhs,"\n";

    my $ll = shift @lhs;
    my $rr = shift @rhs;
    my $lid = get_id($ll);
    my $rid = get_id($rr);

    if ( $lid > $rid ) {
        print $ofh $rr, "\n";
        unshift @lhs, $ll;
        $cnt ++;
    } else {
        print $ofh $ll, "\n";
        unshift @rhs, $rr;
        $cnt ++;
    }
    goto LOOP;
}

sub main()
{
    #binmode(STDOUT, ':encoding(utf8)');
    normalize_ipodlog($ipodlog_fn);
    normalize_sdklog($ipodsdk_fn);

    merge_log();
}

main();
