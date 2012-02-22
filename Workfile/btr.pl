#!/usr/bin/perl

# make my code beautiful
# 2005-03-04 by ericosur

#
# add space after the following keywords:
# if, for, while, switch
# and '//'
# trim the trailing space
#
# Mar 14 2005 by rasmus init version
# Mar 16 2005 by rasmus change // comment processing
#

#@ usage:
#@ btr.pl <filename.ext>
#@
#@ the original file would be filename.ext.bak
#@

use strict;
use warnings;

sub read_and_write($$);

my $file;
my $outfile;

if ($ARGV[0])
{
	$file = $ARGV[0];
	$outfile = $file . ".tmp";
	read_and_write($file, $outfile);
}
else
{
	print "please specify the filename";
}


sub read_and_write($$)
{
	my $in_file = shift;
	my $out_file = shift;
	my $line_num = 0;

	open FH, "< $in_file" or die "cannot open $!\n";
	open OFH, "> $out_file" or die "cannot write $!\n";

	while (<FH>)
	{
		$line_num ++;

		s[if\(][if \(];
		s[for\(][for \(];
		s[}while][} while];
		s[while\(][while \(];
		s[switch\(][switch \(];

		# //xxx => // xxx
		s((?<!:)//(\S+))(// $1)g;	#s[\/\/(\S+)][\/\/ $1];

		# trailing spaces
		s[\s+\n$][\n];

		print OFH $_;
	}

	close FH;
	close OFH;

	rename $in_file, $in_file . ".bak";
	rename $out_file, $in_file;
}
