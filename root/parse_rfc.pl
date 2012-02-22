#!/usr/bin/perl
﻿use strict;
use warnings;


#
# todo: maybe I could use some module to access the excel file data cells directly
# thus I need not parse the text csv file
#
# the output result could be used at visgraphviz.com to generate relationship map

my $obs = "Obsoletes";
my $ups = "Updates";

my $file = "fuck.txt";	# this file is csv format

my $str;

# test string
#my $str = q(2048	"Obsoletes RFC1521, RFC1522, RFC1590, Obsoleted by RFC4288, RFC4289, Updated by RFC3023 updates RFC1234");

open FH, $file or die;

while (<FH>)
{
	$str = $_;

	$str =~ s/[\",]//g;	# eat " and ,
	$str =~ s/RFC//g;	# eat RFC
	$str =~ s/(?:$)/T/;	# append 'T' at the end

	$str =~ m/(\d+)\t(.*)/;
	my ($head, $tail) = ($1, $2);

#	printf "<%s>\n<%s>\n", $head, $tail;

	my @array = ();
	my $xx;

	if ( $tail =~ m/$obs\s+([\d\s]+)[A-Za-z]/i )
	{
#		printf "=>%s<=\n", $1;
		@array = split / /,$1;
		foreach $xx (@array)
		{
			printf "%s->%s [label=B]\n", $head, $xx;
		}
	}

#	print "-" x 40, "\n";
	@array = ();

	if ( $tail =~ m/$ups\s+([\d\s]+)[A-Za-z]/i )
	{
#		printf "=>%s<=\n", $1;
		@array = split / /,$1;
		foreach $xx (@array)
		{
			printf "%s->%s [label=U]\n", $head, $xx;
		}
	}

}	# while (<FH>)
