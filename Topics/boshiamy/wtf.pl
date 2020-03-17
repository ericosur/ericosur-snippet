#!/usr/bin/perl
#
use strict;

while (<DATA>) {
    s/[\r\n]//;
    if ( m/^\w+:\s+(\d+)/ ) {
        printf("%x\n", $1);
    }
}

__DATA__
missing: 131205
missing: 139304
missing: 139305
missing: 173783
missing: 173784
missing: 173785
missing: 173786
missing: 173787
missing: 173788
missing: 173789
missing: 173790
missing: 173791
