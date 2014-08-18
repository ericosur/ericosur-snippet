use strict;
use Image::ExifTool;
use Image::ExifTool::Location;
use Geo::Coordinates::DecimalDegrees;

my $exif = Image::ExifTool->new();

my $src = $ARGV[0] || die;
die if not -f $src;
my $dst = $src;
$dst =~ s/(.*)\.(.*)/$1_lbs\.$2/;

print STDERR "input: $src\noutput: $dst\n";

$exif->ExtractInfo($src);
$exif->SetLocation(
	24.48280,
	118.32119);
$exif->WriteInfo($src, $dst);

sub get_decimal_deg()
{
	my ($deg, $min, $sec) = @_;

	if ($sec)  {
		return dm2decimal($deg, $min, $sec);
	} else  {
		return dm2decimal($deg, $min);
	}
}

# •jπÁ¿Yæ‘•v¿] N24 28.968 E118 19.271
