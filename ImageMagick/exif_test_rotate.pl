#!/usr/bin/perl

#
#  use Image::Exiftool to check the image width/height whether match
#  the auto rotate / orientation info in the EXIF
#
# 2007/10/30 by ericosur

use Image::ExifTool qw(:Public);

my $file = 'list.txt';
my $verbose = 1;

open FH, $file or die "file list needed\n";

print "\@echo off\n";
print "rem brutely rotated image list:\n";

while (<FH>)
{
	s/\r//;
	s/\n//;
	process($_);
}

close FH;



sub process($)
{
	my $file = $_;
	my $result1 = 0;
	my $result2 = 0;
	my $total_file = 0;
	my $found_file = 0;

#    printf "%s:\n", $_ if $verbose == 1;

    get_info($file);

#	$result1 = get_orientation($file);
#	$result2 = get_image_size($file);

#	if ($result1 == 1 && $result2 == 1)
#	{
#		my $cmd = sprintf "exiftool -exiftool -Orientation=Horizontal \"%s\"", $file;

#		print $cmd, "\n";
#		system $cmd;
#	}
}


sub get_info()
{
	my $img_file = shift;
	my $exif = new Image::ExifTool;
	my $info = $exif->ImageInfo($img_file);
	my $is_rotate = 0;
	my $is_potrait = 0;

# to know the picture is potrait or landscape
	my $img_size = strize($$info{'ImageSize'}), "\n";
	if ($img_size =~ /(\d+)x(\d+)/)
	{
		my $mm = $1;
		my $nn = $2;
		$is_potrait = 1 if ($mm < $nn);
#		printf "potrait: %d\n", $is_potrait;
	}

# rotate info
	my $rotate = strize($$info{'Orientation'});
	$is_rotate = 1 if ($rotate =~ /rotate/i);
#	printf "rotate: %d\n", $is_rotate;


	printf "%s\n", $img_file if ($is_rotate && $is_potrait);

	my $result = $exif->SetFileModifyDate($file);
	print "time/date set" if $result;
	$exif->WriteInfo();

#
#	show_all_exif($info);
#
	undef $exif;
	undef $info;
}

sub strize($)
{
	my $val = shift;
	if (ref $val eq 'ARRAY')
	{
		$val = join(', ', @$val);
	}
	elsif (ref $val eq 'SCALAR')
	{
		$val = '(Binary data)';
	}
	return $val;
}

sub show_all_exif()
{
	my $info = shift;

	foreach (keys %$info)
	{
	    my $val = strize($$info{$_});
	    printf("%-24s : %s\n", $_, $val);
	}
}


sub get_orientation($)
{
	my $img_file = $_;
	my $is_rotate = 0;

	if ( -f $img_file )
	{
		my $info = ImageInfo($img_file);
		my ($orient, $rotate) = (
			$$info{'Orientation'},
			$$info{'AutoRotate'},
		);

		if ( $orient =~ /rotate/i )
		{
			$is_rotate = 1;
		}

		if ($verbose == 1)
		{
			print $orient;
			print "\t", $rotate if $rotate;
			print "\n";
		}
	}
	return $is_rotate;
}


#
# use Image::Magick to get the dimension of image file
#
sub get_image_size($)
{
	my $img_file = $_;
	my $result = 0;

	if (-f $img_file)
	{
		my $im = Image::Magick->new();

		if ( -f $img_file )
		{
			my ($width, $height) = $im->Ping($img_file);
			printf "%d, %d\n", $width, $height if $verbose == 1;
			if ($width < $height)
			{
				$result = 1;
			}
		}
		undef $im;
	}
	return $result;
}
