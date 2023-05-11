#!/usr/bin/perl

use strict;

sub check_file($)
{
    my $f = shift;
    open my $cfh, $f or die;
    while (<$cfh>) {
        s/[\r\n]//;
        if ( m!/usr/bin/python/! ) {
            printf("%s\n", $f);
        } 
    }
    close($cfh);
}

my $file = 'exec-py.txt';
open my $fh, $file or die;

while (<$fh>) {
	s/[\r\n]//;
    my $f = $_;
    check_file($f);
}

close($fh);

