#!/usr/bin/perl

use strict;
use warnings;

use Image::Magick;

#my @ext = qw(png gif jpg tif pict tga xpm wbmp sgi tga);
my @ext = qw(jpg);
my $pix_fname = 'tmp';
my $debug = 0;

sub get_date()
{
	my ($sec,$min,$hour,$mday,$mon,$year,undef,undef,undef) = localtime;
	my $date = sprintf "%02d-%02d-%02d %02d:%02d:%02d",
		($year-100), $mon + 1, $mday, $hour, $min, $sec;
	#print "$date\n";
	return $date;
}

sub get_random_color()
{
	my $color = sprintf("#%02x%02x%02x",
		int(rand(255)), int(rand(255)), int(rand(255))
	);
	print "color = $color\n" if $debug;
	return $color;
}

sub draw($$)
{
	my $im = Image::Magick->new;
	my ($pix_name, $count) = @_;

	my $rc = $im->Read($pix_name);
	warn $rc if $rc;

	my ($maxx, $maxy) = $im->Get('width', 'height');

	my $str = sprintf "%04d", $count;
	$rc = $im->Annotate(
		x => $maxx/2,
		y => 100,
		font => 'Arial',
		stroke	 => 'yellow',
		filled => 'yellow',
		pointsize  => 99,
		text => $str,
		align => 'center'
	);
	warn $rc if $rc;

	my $new_name = sprintf "rand_%04d.jpg", $count;
	$im->Write($new_name);
	print $new_name, "\n";
}

#
#
# main procedure starts here
#
#
my @files = glob('*.jpg');
my $count = 0;

foreach my $ff (@files)  {
	++ $count;
	print "$ff => ";
	draw($ff, $count);
#	if ($count > 3)  {
#		last;
#	}
}
