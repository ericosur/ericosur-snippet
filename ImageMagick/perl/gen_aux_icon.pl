#!/usr/bin/perl

use strict;
use warnings;

use Image::Magick;

#my @ext = qw(png gif jpg tif pict tga xpm wbmp sgi tga);
my @ext = qw(png);
my $pix_fname = 'tmp';
my $maxx = 50;
my $maxy = 50;
my $debug = 0;

sub get_randomtext()
{
	my $text = Text::Lorem->new();
	my $result = $text->words(3);

	print $result,"\n" if $debug;
	return $result;
}

sub get_date()
{
	my ($sec,$min,$hour,$mday,$mon,$year,undef,undef,undef) = localtime;
	my $date = sprintf "%02d-%02d-%02d %02d:%02d:%02d",
		($year-100), $mon + 1, $mday, $hour, $min, $sec;
	#print "$date\n";
	return $date;
}

sub get_random_coord()
{
	my $coordinate = sprintf("%d,%d %d,%d",
		int(rand($maxx*2/3)+40), int(rand($maxy*2/3)+40),
		int(rand($maxx*1/4)), int(rand($maxy*1/4)),
	);
	print $coordinate,"\n" if $debug;
	return $coordinate;
}

sub get_random_color()
{
	my $color = sprintf("#%02x%02x%02x",
		int(rand(255)), int(rand(255)), int(rand(255))
	);
	print "color = $color\n" if $debug;
	return $color;
}

sub get_pix_name()
{
	my $maxidx = scalar @ext;
	my $str = sprintf "%s.%s", $pix_fname, $ext[int(rand($maxidx))];

	print $str;
	return $str;
}

sub draw($)
{
	my $im = Image::Magick->new(size => "$maxx x $maxy");
	my $rc;
	my $pix_name = shift;

	$rc = $im->Read('xc:black');
	warn $rc if $rc;

	$rc = $im->Annotate(
		x => 2,
		y => 30,
		font => 'Lucida-Console',
		#stroke	 => 'lightgrey',
		fill => 'lightgrey',
		pointsize  => 24,
		text => "AUX"
	);
	warn $rc if $rc;

	$im->Write($pix_name);
}

#
#
# main procedure starts here
#
#
my $file;
my $n = 1;
for (@ext)  {
	$file = "tmp$n." . $_;
	$file = sprintf("randpix_%d.%s", $n, $_);
	draw($file);
	print "$file\n";
}
