#!/usr/bin/perl
#!/bin/perl

# demo how to use sprintf in the s/ ... / ... / regex
#
# 2006/12/27 by ericosur

use strict;
use warnings;


while ( <DATA> )	# demo data from __DATA__ section
{
#	if ( m/^([a-zA-z]*?),\s*(\d+)/ )
#	{
#		print $1, $2, "\n";
#	}

	# number in the 2nd field will be sqrt'ed and multiple by 10
	s{
		^\s*([a-zA-z]*?),\s*(\d+[.\d]*)
	}
	{
		sprintf "%10s,\t%.2f,\t(%.2f)", $1, sqrt($2)*10.0, $2
	}xe;
	print $_;
}

# not used any more, move to this subroutine
sub generate_data_file()
{
	# make a data file for demo
	open FILE, "> $file" or die;

	print FILE <<EOF;
Raymond, 43.25, basketball
Alice, 34.5, eating apple
Catherine, 53, watching movies
Bobu, 26.9, body building
EOF

	close FILE;
}

__DATA__;
Raymond, 43.25, basketball
Alice, 34.5, eating apple
Catherine, 53, watching movies
Bobu, 26.9, body building
