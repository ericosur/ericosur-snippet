#!/usr/bin/perl

#@ h2b.pl
#@ parse comneon resource file (cpp) into binary data
#@ for testing making ffs bitmap loading
#
# Nov 21 2006
# changed to accept general hex string
#

use strict;
use warnings;


# @ARGV = ('-') unless @ARGV;
die "$0 <infile> <outfile>\n" unless @ARGV;

process(@ARGV);


sub process {
	my $input_file = $ARGV[0];
	shift @ARGV;
	my $output_file = $ARGV[0];
	my $count = 0;
	my $byte_count = 0;

	print "read from [$input_file]\n";
	print "write to [$output_file]\n";

	# open input / output file
	open(INFILE, "<$input_file") or die "[$input_file] not exists";
	open(OUTFILE, ">$output_file") or die "[$output_file] canoot open for writing";
	binmode(OUTFILE);

	while (<INFILE>)
	{

#		if ( /\s*[0-9a-fA-F].*\s+[0-9a-fA-F].*/ )
#		{
			print ".";
			$count ++;
			s/^\t//;
			s/\r//;
			s/\n//;
			my @array = split /,\s{0,}/;

			foreach (@array)
			{
				s/\s+//;
				s/,//;
				#printf "(%s) = %d\n", $_, hex($_);
				print OUTFILE chr(hex($_));
				$byte_count++;
#				print STDOUT hex($_) . " ";
			}
			#print "\n";
#		}
	}

	close OUTFILE;
	close INFILE;
	printf "total lines = %d\ntotal bytes = %d\n", $count, $byte_count;
}
