#!/usr/bin/perl

=pod

=head1 NOTE

external app ''exif'' is required application
use it to get info from images

=cut


use warnings;
use strict;

sub process($);
sub get_filename_from_list($);
sub get_exif($);


#####################################################################
# process command line file names and wildcards
sub main()
{
if (@ARGV)  {
	foreach (@ARGV)  {
		#
		# wildcards file names
		#
		if ( /\*|\?/ )		# if contains '*' or '?'
		{
			#print "glob...'$_'\n";
			my @filelist = glob($_);
			foreach ( @filelist )
			{
				process($_) if ( -f $_ );	# file only
			}
		}
		#
		# file list from command line
		#
		elsif ( /@/ ) {
			s/@//;
			get_filename_from_list($_);
		}
		#
		# file names from command line without wildcards
		#
		else
		{
			process($_) if ( -f $_ );
		}
	}
}
else
{
	print "no argument\nUsage: $0 <filenames>\n";
}
}

#####################################################################
sub process($)
{
	get_exif($_);
}
#####################################################################
sub get_filename_from_list($)
{
	my $list_file = shift;

	open FH, $list_file or die;

	while (<FH>)
	{
		s/\r//;
		s/\n//;

		process($_);
	}

	close FH;
}
#####################################################################
sub get_exif($)
{
	my $file = shift;

	unless (-f $file)  {
		warn "no such file";
		return;
	}

	my $cmd = 'exif ' . $file;
	my $result = `$cmd`;
	#print $result;
	my @lines = split /\n/, $result;
	my $fnumber;
	my $exposure;
	my $focal;
	my $flash = 0;

	$result = "";
	foreach (@lines)  {
		#print $_, "\n";
		# Exposure Time
		if ( /^Exposure Time\s+\|(.*) sec./ )  {
			$exposure = $1;
#			print "<$exposure>";
			$result .= $exposure . "s ";
		}
		# FNumber
		elsif ( /^FNumber\s+\|(.*?)\s+$/ )  {
			$fnumber = $1;
#			print "<$fnumber>";
			$result .= $fnumber . ' ';
		}
		# Focal Length        |35.0 mm
		elsif ( /^Focal Length\s+\|(.*?)\s+$/ )  {
			$focal = $1;
#			print "<$focal>";
			$result = $result . '@' . $focal;
		}
		# flash status
		elsif ( /^Flash\s+\|(\d+)\s+/ )  {
			$flash = $1;
#			print "<$flash>";
		}
	}

	if ($flash > 0)  {
		$result .= " flash fired";
	}

	print $file, "\t", $result, "\n";

	return $result;
}

main;

