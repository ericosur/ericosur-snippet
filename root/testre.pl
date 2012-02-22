#!/usr/bin/perl
#@ test RE
#
# 2006/12/27 by ericosur

use strict;
use warnings;

sub match_line($);
sub match_part($$);
sub replace_line($);

my $ifile = $ARGV[0] || "ifile.txt";
my $ofile = $ARGV[1] || "ofile.txt";
my $re;
my $line_num = 0;
my $match_count = 0;
my ($ifh, $ofh) = ();

	if ($ifile eq '-')  {
		$ifh = \*STDIN;
	}
	else  {
		open $ifh, $ifile or die;
	}

	if ($ofile eq '-')  {
		$ofh = \*STDOUT;
	}
	else  {
		open $ofh, "> $ofile" or die;
	}

	print STDERR "please input RE for matching in [$file]:\n";
	$re = <STDIN>;
	chomp $re;
	print STDERR '-' x 60 . "\n";

FILE: while ( <FH> )
	{
		$line_num ++;

		s/\r\n//g;
		match_line($_);
		#replace_line($_);
	}

	my $msg = "\n$match_count lines matched.\n";
#	print STDERR $msg;
#	print OFH $msg;

	close FH;
	close OFH;



########################################################################
#
#
#

sub match_line($)
{
#	print "match_line(): $_";

	if ( m($re) )
	{
		my $local_line = $_;

		s[($re)][``$1``];
		print OFH "$line_num:($1): $_";
		#print OFH "$1\n" if ($1);
		$match_count ++;

		$local_line =~ s[($re)][];
		match_part($local_line, $re);
	}
}

sub match_part($$)
{
	my $pline = shift;
	my $pre = shift;

	$pline =~ s/\r//;
	$pline =~ s/\n//;

#	if (not length($pline))
#	{
#		return;
#	}

	if ( $pline =~ m($pre) )
	{
		my $tmp = $pline;

		$pline =~ s[($pre)][``$1``];
		print OFH "($1): $pline\n";

		$tmp =~ s[($re)][];
		match_part($tmp, $pre);
	}
}

# this is a test function
sub replace_line($)
{
	#s([^:]//(\S+).*$)(// $1);
	#s[\/\/(\S+)][\/\/ $1];

	s((?<!:)//(\S+))(// $1)g;

	print OFH $_;
}
