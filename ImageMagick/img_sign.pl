#!/usr/bin/perl
#
# Mar 13 2007 by ericosur
#
# use package Image::Magick and Image::ExifTool
#
# img_sign.pl <wildcard>
# or
# img_sign.pl @filelist.txt
#
#
# $write_operation would control the 'read' write operation

use strict;
use warnings;

use Image::Magick;
use Image::ExifTool qw(:Public);

sub get_filename_from_list($);
sub process($);

my $write_operation = 0;	# turn off the write operation


if ($write_operation == 0)
{
	print STDERR "no write operation taken\n";
}

# process command line file names and wildcards
if (@ARGV)
{
	foreach (@ARGV)
	{
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
else  {
	print "no file(s) specified\n";
}

#############################################################################
sub process($)
{
	my $param = shift;
	my $result;

	$result = make_notation($param);
	printf STDERR "%s: %s\n", $param, $result;

	if ($write_operation != 0)
	{
		sign_image($param, $result);
	}
}
#############################################################################
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
#############################################################################
#
# arg1: file name
# arg2: the string would be annoted to the bottom of image
#
#
sub sign_image($$)
{
	my $img_file = shift;
	my $im = Image::Magick->new();

	my $annotation_text = shift;
	my $fontsize = 80;

	if ( not -f $img_file )
	{
		printf STDERR "%s not found, exit\n", $img_file;
		return;
	}

	my $rc = $im->Read($img_file);
	die "Cannot read $img_file: $rc" if $rc;

	my ($ww, $hh) = $im->Get('width', 'height');

	#printf "%s: %d, %d\n", $img_file, $ww, $hh;
	my $geom = sprintf "+20+%d", $hh - 40;

	$im->Set(stroke => '#ffffff');


	$rc = $im->Annotate(
				  text 		 => $annotation_text,
				  font 		 => 'Lucida-Console',
				  fill		 => 'white',
				  stroke	 => 'yellow',
				  undercolor => 'black',
				  geometry	 => $geom,
				  pointsize  => $fontsize);
	warn $rc if $rc;

	my $pix = make_filename($img_file);

#	if ( -f $pix )
#	{
#		print "old file exists, not overwirte\n";
#	}
#	else
#	{
		$im->Write($pix);
#	}

	undef $im;

#	system("start $pix");
}

#############################################################################
#
# append postfix to file name
#
sub make_filename($)
{
	my $file = shift;
	my $result;

	s/\r//;
	s/\n//;

	if ( /(.*)\.(.*)/ )
	{
		$result = sprintf "%s_sign.%s", $1, $2;
	}

	return $result;
}

#############################################################################
#
# get exif from image and return the result string
#
#
sub make_notation($)
{
	my $img_file = shift;
	my $info = ImageInfo($img_file);
	my $str;
	my ($model, $lens, $apert, $expos, $focal, $iso) = (
		$$info{'Model'},
		$$info{'Lens'},
		$$info{'Aperture'},
		$$info{'ExposureTime'},
		$$info{'FocalLength'},
		$$info{'ISO'}
	);

	my $expcomp = $$info{'ExposureCompensation'};

	$model =~ s/ DIGITAL//;
	$model =~ s/ *$//g;
	$lens =~ s/ //g;

	if ($lens eq undef)
	{
		$str = sprintf "%s F%s %ss @%s",
			$model, $apert, $expos, $focal;
		if ($iso ne undef)
		{
			$str = $str . ' ISO' . $iso;
		}

	}
	else	# for my DSLR
	{
		$str = sprintf "%s %s F%s %ss @%s ISO%s",
			$model, $lens, $apert, $expos, $focal, $iso;
		if ($expcomp ne '0')
		{
			$str = $str . ' ' . $expcomp . 'ev';
		}
	}

	#print STDERR $str, "\n";
	return $str;
}
