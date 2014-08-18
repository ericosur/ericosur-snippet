#!/usr/bin/perl
=pod

=head1 NAME

uqp.pl
translate B<quoted print> format into plain text format

=head1 USAGE

uqp.pl <infile> <outfile>

=head1 AUTHOR

Oct 11 2004 by ericosur

Mar 22 2008 fix a error if not binmode
=cut

use strict;
use warnings;

use MIME::QuotedPrint;

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

#print "$file_content\n";

my $tmp = decode_qp($file_content);

#print "$tmp\n";
print $out_fh "$tmp";

close $in_fh;
close $out_fh;
