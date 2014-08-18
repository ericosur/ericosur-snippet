#!/usr/bin/perl
require "charutil.pl";

my $ff = q(diff.txt);
open my $fh, $ff or die;
my $cnt = 0;
my $ofh = \*STDOUT;
binmode $ofh;

while (<$fh>)  {
	if (m/^>\s([0-9a-fA-F]{4})/)  {
		print $ofh $1, "\t";
		print $ofh charutil::write_char($1),"\n";
	}
}
close $fh;
