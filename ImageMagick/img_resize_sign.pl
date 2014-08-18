#!/usr/bin/perl
#!/bin/perl

# need Image::Magick
# need exif

#
# resize specified jpeg files and extract exif and print
# onto the pictures
# maybe use Exif::Tool to retrieve the exif infomation
#
# 2006/12/27 by ericosur

use warnings;
use strict;
use Image::Magick;

sub image_process($);
sub gcd($$);
sub get_exif($);

# main procedure
# global defines
	my $inner_width = 1020;
	my $inner_height = 680;
	my $inner_size = $inner_width . 'x' . $inner_height;
	my $dst_width = 1080;
	my $dst_height = 720;
	my $dst_size = $dst_width . 'x' . $dst_height;
	my $quality = 70;

	# takes wildcard here
	if (@ARGV)  {
		foreach (@ARGV)  {
			if ( /\*|\?/ )  {			# if contains '*' or '?'
				#print "glob...'$_'\n";
				my @filelist = glob($_);
				foreach ( @filelist )  {
					image_process($_) if ( -f $_ );	# file only
				}
			}
			else  {		# without wildcard
				image_process($_) if ( -f $_ );
			}
		}
	}
	else  {
		print "no argument, usage: $0 [jpeg filename]\n";
	}
# end of main

#######################################################################
#
#
#
sub image_process($)
{
# local variables
	my $img_file = shift;
	my $rc;
	my $out_file = $img_file;

	$out_file =~ s[(.*?)\.jpg][$1_resized\.jpg]i;

	die "file [$img_file] is not found\n" unless -e $img_file;
	if ( -e $out_file )
	{
		print "$out_file existed, delete it\n";
		unlink $out_file;
	}

	my $img = Image::Magick->new();
	my $clone;
	$rc = $img->Set(quality => $quality,
			  		stroke => '#ffffff'
	);
	warn $rc if $rc;

	$rc = $img->Read($img_file);
	warn $rc if $rc;

	# get picture size
	my ($ww, $hh) = $img->Get('width', 'height');
#	printf "%s: %d x %d\n", $img_file, $ww, $hh;
	die "only landscape style pictures\n" if ($hh >= $ww);
	warn "source picture is smaller than output dimension\n" if ($ww < $dst_width || $hh < $dst_height);

	# get the ratio
#	my $gcd = gcd($ww, $hh);
#	$ww = $ww / $gcd;
#	$hh = $hh / $gcd;
#	printf "%s: %d x %d\n", $img_file, $ww, $hh;
	my $ratio = $ww / $hh;
	die "only 3:2 pictures\n" unless ($ratio > 1.45 && $ratio < 1.54);	# to capture 1.5

#	print $img_file, ' => ', $out_file;
	print $img_file, ': ';
	# resize
	$clone = $img->Clone();

	$rc = $clone->Scale(geometry => $inner_size);
	warn $rc if $rc;
	$rc = $img->Scale(geometry => $dst_size);
	warn $rc if $rc;
	$rc	= $img->Draw(
			primitive	=> 'color',
			method		=> 'filltoborder',
			points		=> '1, 1',
			bordercolor	=> 'red',
			fill		=> 'white');
	warn $rc if $rc;
	$rc = $img->Composite(
							image => $clone,
							x => ($dst_width - $inner_width) / 2,
							y => ($dst_height - $inner_height) / 2,
							compose => 'Over');
	warn $rc if $rc;

#	my $msg = 'Canon EOS 300D DIGITAL 1/20 sec. f/2.8';
	my $msg = get_exif($img_file);
# print exif info onto picture
	$rc = $img->Annotate(
				  text 		=> $msg,
				  font 		=> 'Arial-Bold',
				  fill		=> 'black',
				  geometry	=> '+15+710',
				  pointsize => 36);
	warn $rc if $rc;

# write to file
	$rc = $img->Write($out_file);
	warn $rc if $rc;
}

#
# gcd: greatest common divisor
#
sub gcd($$)
{
	my $a = shift;
	my $b = shift;
	my $t = 0;

	return 1 if (0 >= $a || 0 >= $b);

	while ($a != 0)  {
		$t = $b % $a;
		$b = $a;
		$a = $t;
	}

	return $b;
}

#
# get exif from specified JPEG
#
sub get_exif($)
{
	my $cmd = shift;

	$cmd = 'exif ' . $cmd;

	my $result = `$cmd`;
	my @lines = split /\n/, $result;
	my $fnumber;
	my $exposure;
	my $focal;
	my $flash = 0;
	my ($isorating, $model);

	$result = undef;
	foreach (@lines)
	{
		# Exposure Time
		if ( /^Exposure Time\s+\|(.*) sec./ )
		{
			$exposure = $1;
			$result .= $exposure . "s ";
		}
		# FNumber
		elsif ( /^FNumber\s+\|(.*?)\s+$/ )
		{
			$fnumber = $1;
			$result .= $fnumber . ' ';
		}
		# Focal Length
		elsif ( /^Focal Length\s+\|(.*?)\s+$/ )
		{
			$focal = $1;
			$result = $result . "\@" . $focal;
		}
		# ISO speed
		elsif ( /^ISO Speed Ratings\s+\|(\d+)\s+$/ )
		{
			$isorating = $1;
			$result .= 'ISO ' . $isorating;
		}
		# flash status
		elsif ( /^Flash\s+\|(\d+)\s+/ )
		{
			$flash = $1;
		}

		if ( /^Model\s+\|(.*?)\s+$/ )
		{
			$model = $1 ;
			$model =~ s/DIGITAL//i;
		}
	}
	$result .= " flash fired" if ($flash > 0);
	$result .= ' ' . $model if ($model);
	printf "%s\n", $result;
	return $result;
}
