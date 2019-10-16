#!/usr/bin/perl
#
# 2006/12/27 by ericosur
#

#
# a wrapper script to process ARGV and then call get_exif
#
# wildcards supported
#

use strict;
use warnings;

require "get_exif.pl";

if (@ARGV)  {
	foreach (@ARGV)  {
		if ( /\*|\?/ )  {			# if contains '*' or '?'
			#print "glob...'$_'\n";
			my @filelist = glob($_);
			foreach ( @filelist )  {
				Rasmus::get_exif($_) if ( -f $_ );	# file only
			}
		}
		else  {		# without wildcard
			Rasmus::get_exif($_);
		}
	}
}
else  {
	print "no argument\n";
}
