#!/usr/bin/perl

#@ h2b.pl
#
# input text file like this
# 00 25 00 64 52 47 00 4d 00 4d
# and output the binary data
#
# Nov 21 2006
# changed to accept general hex string
#
# the line begin with ''#'' '':'' '';'' would be skipped
#

use strict;
use warnings;

sub process($$)
{
	my ($input_file, $output_file)  = @_;
	my $count = 0;
	my $byte_count = 0;
	my ($ifh, $ofh);

	# open input / output file
	if ($input_file eq '-')  {
		$ifh = \*STDIN;
		#print STDERR "read from STDIN\n";
	} else  {
		open($ifh, "<$input_file") or die "[$input_file] not exists";
		print "read from [$input_file]\n";
	}
	if ($output_file eq '-')  {
		$ofh = \*STDOUT;
		#print STDERR "output to STDOUT\n";
	} else  {
		open($ofh, ">$output_file") or die "[$output_file] canoot open for writing";
		print "write to [$output_file]\n";
	}
	binmode($ofh);

	while (<$ifh>)  {
		s/^\t//;
		s/[\r\n]//;
		next if /^[;#:]/;	# skip comment line
		$count ++;

		foreach (split /\s+/)  {
			# for debugging
			s/,//;
#			printf "(%s) = %d\n", $_, hex($_);
			++ $byte_count;
			print $ofh chr(hex($_));
			if ($ofh ne \*STDOUT)  {
				print STDERR "output byte: $byte_count\r";
			}
#			print STDOUT hex($_) . " ";
		}
	}
	print "\n";
	printf STDERR "total lines = $count\n";
	close $ofh;
	close $ifh;
}

# main procedure starts here
print STDERR "$0 <infile> <outfile>\n" if not @ARGV;
my $inf = $ARGV[0] || "h2b_data.txt";
my $outf = $ARGV[1] || "h2b_out.bin";
process($inf, $outf);
