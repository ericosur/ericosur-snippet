use strict;
use warnings;

use Image::ExifTool ();
use Data::Dump qw(dump);

my $file = "img.jpg";
my $exiftool = new Image::ExifTool;
my $info = $exiftool->ImageInfo($file);

# add a keyword without replacing existing keywords
#$exiftool->SetNewValue('Keywords', "foobar", AddValue => 1);
$exiftool->SetNewValue("UserComment", "3.141592653");

$exiftool->WriteInfo($file, 'foobar.jpg');


