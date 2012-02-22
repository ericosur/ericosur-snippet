#!/usr/bin/perl
use strict;
use warnings;

#use utf8;

use Encode qw/encode decode/;
# decode mime header encoding from/to stdin/stdout

print STDERR "decode mime header encoding from/to stdin/stdout\n";
my $str = <> || "=?big5?Q?=B9q=A4l=B9=EF=B1b=B3=E6=A4U=B8=FC=B3q=AA=BE?=";
my $dec_str = decode('MIME-Header', $str);

my $ofh = \*STDOUT;
binmode $ofh;

printf $ofh "%s\n", $dec_str,"\n";	# it will croak if using print

close $ofh;
