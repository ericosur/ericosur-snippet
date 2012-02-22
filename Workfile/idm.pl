#!/usr/bin/perl
#
# This script helps me to rename images in modis repository with
# incorrect file extension. For example, many ''pbm'' files are
# actually ''bmp'' files
#
# support wildcard, file list
#

use strict;
use warnings;
use Image::Magick;

my $count = 0;	# total processed files count
my $bmp_count = 0;	# windows bitmap files count

sub main();
sub process($);
sub get_filename_from_list($);
sub is_windows_bmp($);

# total, bmp, gif, jpeg, png, unknown
my %count = ();

sub id($)
{
	my $im = Image::Magick->new();
	my $file = shift;

	print $file,"\n";
	my (undef, undef, undef, $fmt) = $im->Ping($file);

	return $fmt;
}


sub main()
{
	if (@ARGV)  {
		foreach (@ARGV)  {
			if ( /\*|\?/ )  {			# if contains '*' or '?'
				#print "glob...'$_'\n";
				my @filelist = glob($_);
				foreach ( @filelist )  {
					process($_) if ( -f $_ );	# file only
				}
			}
			elsif ( /@/ ) {
				s/@//;
				get_filename_from_list($_);
			}
			else  {		# without wildcard
				process($_);
			}
		}
		# show the result
		foreach (keys %count)  {
			printf "%s => %s\n", $_, $count{$_};
		}
#		printf "%d bitmap files, %d files checked\n", $bmp_count, $count;
	}
	else  {
	    print <<EOL;
By inspecting magic number in the head of image files to guess the file type
EOL

		printf "\n%s <filename> [\@list file] [filenames...] \n", $0;
	}
}

sub rename_file($$)
{
	my $ifile = shift;
	my $ext = shift;
	my $ofile = $ifile;

	$ext = lc($ext);
	$ofile =~ s/(.*)\.(\w+)$/$1\.$ext/;
	rename $ifile, $ofile;
}

# just take one argument and print it out
sub process($)
{
	my $file = shift;
#	print "$file: ";

	# only files are accepted
	if (-f $file)  {
		++ $count{total};
		my $ext = id($file);
		# rename the file name
		rename_file($file, $ext);
	}
}


sub get_filename_from_list($)
{
	my $list_file = shift;

	open FH, $list_file or die;
	while (<FH>)
	{
		s/[\r\n]//;
		#print $_;
		process($_);
	}
	close FH;
}


main();
