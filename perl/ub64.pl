#!/usr/bin/perl
=pod

=head1 NAME

b64.pl

=head1 DESCRIPTION

translate input file into output file as C<BASE64> format

=head1 USAGE

usage: b64.pl <infile> <outfile>

=head1 NOTE

no good if the input file is very large
please refer to another version: ''b64_buffer.pl''

Oct 11 2004 by ericosur

=cut

use strict;
use warnings;

use MIME::Base64;

my ($infile, $outfile) = @ARGV;
my $in_fh;
my $out_fh;

print STDERR "$0 <infile> <outfile>\nUse STDIN/STDOUT if not specified\n";

if ($infile)  {
	open $in_fh, "< $infile" or die "open error\n";
	print STDERR "input from $infile\n";
}
else  {
	$in_fh = \*STDIN;
	print STDERR "take input from STDIN\n";
}

if ($outfile)  {
	open $out_fh, "> $outfile" or die "write error\n";
	print STDERR "output to $outfile\n";
}
else  {
	$out_fh = \*STDOUT;
	print STDERR "output to STDOUT\n";
}

binmode $in_fh;

my $file_content;
# I thought it is a stupid way to read whole content into a scalar
while ( <$in_fh> )
{
	$file_content = $file_content . $_;
}

print STDERR "==> $file_content\n";

my $tmp = decode_base64($file_content);

#print "$tmp\n";
print $out_fh "$tmp";

close $in_fh;
close $out_fh;

