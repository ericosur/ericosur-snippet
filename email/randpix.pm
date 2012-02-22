use strict;
use warnings;

package pixutil;

use Image::Magick;
use Text::Lorem;

#my @ext = qw(png gif jpg tif pict tga xpm wbmp sgi tga);
my @ext = qw(png gif jpg);
my $pix_fname = 'tmp';
my $maxx = 240;
my $maxy = 320;
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

for (1..5)  {
	$rc = $im->Draw(
		primitive => 'circle',
		#stroke	 => 'red',
		fill => get_random_color(),
		strokewidth => 4,
		points => get_random_coord()
	);
	warn $rc if $rc;
}

	$rc = $im->Annotate(
		x => 20,
		y => 40,
		font => 'Lucida-Console',
		#stroke	 => 'yellow',
		fill => get_random_color(),
		pointsize  => 20,
		text => get_randomtext()
	);
	warn $rc if $rc;

	$rc = $im->Annotate(
		x => 20,
		y => 70,
		font => 'Aroa;',
		#stroke	 => 'blue',
		fill => get_random_color(),
		pointsize  => 18,
		text => get_date()
	);
	warn $rc if $rc;

	$rc = $im->Annotate(
		x => 15,
		y => $maxy - 25,
		font => 'Aroa;',
		#stroke	 => 'yellow',
		fill => get_random_color(),
		pointsize  => 18,
		text => "by ImageMagick"
	);
	warn $rc if $rc;

	$rc = $im->Write($pix_name);
	warn $rc if $rc;
}

1;
