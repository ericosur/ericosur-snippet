#!/usr/bin/env perl

use strict;
my $file = $ARGV[0] // die "need specify ts file";
print STDERR $file,"\n";

open my $fh, $file or die;
while (<$fh>) {
	if (m/type=\"unfinished\"/) {
        s/ type=\"unfinished\"//;
        print;
    } else {
        print;
    }
}
close $fh;

