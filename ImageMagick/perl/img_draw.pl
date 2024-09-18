#!/usr/bin/perl
#
# Image::Magick
# test recipes
#
# 2007/11/15 by ericosur

use Image::Magick;

my $jpg_file = "TEST.JPG";

if (not -f $jpg_file)
{
	print "please prepare a jpeg file ($jpg_file) for testing\n";
	exit 0;
}


#my $im = Image::Magick->new(size => '400x300');
my $im = Image::Magick->new();

$im->Read($jpg_file);
$im->Set(stroke => 'black');

$im->Draw(primitive => 'rectangle',
		  points	=> '0,129 199,169',
		  fill		=> 'blue',
		  stroke	=> 'blue');

$im->Draw(primitive => 'polygon',
		  points	=> '199,149 399,74 324,149 399,224',
		  fill		=> 'yellow',
		  stroke	=> 'black');

$im->Set(antialias => 0, fuzz => 15);
$im->Draw(primitive 	=> 'circle',
		  strokewidth 	=> 3,
		  points		=> '199,149 74,149');
$im->Draw(primitive		=> 'ellipse',
		  strokewidth	=> 3,
		  points		=> '199,149 50,100 0,360');

$im->Draw(primitive		=> 'color',
		  method		=> 'filltoborder',
		  points		=> '99,149',
		  bordercolor	=> 'red',
		  fill			=> 'green1');

$im->Draw(primitive => 'rectangle',
		  points	=> '0,0 399,299');

$im->Draw(primitive => 'line',
		  points	=> '199,0 199,299');
$im->Draw(primitive => 'line',
		  points	=> '0,149 399,149');
$im->Draw(primitive => 'line',
		  points	=> '20,0 20,299');
$im->Draw(primitive => 'line',
		  points	=> '0,50 399,50');

$rc = $im->Annotate(
			x		=> 20,
			y		=> 20,
			text	=> 'powered by Image::Magick');
warn $rc if $rc;
$rc = $im->Annotate(
			  text 		=> 'Green Text',
			  font 		=> 'Century',
			  fill		=> 'yellow',
			  geometry	=> '+20+50',
			  pointsize => 48);
warn $rc if $rc;
$rc = $im->Draw(
			primitive	=> 'Text',
		  	points		=> '10,99 "Other String"');
warn $rc if $rc;
# $im->Read('label: New Image');

my $pix = $jpg_file;
$im->Write($pix);

system("start $pix");

=pod

=head1 NAME

img_draw.pl

=head1 DESCRIPTION

Test demo for Image::Magick. This script would produce an image by
using Image::Magick api. The output file is defined at C<$jpg_file>

=cut
