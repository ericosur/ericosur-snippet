#!/usr/bin/perl

use strict;
use Getopt::Std;

sub help()
{
    print<<EOL;
perl readable_time.pl <options>

    -a android android_unixtime
    -u unix time
    -h this message and sample

EOL
}

sub get_readtime($)
{
    my $ut = shift;
    my $rt = localtime($ut);
    return $rt;
}

sub main()
{
    my %opts = ();
    getopt("auh", \%opts);

    # adb shell getprop ro.runtime.firstboot in milli second
    #my $android_unixtime = 1368525096398;
    #my $readtime = localtime($android_unixtime/1000);
    #printf("unix: %s\nlocal: %s\n", $android_unixtime, $readtime);

    my $ut;
    if ($opts{'a'}) {
        $ut = $opts{'a'};
        printf("android epoch: %s\nreadable_time: %s\n", $ut, get_readtime($ut/1000));
        #return;
    }
    if ($opts{'u'}) {
        $ut = $opts{'u'};
        printf("   unix epoch: %s\nreadable_time: %s\n", $ut, get_readtime($ut));
    } elsif (not @ARGV || $opts{'h'}) {
        help();
    }
}

main;
