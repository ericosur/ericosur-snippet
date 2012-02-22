#!/usr/bin/perl
#!/bin/perl

# rotate specified jpg Clockwise
#
# 2006/12/27 by ericosur

use strict;
use warnings;

use Image::Magick;

sub RotateCW($);

if (@ARGV)  {
	foreach (@ARGV)  {
		if ( /\*|\?/ )  {			# if contains '*' or '?'
			#print "glob...'$_'\n";
			my @filelist = glob($_);
			foreach ( @filelist )  {
				RotateCW($_) if ( -f $_ );	# file only
			}
		}
		else  {		# without wildcard
			RotateCW($_);
		}
	}
}
else  {
	print "no argument\n";
}


# just take one argument and print it out
sub RotateCW($)
{
	my $in_file = shift;
	my $out_file = $in_file;

	$out_file =~ s/(.*?)\.(.*)/$1_ccw.$2/i;

	my $img;
	my $rc;
	@$img = ();

	printf "%s => %s\n", $in_file, $out_file;

	$img = Image::Magick->new();
	$rc = $img->Read($in_file);
	warn $rc if $rc;

	$rc = $img->Rotate(degrees => -90);
	warn $rc if $rc;

	$rc = $img->Write($out_file);
	warn $rc if $rc;
}
