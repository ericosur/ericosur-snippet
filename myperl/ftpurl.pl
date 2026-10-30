#!/usr/bin/perl
# -- Jul 14 1998 by Eric
# generate script for bitftp...

# Of course you can turn 'use' statements off
use strict;
use vars qw($input $host $path $file);

print "please enter a FTP URL: ";
$input = <STDIN>;
#$input = "ftp://ftp.notexist.com.tw/pub/newfiles/readme.txt";

if ( $input =~ m[^ftp://([^/\s]+)/(?:(.*)/)?([^/\s]+)\s*$] ) {
    $host = $1;
    $path = defined $2 ? $2 : '.';
    $file = $3;
}
else {
    die "cannot parse your input\n";
}

print STDOUT <<EOF
open $host
user anonymous
bin
cd $path
get $file
close
EOF
