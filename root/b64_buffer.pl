#!/usr/bin/perl
=pod

=head1 NAME

b64_buffer.pl

=head1 NOTE

Use cyclic block to encode input file to C<Base64> format.
=cut

use strict;
use warnings;
use MIME::Base64;

my ($infile, $outfile) = @ARGV;
die "b64.pl <infile> <outfile>\n" unless ($infile && $outfile);

printf "infile = [%s], outfile = [%s]\n", $infile, $outfile;

open INFILE, "< $infile" or die "open error\n";
open OUTFILE, "> $outfile" or die "write error\n";

binmode INFILE;

my $ret;
my $buf;
my $bufsize = 5700;		# need to be multiple of 57, 57/6*8 = 76
my $tmp;
my $cnt = 0;

while ( 1 )  {
	$ret = read(INFILE, $buf, $bufsize);
#	printf "ret = %d\n", $ret;

	last if ($ret eq 0);
	$tmp = encode_base64($buf);

	#print "$tmp\n";
	print OUTFILE "$tmp";

	$cnt += $ret;
	print "$cnt\r";
}

#print "$file_content\n";
print "\n";

close INFILE;
close OUTFILE;


__END__
