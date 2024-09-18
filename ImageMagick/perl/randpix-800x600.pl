#!/usr/bin/perl

use strict;
use warnings;

use Image::Magick;
#use Text::Lorem;

#my @ext = qw(png gif jpg tif pict tga xpm wbmp sgi tga);
#my @ext = qw(png gif jpg);
my @ext = qw(jpg);
my $pix_fname = 'tmp';
my $maxx = 800;
my $maxy = 600;
my $debug = 0;

=pod
sub get_randomtext()
{
	my $text = Text::Lorem->new();
	my $result = $text->words(3);

	print $result,"\n" if $debug;
	return $result;
}
=cut

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

for (1..2)  {
	$rc = $im->Draw(
		primitive => 'circle',
		#stroke	 => 'red',
		filled => get_random_color(),
		strokewidth => 4,
		points => get_random_coord()
	);
	warn $rc if $rc;
}

#	$rc = $im->Annotate(
#		x => 20,
#		y => 40,
#		font => 'Lucida-Console',
#		#stroke	 => 'yellow',
#		filled => get_random_color(),
#		pointsize  => 24,
#		text => get_randomtext()
#	);
#	warn $rc if $rc;

	$rc = $im->Annotate(
		x => 20,
		y => 70,
		font => 'Aroa;',
		#stroke	 => 'blue',
		filled => get_random_color(),
		pointsize  => 20,
		text => get_date()
	);
	warn $rc if $rc;

	$rc = $im->Annotate(
		x => 15,
		y => $maxy - 25,
		font => 'Aroa;',
		#stroke	 => 'yellow',
		filled => get_random_color(),
		pointsize  => 20,
		text => "by ImageMagick"
	);
	warn $rc if $rc;

	$rc = $im->Annotate(
		x => ($maxx - 24 * length($pix_name)) / 2,
		y => $maxy / 2 - 40,
		font => 'Arial',
		#stroke	 => 'yellow',
		filled => get_random_color(),
		pointsize  => 64,
		text => $pix_name,
		align => 'center'
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
for my $n (1..1000)  {
	for my $ee (@ext)  {
		$file = sprintf "rand_%04d.%s", $n, $ee;
		draw($file);
		print "$file\n";
	}
}
