#!/usr/bin/perl -w

# $Id: gpsPhoto.pl,v 1.154 2010/09/11 16:05:06 girlich Exp $

#Copyright (C) 2005 Peter Sykora, Andreas Neumann

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# Requirements: Perl >5.8, 
# Module XML::Parser (Activestate: XML-Parser)
# Module Image::ExifTool (Activestate: Image-ExifTool, warning: Activestate has usually an old version of this module that won't work well with NEF files)
# Macosx: xcode tools (for gcc compiler)
# (exiftags: http://www.sno.phy.queensu.ca/~phil/exiftool/)


########################################################################
package util;

use strict;
use POSIX qw(floor);
use File::Basename qw(fileparse);

sub dd2dms {
	my $dd = shift;
	# print "$dd\n";
	my $minutes = ($dd - floor($dd)) * 60.0;
	my $seconds = ($minutes - floor($minutes)) * 60.0;
	$minutes = floor($minutes);
	my $degrees = floor($dd);
	return $degrees.",".$minutes.",".$seconds;
}

sub dms2dd($)
{
	my ($dms) = @_;
	# print "dms=$dms\n";
	# 48 deg 17' 33.39"
	$dms =~ /(\d+) deg (\d+)' ([\d.]+)"/;
	my ($degrees, $minutes, $seconds) = ($1, $2, $3);
	my $dd = $degrees + $minutes/60.0 + $seconds/3600.0;
	# print "$dd\n";
	return $dd;
}

sub stripheight($)
{
	my ($height) = @_;
	# print  "height=$height\n";
	# 475 metres
	$height =~ s/(\d+)\s.*/$1/;
	# print  "height=$height\n";
	return $height;
}

sub dtexpand($)
{
	my ($dt) = @_;
	my ($d, $t, $dummy) = split(/[T|Z]/,$dt);
	return ($d, $t);
}

sub dtcombine($$)
{
	my ($d, $t) = @_;
	return sprintf("%sT%sZ", $d, $t);
}

sub DateTimeOriginal_to_dt($)
{
	my ($DateTimeOriginal) = @_;
	return undef unless defined $DateTimeOriginal;

	$DateTimeOriginal=~/(\d{4}):(\d{1,2}):(\d{1,2})\s+(\d{1,2}):(\d{1,2}):(\d{1,2})/;
	my $dt = sprintf("%04d-%02d-%02dT%02d:%02d:%02dZ", $1, $2, $3, $4, $5, $6);
	return $dt;
}

sub dt_to_DateTimeOriginal($)
{
	my ($dt) = @_;
	return undef unless defined $dt;

	my $DateTimeOriginal = $dt;
	$DateTimeOriginal =~ s/T/ /;
	$DateTimeOriginal =~ s/Z$//;
	$DateTimeOriginal =~ s/-/:/g;
	return $DateTimeOriginal;
}

sub printpoint($)
{
	my ($point) = @_;

	print "Point={\n";
	for my $key (keys %{$point}) {
		printf " %s=%s\n", $key, $point->{$key};
	}
	print "}\n";
}

sub dest_to_temp($)
{
	my ($dest) = @_;

	my ($base, $dir, $ext) = fileparse($dest,qr/\.[^.]*/);
	return File::Spec->join($dir, "${base}_1$ext");
}


########################################################################
package meta;

use strict;
use Image::ExifTool;

sub new
{
	my $class = shift;
	my $self = {};
	($self->{metaFile}) = @_;
	bless($self,$class);
	return $self;
}

sub exifTool($)
{
	my $self = shift;
	if (!exists $self->{exifTool}) {
		$self->{exifTool} = new Image::ExifTool;
	}
	return $self->{exifTool};
}

sub imgInfo($)
{
	my $self = shift;
	if (!exists $self->{imgInfo}) {
		$self->{imgInfo} = $self->exifTool->ImageInfo($self->{metaFile});
	}
	return $self->{imgInfo};
}

sub SetNewValue($$$$)
{
	my $self = shift;
	my ($tag, $value, $group, @opts) = @_;

	my ($success, $errStr) = $self->exifTool->SetNewValue($tag,$value,Group=>$group, @opts);
	die "Problem writing out '$tag'='$value' for file '$self->{metaFile}'. Error: $errStr\n" if $success != 1; 
}

sub _is_geotagged($$)
{
	my $self = shift;
	my @geotags = @_;

	my $it_is = 1;
	for my $geotag (@geotags) {
		if (!exists $self->imgInfo->{$geotag}) {
			$it_is = 0;
			last;
		}
	}
	return $it_is;
}

sub getDateTimeOriginal($)
{
	my $self = shift;
	my $time = $self->imgInfo->{DateTimeOriginal};
	if (!defined $time) {
		$time = $self->imgInfo->{DateTimeDigitized};
	}
	if (!defined $time) {
		$time = $self->imgInfo->{CreateDate};
	}
	return util::DateTimeOriginal_to_dt($time);
}


########################################################################
package meta_exif;

use strict;
use vars qw(@ISA);
@ISA = qw( meta );

sub is_geotagged($)
{
	my $self = shift;

	return $self->_is_geotagged(
		'GPSLatitude',
		'GPSLatitudeRef',
		'GPSLongitude',
		'GPSLongitudeRef',
	);
}

sub get_point($)
{
	my $self = shift;

	my $point;

	# Latitude.
	$point->{y} = util::dms2dd($self->imgInfo->{GPSLatitude}) *
	(($self->imgInfo->{GPSLatitudeRef} eq 'South') ? -1.0 : 1.0);

	# Longitude.
	$point->{x} = util::dms2dd($self->imgInfo->{GPSLongitude}) *
	(($self->imgInfo->{GPSLongitudeRef} eq 'West') ? -1.0 : 1.0);

	# Altitude.
	if (
		exists $self->imgInfo->{GPSAltitude} &&
		exists $self->imgInfo->{GPSAltitudeRef}
	) {
		$point->{z} = util::stripheight($self->imgInfo->{GPSAltitude}) *
		(($self->imgInfo->{GPSAltitudeRef} eq 'Below Sea Level') ? -1.0 : 1.0);
	}
	else {
		$point->{z} = 0;
	}

	# Date & Time.
	if (
		exists $self->imgInfo->{GPSDateStamp} &&
		exists $self->imgInfo->{GPSTimeStamp}
	) {
		$point->{d} = $self->imgInfo->{GPSDateStamp};
		$point->{d} =~ s/:/-/g;

		$point->{t} = $self->imgInfo->{GPSTimeStamp};
		$point->{t} =~ s/:(\d)$/:0$1/;

		# Combined value.
		$point->{dt} = util::dtcombine($point->{d}, $point->{t});
	}
	else {
		$point->{dt} = $self->getDateTimeOriginal();
		($point->{d}, $point->{t}) = util::dtexpand($point->{dt});
	}

	return $point;
}

sub setDateTimeOriginal($$)
{
	my $self = shift;
	my ($dt) = @_;
	my ($d, $t) = util::dtexpand($dt);
	$d =~ s/-/:/g;
	$self->SetNewValue('DateCreated',$d,'IPTC');
	$self->SetNewValue('TimeCreated',$t,'IPTC');
}

sub setGPSLatitude($$)
{
	my $self = shift;
	my ($point) = @_;
	$self->SetNewValue('GPSLatitude',util::dd2dms(abs($point->{y})),'GPS');
	if ($point->{y} > 0) {
		$self->SetNewValue('GPSLatitudeRef','N','GPS');
	}
	else {
		$self->SetNewValue('GPSLatitudeRef','S','GPS');
	}
}

sub setGPSLongitude($$)
{
	my $self = shift;
	my ($point) = @_;
	$self->SetNewValue('GPSLongitude',util::dd2dms(abs($point->{x})),'GPS');
	if ($point->{x} > 0) {
		$self->SetNewValue('GPSLongitudeRef','E','GPS');
	}
	else {
		$self->SetNewValue('GPSLongitudeRef','W','GPS');
	}
}

sub setGPSTimeStamp($$)
{
	my $self = shift;
	my ($point) = @_;
	$self->SetNewValue('GPSTimeStamp',$point->{t},'GPS');
	$self->SetNewValue('GPSDateStamp',$point->{d},'GPS');
}


########################################################################
package meta_xmp;

use strict;
use vars qw(@ISA);
@ISA = qw( meta );

sub is_geotagged($)
{
	my $self = shift;
	return $self->_is_geotagged(
		'GPSLatitude',
		'GPSLongitude',
	);
}

sub get_point($)
{
	my $self = shift;

	my $point;

	# Latitude.
	$point->{y} = util::dms2dd($self->imgInfo->{GPSLatitude});

	# Longitude.
	$point->{x} = util::dms2dd($self->imgInfo->{GPSLongitude});

	# Altitude.
	if (
		exists $self->imgInfo->{GPSAltitude} &&
		exists $self->imgInfo->{GPSAltitudeRef}
	) {
		$point->{z} = util::stripheight($self->imgInfo->{GPSAltitude}) *
		(($self->imgInfo->{GPSAltitudeRef} eq 'Below Sea Level') ? -1.0 : 1.0);
	}
	else {
		$point->{z} = 0;
	}

	# Date and Time.
	if (exists $self->imgInfo->{GPSTimeStamp}) {
		$point->{dt} = util::DateTimeOriginal_to_dt($self->imgInfo->{GPSTimeStamp});
	}
	else {
		$point->{dt} = $self->getDateTimeOriginal();
	}
	($point->{d}, $point->{t}) = util::dtexpand($point->{dt});

	return $point;
}

sub setDateTimeOriginal($$)
{
	my $self = shift;
	my ($dt) = @_;
	$self->SetNewValue('DateTimeOriginal',util::dt_to_DateTimeOriginal($dt),'XMP');
}

sub setGPSLatitude($$)
{
	my $self = shift;
	my ($point) = @_;
	$self->SetNewValue('GPSLatitude',util::dd2dms($point->{y}),'XMP');
}

sub setGPSLongitude($$)
{
	my $self = shift;
	my ($point) = @_;
	$self->SetNewValue('GPSLongitude',util::dd2dms($point->{x}),'XMP');
}

{
	# Remember the proper tag name.
	my $tagname = undef;

sub setGPSTimeStamp($$)
{
	my $self = shift;
	my ($point) = @_;
	# util::printpoint($point);
	unless (defined $tagname) {
		my @tags = Image::ExifTool::GetAllTags('XMP');
		foreach my $tag (@tags) {
			# ExifTool 6.90 uses GPSTimeStamp.
			# ExifTool 7.36 uses GPSDateTime.
			if ($tag eq 'GPSDateTime' || $tag eq 'GPSTimeStamp') {
				# print "we have $tag\n";
				$tagname = $tag;
			}
		}
	}
	$self->SetNewValue($tagname,util::dt_to_DateTimeOriginal($point->{dt}),'XMP');
}

}


package IPTC;

use strict;

sub new
{
	my $class = shift;
	my %params;
	if (($#_ % 2) != 1) {
		die "Odd number of parameters for IPTC->new";
	}
	%params=@_;
	my $self = {};
	@$self{keys %params} = values %params;
	bless($self,$class);
	return $self;
}

sub set_val($$$)
{
	my $self = shift @_;
	my ($state, $val) = @_;

	if (length($val) > $self->len()) {
		die "The IPTC tag '$self->tag()') has the maximum length $self->len().\nThe length of value '$val' is too big.\n";
	}

	if (!exists $self->{val}) {
		$self->{val} = {};
	}

	if ($state eq 'any' || $state eq 'geotag') {
		$self->{val}->{geotag} = $val;
		printf "%s(geotag)=%s\n", $self->tag(), $val;
	}
	if ($state eq 'any' || $state eq 'nogeotag') {
		$self->{val}->{nogeotag} = $val;
		printf "%s(nogeotag)=%s\n", $self->tag(), $val;
	}
}

sub get_val($$)
{
	my $self = shift @_;
	my ($point) = @_;

	my $val = undef;

	my $valhash = $self->{val};

	if (defined $valhash) {

		if (defined $point) {
			if (exists $valhash->{geotag}) {
				$val = $valhash->{geotag};
			}
		}
		else {
			if (exists $valhash->{nogeotag}) {
				$val = $valhash->{nogeotag};
			}
		}

	}

	return $val;
}

sub opt($)
{
	my $self = shift @_;
	my $opt = undef;
	if (exists $self->{opt}) {
		$opt = $self->{opt};
	}
	return $opt;
}

sub tag($)
{
	my $self = shift @_;
	my $tag = undef;
	if (exists $self->{tag}) {
		$tag = $self->{tag};
	}
	return $tag;
}

sub len($)
{
	my $self = shift @_;
	my $len = undef;
	if (exists $self->{len}) {
		$len = $self->{len};
	}
	return $len;
}

sub list($)
{
	my $self = shift @_;
	my $list = undef;
	if (exists $self->{list}) {
		$list = $self->{list};
	}
	return $list;
}


########################################################################
package main;

use strict;

# Standard Perl modules.
use File::Basename;
use File::Copy;
use File::Spec;
use Getopt::Long qw(:config no_ignore_case);
use POSIX qw(floor tzset tzname);
use Time::Local;
use Pod::Usage;

use Math::Complex qw(:trig);
use Math::Trig qw(deg2rad rad2deg great_circle_distance great_circle_waypoint great_circle_direction spherical_to_cartesian cartesian_to_spherical);
# With this code I can get the symbols from any module.
# Hopefully the interfaces of other modules remain a bit
# more stable than Math::Trig and Math::Complex.
BEGIN {
        my %syms = ('pi'=>1, 'pip2'=>1, 'pip4'=>1, 'pi2'=>1);
        my @modules = ('Math::Trig', 'Math::Complex');
	for my $module (@modules) {
		for my $sym (keys %syms) {
			no strict 'refs';
			for my $e (@{"${module}::EXPORT"}, @{"${module}::EXPORT_OK"}) {
				if ($e eq $sym) {
					*{$sym}=\&{"${module}::$sym"};
					delete $syms{$sym};
				}
			}
			use strict;
		}
	}
	for my $sym (keys %syms) {
		print STDERR "WARNING: The symbol '$sym' is not exported by ", (join ', ', @modules), ".\n";
		print STDERR "WARNING: Please install newer module versions.\n";
		no strict 'refs';
		*{$sym}=\&{"Math::Complex::$sym"};
		use strict;
	}
}

use IO::Socket::INET;
use IO::File;
use File::Temp qw(tempdir);

# Additional Perl Module.
use XML::Parser;	# There is no more basic XML parser module.
use Image::ExifTool;	# Someone has to do all the image manipulation.

sub kml_create($);
sub kml_write_header($$$);
sub kml_write_photo_header($);
sub kml_write_folder_start($$);
sub kml_write_folder_end($);
sub kml_write_image($$$);
sub kml_write_image_placemark($$$$$$$);
sub kml_write_image_screenoverlay($$$$);
sub kml_write_image_groundoverlay($$$$$);
sub kml_write_image_photooverlay($$$$$$);
sub kml_write_photo_footer($);
sub kml_write_track_line($);
sub kml_write_track_timeline($);
sub kml_write_about($);
sub kml_write_footer($);
sub kml_close($$);
sub temp_outfile_cleanup($);
sub image_action_correlate($$$);
sub image_action_delete_geotag($$$);
sub dms2dd($);
sub stripheight($);
sub binary_search_s($$);
sub interpolate_factor($$$);
sub interpolate_calc($$$);
sub interpolate_linear($$$);
sub interpolate_great_circle($$$);
sub uniq(@);
sub set_option_hashlist($$$$);
sub set_option_radiolist($$$$);
sub set_kml_image_type($$);
sub set_opt_kml_track_enable($$);
sub set_opt_kml_track_color($$);
sub set_opt_kml_thumbnail_method($$);
sub set_opt_select($$);
sub set_IPTC_tag($$);
sub get_IPTC_tag($);
sub set_tz_guess($$);
sub set_report_distance($$);
sub set_report_direction($$);
sub set_geoinfo($$);
sub set_geotag_source($$);
sub set_image_action($$);
sub set_interpolate($$);
sub set_image_file_time($$);
sub Parser_process_node($@);
sub store_segment($@);
sub report_distance_none($$$);
sub report_distance_gen($$$$$);
sub report_distance_km($$$);
sub report_distance_miles($$$);
sub report_distance_nautical($$$);
sub report_direction_none($);
sub report_direction_degree($);
sub report_direction_4($);
sub report_direction_8($);
sub expand_iptc_value($$$);
sub get_geoinfo_geourl($$$);
sub get_geoinfo_geonames($$$);
sub get_geoinfo_wikipedia($$$);
sub get_geoinfo_osm($$$);
sub get_geoinfo_zip($$$);
sub get_geoinfo_none($$$);
sub get_url_LWP($);
sub get_url_selfmade($);
sub get_url_fakefile($);
sub thumbnail_none();
sub thumbnail_convert();
sub image_file_time_modify($$$);
sub image_file_time_exif($$$);
sub image_file_time_keep($$$);

my @dir; #directories with images
my @image_list; # Contains the list of files with image file names.
my @image; # Contains the list of image file names given on the command line.
my @opt_gpsdir; # Directory with gpsfiles.
my @opt_gpsfile_list; # Contains the list of files with gpsfile names.
my @opt_gpsfile; #text-files containing gps-data
my $maxtimediff=120; #maximum time-difference in seconds (integer value)
my $maxdistance=20; # Maximum distance for interpolation (integer value, metres)
my $timeoffset=undef; #time-offset in seconds (simple expression)
my $writecaption; #indicates that caption should be copied from file-name
my $copydate; #indicates that the program should copy the EXIF date to the IPTC tag
my $opt_enable_xmp; # Enables XMP support.
my @gpsData=(); #array holding GPS data
my $kml; #path to keyhole file output
my $kmz; # Path to keyhole compressed output file.
my %kml_image_type_default = ('photooverlay'=>1); # Default: photooverlay only.
my %kml_image_type; # How are images represented in a KML file.
my $opt_kml_image_dir = undef; # KML will refer to images there.
my $opt_kml_track_enable = 0x01; # Write track into KML.
my @opt_kml_track_color=(); # Track colour.
my @opt_kml_track_color_default = ('7fffffff'); # Default track colour.
my $thumbnail_method = \&thumbnail_none; # Thumbnail creation method.
my $opt_thumb_dir = 'thumbs'; # Directory to store thumbnails in. Relative to image directory or absolute.
my $opt_track_height = 0; # Flag: Track with height or not (default).
my $opt_kml_timeline = 0; # Flag: Additional timeline in the KML or not (default).
my $opt_kml_placemark_thumbnail_size = 200; # Size of the longer side of the thumbnail image in a placemark.
my $dry_run; # Don't change the image files.
my $image_file_time = \&image_file_time_modify; # Let ExifTool manipulate the file time.
my $overwrite_geotagged; # Overwrite images, which are already geotagged.
my $interpolate = undef; # Interpolate geo coordinates.
my $tz_guess = undef;
my $report_distance = \&report_distance_none; # Do not report the distance.
my $report_direction = \&report_direction_none; # Do not report the direction.
my $get_geoinfo = \&get_geoinfo_geonames; # Method to guess geo information.
my %geotag_source_default = ('exif'=>1,'track'=>1);
my %geotag_source;
my $opt_geotag = undef;
my $image_action = \&image_action_correlate; # Default: perform the correlation.
my $opt_language = undef; # Language.
my $opt_version; # Print the version number.
my $opt_help; # Print help.
my $opt_man; # Print manual page.
my $opt_select = 'any'; # Default: any image.
my @IPTC=( # IPTC options definition.
	IPTC->new( 'opt'=>'credit', 'tag'=>'Credit', 'len'=>32, 'list'=>0, ),
	IPTC->new( 'opt'=>'city', 'tag'=>'City', 'len'=>32, 'list'=>0, ),
	IPTC->new( 'opt'=>'sublocation', 'tag'=>'Sub-location', 'len'=>32, 'list'=>0, ),
	IPTC->new( 'opt'=>'state', 'tag'=>'Province-State', 'len'=>32, 'list'=>0, ),
	IPTC->new( 'opt'=>'country', 'tag'=>'Country-PrimaryLocationName', 'len'=>64, 'list'=>0, ),
	IPTC->new( 'opt'=>'copyright', 'tag'=>'CopyrightNotice', 'len'=>128, 'list'=>0, ),
	IPTC->new( 'opt'=>'keywords', 'tag'=>'Keywords', 'len'=>32768, 'list'=>1, ),
	IPTC->new( 'opt'=>'source', 'tag'=>'Source', 'len'=>32, 'list'=>0, ),
	IPTC->new( 'opt'=>'caption', 'tag'=>'Caption-Abstract', 'len'=>2000, 'list'=>0, ),
);

(my $source_release = q$Id: gpsPhoto.pl,v 1.154 2010/09/11 16:05:06 girlich Exp $) =~ s/^Id: gpsPhoto.pl,v //;
$source_release =~ s/(:\d{2})\s*.*/$1/;
(my $program = $0) =~ s,.*/,,;

# Define normal options.
my %options = (
		'dir=s' => \@dir,
		'image-list|I=s' => \@image_list,
		'image|i=s' => \@image,
		'gpsdir=s' => \@opt_gpsdir,
		'gpsfile-list|G=s' => \@opt_gpsfile_list,
		'gpsfile=s' => \@opt_gpsfile,
		'maxtimediff=i' => \$maxtimediff,
		'maxdistance=i' => \$maxdistance,
		'timeoffset=s' => \$timeoffset,
		'writecaption' => \$writecaption,
		'copydate' => \$copydate,
		'enable-xmp' => \$opt_enable_xmp,
		'kml=s' => \$kml,
		'kmz=s' => \$kmz,
		'kml-image-type=s' => \&set_kml_image_type,
		'kml-image-dir=s' => \$opt_kml_image_dir,
		'kml-track-enable=s' => \&set_opt_kml_track_enable,
		'track-color=s' => \&set_opt_kml_track_color,
		'track-colour=s' => \&set_opt_kml_track_color,
		'track-height' => \$opt_track_height,
		'kml-timeline' => \$opt_kml_timeline,
		'kml-placemark-thumbnail-size=i' => \$opt_kml_placemark_thumbnail_size,
		'kml-placemark-thumbnail-method=s' => \&set_kml_placemark_thumbnail_method,
		'kml-placemark-thumbnail-dir=s' => \$opt_thumb_dir,
		'dry-run|n' => \$dry_run,
		'image-file-time=s'=> \&set_image_file_time,
		'overwrite-geotagged' => \$overwrite_geotagged,
		'interpolate=s' => \&set_interpolate,
		'tz-guess=s' => \&set_tz_guess,
		'report-distance=s' => \&set_report_distance,
		'report-direction=s' => \&set_report_direction,
		'geoinfo=s' => \&set_geoinfo,
		'geotag-source=s' => \&set_geotag_source,
		'geotag=s' => \$opt_geotag,
		'language=s' => \$opt_language,
		'delete-geotag' => \&set_image_action,
		'select=s' => \&set_opt_select,
		'V|version' => \$opt_version,
		'help|?' => \$opt_help,
		'man' => \$opt_man,
);

# Add the IPTC options.
foreach my $iptc (@IPTC) {
	$options{$iptc->opt().'=s'}=\&set_IPTC_tag;
}

my $fakefile;
# $fakefile = 'rss';

my $geturl = \&get_url_selfmade;
eval {
	require LWP::Simple;
	$geturl = \&get_url_LWP;
};
if ($fakefile) {
	$geturl = \&get_url_fakefile;
}

#get parameters
GetOptions(%options) or pod2usage(-verbose=>0);

if ($opt_version) {
	print "$program (release $source_release)\n";
	exit (0);
} elsif ($opt_help) {
	pod2usage(-verbose=>0);
	exit(0);
} elsif ($opt_man) {
	pod2usage(-verbose=>2);
	exit(0);
}

my $thumb_absolute = File::Spec->file_name_is_absolute($opt_thumb_dir);

if ($thumb_absolute && $opt_kml_image_dir) {
	die "You used the options:\n--kml-image-dir=$opt_kml_image_dir\n--kml-placemark-thumbnail-dir=$opt_thumb_dir\nThis combination is not allowed. The one and only thumbnail path must be\nrelative to the images on disk and relative to the same images in KML.\n";
}

if ($kmz) {
	my $can_do_it = 0;
	eval {
		require Archive::Zip;
		$can_do_it = 1;
	};
	if ($can_do_it == 0) {
		print "KMZ file creation needs ZIP support in Perl.\n";
		print "Loading the module 'Archive::Zip' failed.\n";
		print "Please install this module to create KMZ files.\n";
		die "@_";
	}
}

if (scalar @dir==0 && scalar @image_list==0 && @image==0) {
	warn "You have to specify images (--dir, --image-list, --image)!\n";
	pod2usage(-verbose=>0);
	exit(0);
}

print "Image files will not be changed.\n" if $dry_run;

# If not given, use the default source.
if (scalar keys %geotag_source == 0) {
	%geotag_source = %geotag_source_default;
}

# If not given, use the default type.
if (scalar keys %kml_image_type == 0) {
	%kml_image_type = %kml_image_type_default;
}

# If not given, use the default colour.
if (scalar @opt_kml_track_color == 0) {
	@opt_kml_track_color = @opt_kml_track_color_default;
}

# We start with an empty gps file list.
my @gpsfiles = ();

# Add the single gps files.
foreach (@opt_gpsfile) {
	if (-f) {
		$_ = File::Spec->rel2abs($_);
		push @gpsfiles, $_;
	}
	else {
		die "GPS file $_ does not exist.\n";
	}
}

# Add the directories.
for my $dir (@opt_gpsdir) {
	# Read directory and collect gps files.
	opendir(DIR, $dir) or die "Can't open directory $dir: $!.";
	print "Processing directory \"$dir\".";
	my $count = 0;
	while (defined(my $file = readdir(DIR))) {
		$file = File::Spec->rel2abs(File::Spec->join($dir,$file));
		# First check if it is an gps file.
		my ($base, $dir, $ext) = fileparse($file,qr/\.[^.]*/);
		if ($ext =~ /^\.(gpx)$/i) {
			push @gpsfiles, $file;
			$count++;
		}
	}
	closedir(DIR);
	print " $count gps file" . ($count!=1?'s':'') . ".\n";
}

# Add the list of file names.
for my $list (@opt_gpsfile_list) {
	open FD, "<$list" or
		die "Can't open gps list file $list for reading: $!.\n";
	print "Processing gps list file \"$list\".";
	my $count = 0;
	while (<FD>) {
		chomp;
		s/^\s*#.*//;
		s/\s*$//;
		next unless /./;
		if (-f) {
			$_ = File::Spec->rel2abs($_);
			push @gpsfiles, $_;
			$count++;
		}
		else {
			print " Line $.: \"$_\" does not exist.\n";
		}
	}
	close FD;
	print " $count gps file" . ($count!=1?'s':'') . ".\n";
}

my $gpsfiles = scalar @gpsfiles;
printf "Found %d total gps file name%s.\n", $gpsfiles, $gpsfiles!=1?"s":"";

# Process every file only once. The first survives.
@gpsfiles = uniq(@gpsfiles);

if ($gpsfiles != scalar @gpsfiles) {
        print "Found only " . scalar @gpsfiles . " disjunct gps file names.\n";
}

my $lineCounter=0;

my %gpsTracks=();
for my $gpsfile (@gpsfiles) {
	print "Parsing GPX file \"$gpsfile\":";
	my $parser = XML::Parser->new(Style => 'Tree');
	my $doc;
	eval {
		$doc = $parser->parsefile($gpsfile);
	};
	if ($@) {
		print " Error in file. Ignore it.\n";
	} else {
		Parser_process_node($gpsfile,@$doc);
		print " points.\n";
	}
}

print "Processed $lineCounter coordinates.\n";

# Only one entry per second. The first survives.
my %seen = ();
@gpsData = grep { ! $seen{$_->{s}} ++ } @gpsData;

# Give a hint, if some values disappeared.
if ($lineCounter != scalar @gpsData) {
	print "Found only " . scalar @gpsData . " disjunct time stamps.\n";
}

# Sort the track points.
@gpsData = sort { $a->{s} <=> $b->{s} } @gpsData;

# Main point: point with the middle index.
my $mainPoint = $gpsData[@gpsData/2];

# Try guessing the time zone.
if (scalar @gpsData > 0 && $tz_guess) {
	my $guess = &{$tz_guess}($mainPoint);
	# Check the tz_guess functions.
	# for (my $x=-180;$x<180;$x+=4) {
	#	$gpsData[0]->{x} = $x;
	#	&{$tz_guess}($gpsData[$mainPoint]);
	# }

	# Now check, if the timeoffset string contains the string 'guess'.
	if (defined $timeoffset && $timeoffset =~ /guess/) {
		# Replace the string.
		$timeoffset =~ s/guess/($guess)/;

		# Make sure, that we have now only digits, '.', '+', '-',
		# '(', and ')'.
		die "The timeoffset expression '$timeoffset'\nis too complicated to evaluate\n" unless $timeoffset=~/^[\d\.\+\-\(\)]+$/;
		# Evaluate the result.
		my $newtimeoffset = eval $timeoffset;
		if ($@) {
			die "Can't evaluate timeoffset expression '$timeoffset': $@\n";
		}
		$timeoffset = $newtimeoffset;
		printf "Using --timeoffset=%f.\n", $timeoffset;
	}
	else {
		# Only TZ guessing is enough.
		exit(0);
	}
}

my $kml_altitudeMode = 'clampToGround';
# Not yet an option. If 0, the tracks floats in the air.
my $kml_extrude = 1;

my $kml_fh = undef;
my $kmz_dir = undef;
my $kmz_kml = 'doc.kml';
my $kmz_temp_kml = undef;
my $kmz_temp_kml_fh = undef;
my $kmz_zip = undef;
# Start KML file.
if ($kml || $kmz) {
	if ($kml) {
		# Create KML file.
		$kml_fh = kml_create($kml);
	}
	if ($kmz) {
		$kmz_dir = tempdir(CLEANUP => 1);
		$kmz_temp_kml = File::Spec->join($kmz_dir, $kmz_kml);
		# print "$kmz_dir $kmz_temp_kml\n";
		$kmz_temp_kml_fh = kml_create($kmz_temp_kml);
		$kmz_zip = Archive::Zip->new();
		# In GE kmz files, the doc.kml is at the beginning, but we
		# don't have any content yet for doc.kml.
		# $kmz_zip->addFile($kmz_temp_kml, $kmz_kml);
	}

	if ($opt_track_height) {
		$kml_altitudeMode = 'absolute';
	}

	# Guess global track geo information.
	my $geoinfo = undef;
	my $mainGeo;
	foreach my $iptc (@IPTC) {
		# Default is the empty string.
		$mainGeo->{$iptc->tag()} = '';

		# Do we have something better?
		my $value = expand_iptc_value($iptc, $mainPoint, $geoinfo);
		if (defined $value) {
			$mainGeo->{$iptc->tag()} = $value;
		}
	}

	# Create a geo location name. Probably guessed.
	my $location = join " - ",
		$mainGeo->{'Country-PrimaryLocationName'},
		$mainGeo->{'Province-State'},
		$mainGeo->{'City'};
	$location =~ s/-  -|- $|^-//;

	# Start KML file.
	if ($kml) {
		kml_write_header($kml_fh, $location, $copydate);
		kml_write_photo_header($kml_fh);
	}
	if ($kmz) {
		kml_write_header($kmz_temp_kml_fh, $location, $copydate);
		kml_write_photo_header($kmz_temp_kml_fh);
	}
}

my $pictureCounter = 0;
my $pictureCounterCoordinate = 0;

# We start with an empty image list.
my @images = ();

# Add the single images.
foreach (@image) {
	if (-f) {
		$_ = File::Spec->rel2abs($_);
		push @images, $_;
	}
	else {
		die "Image file $_ does not exist.\n";
	}
}

# Add the directories.
for my $dir (@dir) {
	# Read directory and collect image files.
	opendir(DIR, $dir) or die "Can't open directory $dir: $!.";
	print "Processing directory \"$dir\".";
	my $count = 0;
	while (defined(my $file = readdir(DIR))) {
		$file = File::Spec->rel2abs(File::Spec->join($dir,$file));
		# First check if it is an image file.
		my ($base, $dir, $ext) = fileparse($file,qr/\.[^.]*/);
		if ($ext =~ /^\.(jpg|jpeg|nef|cr2|crw|mrw|jpe|tif|tiff)$/i) {
			push @images, $file;
			$count++;
		}
	}
	closedir(DIR);
	print " $count image" . ($count!=1?'s':'') . ".\n";
}

# Add the list of file names.
for my $image_list (@image_list) {
	open FD, "<$image_list" or
	die "Can't open image list file $image_list for reading: $!.\n";
	print "Processing image list file \"$image_list\".";
	my $count = 0;
	while (<FD>) {
		chomp;
		s/^\s*#.*//;
		s/\s*$//;
		next unless /./;
		if (-f) {
			$_ = File::Spec->rel2abs($_);
			push @images, $_;
			$count++;
		}
		else {
			print " Line $.: \"$_\" does not exist.\n";
		}
	}
	close FD;
	print " $count image" . ($count!=1?'s':'') . ".\n";
}

my $images = scalar @images;
printf "Found %d total image file name%s.\n", $images, $images!=1?"s":"";

# Process every file only once. The first survives.
@images = uniq(@images);

if ($images != scalar @images) {
	print "Found only " . scalar @images . " disjunct image file names.\n";
}

my $temp_outfile = undef;

# Process image files.
for my $image_source (@images) {
	my $writeFile = 0;

	my $meta_dest = undef;
	my $xmp_write_source = undef;
	my $meta_in = undef;
	my $meta_out = undef;

	if ($opt_enable_xmp) {
		my ($base, $dir, $ext) = fileparse($image_source,qr/\.[^.]*/);
		# Search the XMP file.
		foreach my $xmp ('xmp','xmP','xMp','xMP','Xmp','XmP','XMp','XMP') {
			my $xmp_source = File::Spec->join($dir, "$base.$xmp");
			if (-f $xmp_source) {
				# Case 1: xmp->xmp.
				$meta_in = meta_xmp->new($xmp_source);
				$xmp_write_source = $xmp_source;
				$meta_dest = $xmp_source;
				$meta_out = meta_xmp->new(util::dest_to_temp($meta_dest));
				last;
			}
		}
		if (!defined $meta_in) {
			# Case 2: image->xmp.
			$meta_in = meta_exif->new($image_source);
			$xmp_write_source = undef;
			$meta_dest = File::Spec->join($dir, "${base}.xmp");
			$meta_out = meta_xmp->new(util::dest_to_temp($meta_dest));
		}
	}
	else {
		# Case 3: image->image.
		$meta_in = meta_exif->new($image_source);
		$meta_dest = $image_source;
		$meta_out = meta_exif->new(util::dest_to_temp($meta_dest));
	}

	print "$image_source";

	# Perform the image action.
	$writeFile = &{$image_action}($image_source, $meta_in, $meta_out);

	#Finally write out the new metadata
	if ($writeFile == 1 && !$dry_run) {
		my $success;

		$temp_outfile = $meta_out->{metaFile};
		$SIG{INT} = \&temp_outfile_cleanup;

		# Prepare file date/time manipulations.
		&$image_file_time($meta_dest, $meta_in, $meta_out);

		if ($opt_enable_xmp) {
			$success = $meta_out->exifTool->WriteInfo($xmp_write_source, $meta_out->{metaFile}, 'XMP');
		}
		else {
			$success = $meta_out->exifTool->WriteInfo($meta_in->{metaFile}, $meta_out->{metaFile});
		}
		if ($success != 1) {
			my $errStr = $meta_out->exifTool->GetValue('Error');
			die "\nError writing $meta_out->{metaFile}" . ($errStr? ",\nerror: $errStr":"") . ".\n";
		}
		else {
			my $result = move($meta_out->{metaFile}, $meta_dest);
			if (!$result) {
				die "\nError replacing $meta_dest with $meta_out->{metaFile}: $!.\n";
			}
		}
		$SIG{INT} = 'DEFAULT';
		$temp_outfile = undef;
	}
	$pictureCounter++;
}
print "Found coordinates for $pictureCounterCoordinate images out of $pictureCounter images ... done.\n";

if ($kml) {
	kml_write_photo_footer($kml_fh);
	kml_write_track_line($kml_fh);
	kml_write_track_timeline($kml_fh);
	kml_write_about($kml_fh);
	kml_write_footer($kml_fh);
	kml_close($kml_fh, $kml);
}
if ($kmz) {
	kml_write_photo_footer($kmz_temp_kml_fh);
	kml_write_track_line($kmz_temp_kml_fh);
	kml_write_track_timeline($kmz_temp_kml_fh);
	kml_write_about($kmz_temp_kml_fh);
	kml_write_footer($kmz_temp_kml_fh);
	kml_close($kmz_temp_kml_fh, $kmz_temp_kml);

	# Compress KMZ file.
	$kmz_zip->addFile($kmz_temp_kml, $kmz_kml);
	my $status = $kmz_zip->writeToFileNamed($kmz);
	die "Can't write KMZ file '$kmz'\n" if $status != Archive::Zip->AZ_OK;
}

# Main end.

sub temp_outfile_cleanup($)
{
	my ($sig) = @_;
	print STDERR "Caught SIG$sig.\n";
	if (defined $temp_outfile && -f $temp_outfile) {
		print STDERR "Cleaning up.\n";
		unlink($temp_outfile);
		$temp_outfile = undef;
	}
	print STDERR "Shutting down.\n";
	exit(1);
}

sub image_action_correlate($$$)
{
	my ($image, $meta_in, $meta_out) = @_;
	my $writeFile = 0;
	my $do_track_correlation = (
		exists $geotag_source{'track'} &&
		scalar @gpsData > 0
	) ? 1 : 0;
	my $IPTC='IPTC';
	my $GPS='GPS';
	if ($opt_enable_xmp) {
		$GPS = 'XMP';
		# $IPTC = 'XMP';
	}

	if (!$overwrite_geotagged && $meta_in->is_geotagged()) {
		print " is already geotagged.\nSkip track correlation.\n";
		$do_track_correlation = 0;
	}

	my @dateTime;
	my $point = undef;

	if ($do_track_correlation) {

		if (!defined $timeoffset) {
			die "To perform a track correlation, the --timeoffset parameter is mandatory.\n";
		}
		if ($timeoffset !~ m/[+-]?\d+/) {
			die "The timeoffset '$timeoffset' is not a signed number.\n";
		}

		# We need the time to compare with the track data.
		my $createDate = $meta_in->getDateTimeOriginal();
		if ($createDate) {

			@dateTime = util::dtexpand($createDate);
			my ($year,$month,$day) = split(/-/,$dateTime[0]);
			my ($hour,$minute,$second) = split(/:/,$dateTime[1]);
			# That is wrong: the date is local but we interpret it
			# as GMT and add an offset. It would be much better to
			# have the real time zone and $timeoffset is only for
			# fine tuning.
			my $secs = timegm($second,$minute,$hour,$day,$month-1,$year) + $timeoffset;
			#now compare timestamps
			my $mintimediff;

			print ", $createDate, ";

			my $minIndex = binary_search_s(\@gpsData,$secs);
			if ($minIndex<scalar @gpsData &&
				$gpsData[$minIndex]->{s} == $secs) {
				# Exact match.
				$mintimediff = 0;
				$point = $gpsData[$minIndex];
				$point->{used} = 1;
				print "exact match.\n";
			} elsif (
				$interpolate
				&&
				$minIndex<scalar @gpsData
				&&
				$minIndex>0
				&&
				(
				(
					abs($gpsData[$minIndex]->{s}-$secs)<$maxtimediff
					&&
					abs($gpsData[$minIndex-1]->{s}-$secs)<$maxtimediff
				)
				||
				(
				great_circle_distance(
					NESW(
						$gpsData[$minIndex-1]->{x},
						$gpsData[$minIndex-1]->{y}),
					NESW(
						$gpsData[$minIndex  ]->{x},
						$gpsData[$minIndex  ]->{y}),
					6378000.0)<$maxdistance
				)
				)
				) {
				# Interpolate between
				# $minIndex-1 and $minIndex.

				printf "timediff=%ds and %ds.\n", $gpsData[$minIndex-1]->{s}-$secs, $gpsData[$minIndex]->{s}-$secs;

				my $factor = interpolate_factor(
					$gpsData[$minIndex-1]->{s},
					$gpsData[$minIndex]->{s},
					$secs);
				$point = &{$interpolate}
				(
					$gpsData[$minIndex-1],
					$gpsData[$minIndex],
					$factor
				);
				$gpsData[$minIndex-1]->{used} = 1;
				$gpsData[$minIndex]->{used} = 1;

				# Exif understands integer heights only.
				$point->{z} = int($point->{z}+0.5);
				$point->{s} = $secs;
				my ($sec,$min,$hour,$mday,$mon,$year)=gmtime($secs);
				$mon++;$year+=1900;
				$point->{t} = sprintf "%02d:%02d:%02d",
					$hour,$min,$sec;
				$point->{d} = sprintf "%02d-%02d-%02d",
					$year,$mon,$mday;
				$point->{dt} = util::dtcombine($point->{d}, $point->{t});
				$mintimediff = 0;
			} else {
				# No exact match. This or the previous
				# point might be nearer but either can be out
				# of array range.
				my $fromIndex = $minIndex>0?$minIndex-1:$minIndex;
				my $toIndex = $minIndex<scalar @gpsData?$minIndex:$minIndex-1;
				$mintimediff=undef;
				foreach my $index ($fromIndex..$toIndex) {
					my $key = $gpsData[$index]->{s};
					if ((!defined $mintimediff) ||
						(defined $mintimediff && 
						abs($key - $secs) < $mintimediff)) {
						$mintimediff = abs($key - $secs);
						if ($mintimediff<$maxtimediff) {
							$minIndex = $index;
							$point = $gpsData[$minIndex];
							$point->{used} = 1;
						}
					}
				}
				if (defined $mintimediff) {
					print "timediff=$mintimediff";
					if ($point) {
						printf " to %s", $point->{t};
					}
					print "\n";
				}
				else {
					print "timediff=completely out of range\n";
				}
			}

		}
		else {
			print " - neither EXIF tag DateTimeOriginal nor DateTimeDigitized available.\n";
		}
	} # End track correlation.

	# We found no point in the GPS file but we have an already
	# geotagged image. That's even better.
	if (!defined $point &&
		defined $geotag_source{'exif'} && $meta_in->is_geotagged()) {

		print ", get geotag from meta info.\n";
		$point = $meta_in->get_point();
	} # End geotag source 'exif'.

	if (!defined $point &&
		defined $geotag_source{'option'} && defined $opt_geotag) {
		if ($opt_geotag =~ /^([^,]+),([^,]+),([^,]+)/) {
			($point->{y},$point->{x},$point->{z}) = ($1, $2, $3);
			$point->{dt} = $meta_in->getDateTimeOriginal();
			($point->{d}, $point->{t}) = util::dtexpand($point->{dt});
		}
		else {
			die "Cannot understand value of option --geotag='$opt_geotag'.\n";
		}
	}

	my $geoinfo = undef;
	
	# Fill all general IPTC tags.
	foreach my $iptc (@IPTC) {
		my $value = expand_iptc_value($iptc, $point, $geoinfo);
		if (defined $value) {
			$writeFile = 1;
			if ($iptc->list() == 1) {
				# http://www.sno.phy.queensu.ca/~phil/exiftool/ExifTool.html#SetNewValue
				my @value_list = split(/,/, $value);
				foreach my $list_value (@value_list) {
					$list_value =~ s/^\s+|\s+$//g;
					$meta_out->SetNewValue($iptc->tag(),$list_value,$IPTC);
				}
			}
			else {
				$meta_out->SetNewValue($iptc->tag(),$value,$IPTC);
			}
			if ($point) {
				$point->{iptc}->{$iptc->opt()} = $value;
			}
		}
	}

	# This part only applies, if we have GPS data.
	if ($point) {

		my $instructions = "Lat ".$point->{y}.", Lon ".$point->{x}." - Bearing: 0 - Altitude: ".$point->{z}."m";
		print $instructions."\n";
		#write coordinates to IPTC field "SpecialInstructions"
		$meta_out->SetNewValue('SpecialInstructions',$instructions,$IPTC);

		# Write out GPS meta tags.

		# Write latitude.
		$meta_out->setGPSLatitude($point);

		# Write longitude.
		$meta_out->setGPSLongitude($point);

		# Write altitude.
		$meta_out->SetNewValue('GPSAltitude',abs($point->{z}),$GPS);
		if ($point->{z} > 0) {
			$meta_out->SetNewValue('GPSAltitudeRef','Above Sea Level',$GPS);
		}
		else {
			$meta_out->SetNewValue('GPSAltitudeRef','Below Sea Level',$GPS);
		}

		# Write date/time.
		$meta_out->setGPSTimeStamp($point);
		
		# Write map datum to WGS84.
		$meta_out->SetNewValue('GPSMapDatum','WGS-84',$GPS);

		# Write destination bearing.
		$meta_out->SetNewValue('GPSImgDirection',0,$GPS);
		$meta_out->SetNewValue('GPSImgDirectionRef','T',$GPS);

		$writeFile = 1;
		$pictureCounterCoordinate++;

		if ($kml || $kmz) {
			# Google Earth cannot display raw files.
			# Maybe we should convert them before referencing in the KML
			# file?
			my ($base, $dir, $ext) = fileparse($image,qr/\.[^.]*/); 
			if ($ext =~ /^\.(jpg|jpeg)$/i) { 
				kml_write_image($image, $point, $meta_in->imgInfo); 
			} 
		}

	}
	else {
		print "Could not find a coordinate.\n";		
	}
	if ($writecaption) {
		$writeFile = 1;
		my ($base, $dir, $ext) = fileparse($image,qr/\.[^.]*/);
		my $caption = $base;
		$caption =~ s/^\d+\_//;
		$caption =~ s/(\_.)/\U$1/g;
		$caption =~ s/\_/ /g;
		$caption = ucfirst($caption);
		$meta_out->SetNewValue('Caption-Abstract',$caption,$IPTC);
		$meta_out->SetNewValue('ObjectName',$caption,$IPTC);
	}

	# Copy EXIF date to IPTC/XMP date.
	if ($copydate) {
		$writeFile = 1;
		$meta_out->setDateTimeOriginal($meta_in->getDateTimeOriginal());
	}

	return $writeFile;
}

sub image_action_delete_geotag($$$)
{
	my ($image, $meta_in, $meta_out) = @_;
	my $writeFile = 0;
	print " delete geotag.\n";
	my @geotags = (
		'GPSLatitude',
		'GPSLatitudeRef',
		'GPSLongitude',
		'GPSLongitudeRef',
		'GPSAltitude',
		'GPSAltitudeRef',
		'GPSTimeStamp',
		'GPSDateStamp',
		'GPSMapDatum',
		'GPSImgDirection',
		'GPSImgDirectionRef',
		'SpecialInstructions',
	);
	foreach my $tag (@geotags) {
		if (exists $meta_in->imgInfo->{$tag}) {
			$writeFile =1;
			my ($changed_tags, $error) =
				$meta_out->exifTool->SetNewValue($tag);
			if ($changed_tags < 1) {
				die "Problem deleting tag '$tag': $error.\n";
			}
		}
	}
	return $writeFile;
}

sub kml_create($)
{
	my ($file) = @_;

	# Create KML file.
	my $fh = new IO::File ">$file";
	if (!defined $fh) {
		die "Can't open file $file for writing: $!\n";
	}

	return $fh;
}

sub kml_write_header($$$)
{
	my ($fh, $_location, $_copydate) = @_;

	# Start KML file.
	print $fh qq (<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.0">
<Document>
  <name>My images</name>
  <open>1</open>
  <description><![CDATA[);
	if (length($_location)>2) { print $fh qq(
	<h3>Location</h3>
	<p>$_location</p>);}
	if (my $_a = get_IPTC_tag('Keywords')) { print $fh qq(
	<h3>Keywords</h3>
	<p>$_a</p>);}
	if (my $_a = get_IPTC_tag('Source')) { print $fh qq(
	<h3>Source</h3>
	<p>$_a</p>);}
	if ($_copydate) { print $fh qq(
	<h3>Copydate</h3>
	<p>$_copydate</p>);}
	if (my $_a = get_IPTC_tag('Credit')) { print $fh qq(
	<h3>Credit</h3>
	<p>$_a</p>);}
	if (my $_a = get_IPTC_tag('CopyrightNotice')) { print $fh qq(
	<h3>Copyright</h3>
	<p>$_a</p>);}
  print $fh qq(
  ]]></description>
  <Style id="Photo">
   <geomScale>.75</geomScale>
    <IconStyle>
     <color>ffffffff</color>
      <Icon>
       <href>root://icons/palette-4.png</href>
       <x>192</x>
       <y>96</y>
       <w>32</w>
       <h>32</h>
      </Icon>
     </IconStyle>
  </Style>
	<Style id="timed_track_point">
		<IconStyle>
			<color>ffffffff</color>
			<scale>0.2</scale>
			<Icon>
				<href>root://icons/palette-6.png</href>
			</Icon>
		</IconStyle>
	</Style>);
}

sub kml_write_photo_header($)
{

	my ($fh) = @_;

	print $fh qq(
  <Folder>
   <name>Photos</name>
   <open>0</open>);
}

sub kml_write_folder_start($$)
{
	my ($fh, $_fn) = @_;
	print $fh qq(
<Folder>
	<name>$_fn</name>
	<open>0</open>
	<visibility>0</visibility>
	<Style>
		<ListStyle>
			<listItemType>radioFolder</listItemType>
			<bgColor>00ffffff</bgColor>
		</ListStyle>
	</Style>

);
}

sub kml_write_folder_end($)
{
	my ($fh) = @_;

	print $fh qq(
</Folder>
);
}

sub kml_write_image($$$)
{
	my ($file, $point, $imgInfo) = @_;

	# Default: landscape.
	my $image_landscape = 1;
	my $image_ratio = 3.0/4.0;

	if (
		exists $imgInfo->{ImageHeight} &&
		exists $imgInfo->{ImageWidth}
	) {
		$image_ratio = $imgInfo->{ImageHeight}/$imgInfo->{ImageWidth};
	}
	# We might detect portrait mode.
	if ($image_ratio>1) {
		$image_landscape = 0;
	}

	my $dummy;
	($dummy, $dummy, my $fn) = File::Spec->splitpath( $file );
	my $kmz_image_dir = 'files'; # GE stores files there.

	if (scalar keys %kml_image_type > 1) {
		if ($kml) {
			kml_write_folder_start($kml_fh, $fn);
		}
		if ($kmz) {
			kml_write_folder_start($kmz_temp_kml_fh, $fn);
		}
	}

	# Image file names in KML and KMZ.
	my $kml_image_file_name = $file;
	if (defined $opt_kml_image_dir) {
		if ($opt_kml_image_dir =~ m,://,) {
			# File name is an URL.
			$kml_image_file_name = $opt_kml_image_dir . '/' . $fn;
		}
		else {
			# Normal file name.
			$kml_image_file_name =
				File::Spec->join($opt_kml_image_dir, $fn);
		}
	}
	my $kmz_image_file_name = File::Spec->join($kmz_image_dir, $fn);

	# Thumbnail file names in KML and KMZ.
	my $thumb_dir_absolute;
	my $thumb_file_absolute = $kml_image_file_name; # Default: the file itself.
	my $kml_thumb_file_name = $kml_image_file_name; # Default: the file itself.
	my $kmz_thumb_file_name = $kmz_image_file_name; # Default: the image in the KMZ itself.
	my $kmz_thumb_subdir = 'thumbs';
	my $kmz_thumb_dir = File::Spec->join($kmz_image_dir, $kmz_thumb_subdir);
	if (
		(
			exists $kml_image_type{'placemark'} ||
			exists $kml_image_type{'photooverlay'}
		) &&
		&$thumbnail_method()
	) {
		# Directory, where the thumbnail will end up on disk.
		if ($thumb_absolute) {
			$thumb_dir_absolute = $opt_thumb_dir;
		}
		else {
			my ($base, $dir, $ext) = fileparse($file,qr/\.[^.]*/);
			# print "$base $dir $ext\n";
			$thumb_dir_absolute = File::Spec->catdir($dir, $opt_thumb_dir);
		}
		unless (-d $thumb_dir_absolute) {
			unless (mkdir $thumb_dir_absolute) {
				die "Could not create directory for thumbnails '$thumb_dir_absolute': $!\n";
			}
		}

		# This is the place on disk, where the thumbnail is created.
		# It might be referenced differently according other options.
		$thumb_file_absolute = File::Spec->join($thumb_dir_absolute, $fn);

		# Create the thumbnail on disk.
		&$thumbnail_method($file, $thumb_file_absolute);

		# Thumbnail file names as referenced in KML and KMZ.
		$kml_thumb_file_name = $thumb_file_absolute; # Default: file itself.
		if (defined $opt_kml_image_dir) {

			# We already made sure, that $opt_thumb_dir is relative.
			if ($opt_kml_image_dir =~ m,://,) {
				# File name is an URL.
				$kml_thumb_file_name = $opt_kml_image_dir . '/' . $opt_thumb_dir . '/'. $fn;
			}
			else {
				# Normal file name.
				$kml_thumb_file_name =
					File::Spec->join($opt_kml_image_dir, $opt_thumb_dir, $fn);
			}
		}
		$kmz_thumb_file_name = File::Spec->join($kmz_image_dir, $fn);
	}

	my $kmz_embed_image = 0;
	my $kmz_embed_thumb = 0;

	if (exists $kml_image_type{'placemark'}) {
		if ($kml) {
			kml_write_image_placemark($kml_fh, $fn, $kml_image_file_name, $kml_thumb_file_name,
				$point, $image_landscape, $image_ratio);
		}
		if ($kmz) {
			kml_write_image_placemark($kmz_temp_kml_fh, $fn, $kmz_image_file_name, $kmz_thumb_file_name,
				$point, $image_landscape, $image_ratio);
			$kmz_embed_image++;
			$kmz_embed_thumb++;
		}
	}

	if (exists $kml_image_type{'screenoverlay'}) {
		if ($kml) {
			kml_write_image_screenoverlay($kml_fh, $fn, $kml_image_file_name,
				$image_landscape);
		}
		if ($kmz) {
			kml_write_image_screenoverlay($kmz_temp_kml_fh, $fn, $kmz_image_file_name,
				$image_landscape);
			$kmz_embed_image++;
		}
	}

	if (exists $kml_image_type{'groundoverlay'}) {
		if ($kml) {
			kml_write_image_groundoverlay($kml_fh, $fn, $kml_image_file_name,
				$point, $imgInfo);
		}
		if ($kmz) {
			kml_write_image_groundoverlay($kmz_temp_kml_fh, $fn, $kmz_image_file_name,
				$point, $imgInfo);
			$kmz_embed_image++;
		}
	}

	if (exists $kml_image_type{'photooverlay'}) {
		if ($kml) {
			kml_write_image_photooverlay($kml_fh, $fn, $kml_image_file_name, $kml_thumb_file_name,
				$point, $image_ratio);
		}
		if ($kmz) {
			kml_write_image_photooverlay($kmz_temp_kml_fh, $fn, $kmz_image_file_name, $kmz_thumb_file_name,
				$point, $image_ratio);
			$kmz_embed_image++;
			$kmz_embed_thumb++;
		}
	}

	if ($kmz) {
		if ($kmz_embed_image) {
			print "embedding $file, $kml_image_file_name\n";
			my $member = $kmz_zip->addFile($file, $kmz_image_file_name);
			unless (defined $member) {
				die "Can't add image file '$file' to the KMZ file.\n";
			}
			else {
				# Do not compress images.
				$member->desiredCompressionMethod(Archive::Zip->COMPRESSION_STORED);
			}
		}
		if ($kmz_embed_thumb) {
			print "embedding thumbnail $thumb_file_absolute, $kmz_thumb_file_name\n";
			my $member = $kmz_zip->addFile($thumb_file_absolute, $kmz_thumb_file_name);
			unless (defined $member) {
				die "Can't add thumbnail '$thumb_file_absolute' to the KMZ file.\n";
			}
			else {
				# Do not compress thumbnails.
				$member->desiredCompressionMethod(Archive::Zip->COMPRESSION_STORED);
			}
		}
	}

	if (scalar keys %kml_image_type > 1) {
		if ($kml) {
			kml_write_folder_end($kml_fh);
		}
		if ($kmz) {
			kml_write_folder_end($kmz_temp_kml_fh);
		}
	}
}

sub kml_write_image_placemark($$$$$$$)
{
	my ($fh, $_fn, $_file, $_thumb, $_point, $_landscape, $_ratio) = @_;

	my $thumb_scale;
	my $width;
	my $height;
	# The longer side is fixed to $opt_kml_placemark_thumbnail_size.
	if ($_landscape) {
		$width = $opt_kml_placemark_thumbnail_size;
		$height = $width * $_ratio;
	} else {
		$height = $opt_kml_placemark_thumbnail_size;
		$width = $height / $_ratio;
	}
	$thumb_scale=sprintf("width=\"%d\" height=\"%d\"", $width, $height);

	print $fh qq(
    <Placemark>
      <name>$_fn</name>
      <description><![CDATA[<a href="$_file"><img src="$_thumb" $thumb_scale /></a><br><a href="$_file">full size</a>);
	if (defined $_point->{iptc}) {
		print $fh "<br>";
		foreach my $opt (keys %{$_point->{iptc}}) {
			my $value = $_point->{iptc}->{$opt};
			printf $fh "<bf>$opt:</bf> $value<br>";
		}
	}
	print $fh qq(]]></description>
      <Snippet/>
      <LookAt>
        <longitude>$_point->{x}</longitude>
        <latitude>$_point->{y}</latitude>
        <range>10000</range>
        <tilt>50</tilt>
        <heading>0</heading>
      </LookAt>
      <styleUrl>#Photo</styleUrl>
      <Point>
        <altitudeMode>$kml_altitudeMode</altitudeMode>
        <coordinates>$_point->{x},$_point->{y},$_point->{z}</coordinates>
      </Point>
    </Placemark>);
}

sub kml_write_image_screenoverlay($$$$)
{

	my ($fh, $_fn, $_file, $_landscape) = @_;

	my $sx;
	my $sy;
	# The longer side must fill the screen.
	if ($_landscape) {
		$sx = 1;
		$sy = 0;
	}
	else {
		$sx = 0;
		$sy = 1;
	}

	print $fh qq(
	<Folder>
		<name>$_fn</name>
		<visibility>0</visibility>
		<open>1</open>
		<Style>
			<ListStyle>
				<listItemType>checkHideChildren</listItemType>
				<bgColor>00ffffff</bgColor>
			</ListStyle>
		</Style>
		<ScreenOverlay>
			<name>black background</name>
			<drawOrder>0</drawOrder>
			<color>ff000000</color>
			<overlayXY x="0.5" y="0.5" xunits="fraction" yunits="fraction"/>
			<screenXY x="0.5" y="0.5" xunits="fraction" yunits="fraction"/>
			<rotationXY x="0" y="0" xunits="fraction" yunits="fraction"/>
			<size x="1" y="1" xunits="fraction" yunits="fraction"/>
		</ScreenOverlay>
		<ScreenOverlay>
			<name>$_fn</name>
			<drawOrder>1</drawOrder>
			<Icon>
			<href>$_file</href>
			</Icon>
			<overlayXY x="0.5" y="0.5" xunits="fraction" yunits="fraction"/>
			<screenXY x="0.5" y="0.5" xunits="fraction" yunits="fraction"/>
			<rotationXY x="0" y="0" xunits="fraction" yunits="fraction"/>
			<size x="$sx" y="$sy" xunits="fraction" yunits="fraction"/>
		</ScreenOverlay>
	</Folder>
);
}

sub kml_write_image_groundoverlay($$$$$)
{

	my ($fh, $_fn, $_file, $_point, $_imgInfo) = @_;

	# Maybe these could become parameters:
	my $image_altitude = 100;	# Image floats above the placemark.
	my $image_range = 2200;		# I see the image from this distance.
	my $image_size = 1000;		# Long side of the image in the air in meter.

	my $alt = $image_altitude + $_point->{z}; # 100 meters above the picture.
	my $size_rad = $image_size / (6378000.0+$alt);
	my $size_deg = rad2deg($size_rad);

	# Default: a square picture.
	my $xf = 1.0;
	my $yf = 1.0;

	if (
		# We need all these image information.
		exists $_imgInfo->{ImageHeight} && $_imgInfo->{ImageHeight}
		&&
		exists $_imgInfo->{ImageWidth} && $_imgInfo->{ImageWidth}
	) {
		if ($_imgInfo->{ImageWidth} > $_imgInfo->{ImageHeight}) {
			$yf *= $_imgInfo->{ImageHeight}/$_imgInfo->{ImageWidth};
		}
		else {
			$xf *= $_imgInfo->{ImageWidth}/$_imgInfo->{ImageHeight};
		}
	}

	# Remember to rescale the longitude according to the cos(latitude).
	my $size_x = $size_deg / 2.0 * $xf / cos(deg2rad($_point->{y}));
	my $size_y = $size_deg / 2.0 * $yf;

	my $west = $_point->{x} - $size_x;
	my $east = $_point->{x} + $size_x;
	my $north = $_point->{y} + $size_y;
	my $south = $_point->{y} - $size_y;

	# The altitude of the GroundOverlay is considerably wrong.
	# I assume it is in feet instead of in meters.
	$alt *= 100.0/(12.0 * 2.54);

	print $fh qq(
	<GroundOverlay>
	<name>$_fn</name>
	<visibility>0</visibility>
	<LookAt>
		<longitude>$_point->{x}</longitude>
		<latitude>$_point->{y}</latitude>
		<altitude>$_point->{z}</altitude>
		<range>$image_range</range>
		<tilt>0</tilt>
		<heading>0</heading>
		<altitudeMode>absolute</altitudeMode>
	</LookAt>
	<Icon>
		<href>$_file</href>
		<viewBoundScale>0.75</viewBoundScale>
	</Icon>
	<altitude>$alt</altitude>
	<altitudeMode>absolute</altitudeMode>
        <LatLonBox>
                <north>$north</north>
                <south>$south</south>
                <east>$east</east>
                <west>$west</west>
        </LatLonBox>
	</GroundOverlay>
);
}

sub kml_write_image_photooverlay($$$$$$)
{
	my ($fh, $_fn, $_file, $_thumb, $_point, $_image_ratio) = @_;

	my $thumb_scale;
	my $ah;
	my $av;
	# The longer side is fixed to $opt_kml_placemark_thumbnail_size.
	# The longer side is fixed to 25 deg.
	# print "ratio=$_image_ratio\n";
	if ($_image_ratio>1) {
		# Portrait mode.
	 	# print "Portrait\n";
		my $height = $opt_kml_placemark_thumbnail_size;
		my $width = $height / $_image_ratio;
		$thumb_scale=sprintf("width=\"%d\" height=\"%d\"", $width, $height);
		$av = 25.0;
		$ah = rad2deg(atan(tan(deg2rad($av) / $_image_ratio), 1));
	} else {
		# Landscape mode.
	 	# print "Landscape\n";
		my $width = $opt_kml_placemark_thumbnail_size;
		my $height = $width * $_image_ratio;
		$thumb_scale=sprintf("width=\"%d\" height=\"%d\"", $width, $height);
		$ah = 25.0;
		$av = rad2deg(atan(tan(deg2rad($ah) * $_image_ratio), 1));
	}
	# print "$ah, $av\n";

	print $fh qq(
    <PhotoOverlay id="$_fn">
      <name>$_fn</name>
      <description><![CDATA[<a href="#$_fn"><img src="$_thumb" $thumb_scale /></a><br><a href="#$_fn">full size</a>);
	if (defined $_point->{iptc}) {
		print $fh "<br>";
		foreach my $opt (keys %{$_point->{iptc}}) {
			my $value = $_point->{iptc}->{$opt};
			printf $fh "<bf>$opt:</bf> $value<br>";
		}
	}
	print $fh qq(]]></description>
      <Snippet/>
      <Camera>
        <longitude>$_point->{x}</longitude>
        <latitude>$_point->{y}</latitude>
        <altitude>$_point->{z}</altitude>
        <heading>-1.216422395190395e-13</heading>
        <tilt>90.0</tilt>
        <roll>-3.49861014960987e-14</roll>
      </Camera>
      <styleUrl>#Photo</styleUrl>
      <Icon>
              <href>$_file</href>
      </Icon>
      <ViewVolume>
              <leftFov>-$ah</leftFov>
              <rightFov>$ah</rightFov>
              <bottomFov>-$av</bottomFov>
              <topFov>$av</topFov>
              <near>10</near>
      </ViewVolume>
      <Point>
        <altitudeMode>$kml_altitudeMode</altitudeMode>
        <coordinates>$_point->{x},$_point->{y},$_point->{z}</coordinates>
      </Point>
    </PhotoOverlay>);
}

sub kml_write_photo_footer($)
{

	my ($fh) = @_;

	print $fh qq(
  </Folder>);
}

sub kml_write_track_line($)
{
	my ($fh) = @_;

	# 0: No track at all.
	return unless $opt_kml_track_enable;

	# Output all or decide later.
	my $used_all = $opt_kml_track_enable & 0x01;
	my $text_all = '';
	my $index = 0;

	$text_all .= qq(
  <Folder>
    <name>Tracks</name>
    <open>0</open>);

	foreach my $gpsfile (sort keys %gpsTracks) {
		# Output file or decide later.
		my $used_file = $opt_kml_track_enable & 0x01;
		my $text_file = '';
		my $fn = (File::Spec->splitpath( $gpsfile ))[2];
		my $segref = $gpsTracks{$gpsfile};
		$text_file .= qq(
  <Folder>
    <name>$fn</name>);
		my $segment = 1;
		foreach my $trackref (@{$segref}) {
			# Output segment or decide later.
			my $used_segment = $opt_kml_track_enable & 0x01;
			my $text_segment = '';
			my $track_color = $opt_kml_track_color[$index];
			$text_segment .= qq(
    <Placemark>
      <name>Track Segment $segment</name>
      <visibility>1</visibility>
      <Style>
        <LineStyle>
          <color>$track_color</color>
          <width>4</width>
        </LineStyle>
        <PolyStyle>
          <color>$track_color</color>
        </PolyStyle>
      </Style>
      <LineString>
        <extrude>$kml_extrude</extrude>
        <tessellate>1</tessellate>
        <altitudeMode>$kml_altitudeMode</altitudeMode>
        <coordinates>);

			my $cpt=1;
			foreach (@{$trackref}) {
				$text_segment .= "</coordinates><coordinates>\n" if($cpt%200==0);
				$text_segment .= "$_->{x}, $_->{y}, $_->{z}\n";
				if ($_->{used}) {
					$used_segment = 1;
				}
			}

			$text_segment .= qq(        </coordinates>
      </LineString>
    </Placemark>);
			if ($used_segment) {
				$used_file = 1;
				$text_file .= $text_segment;
				$index = ($index+1) % (scalar @opt_kml_track_color);
				$segment++;
			}
		} # End for segments.
		$text_file .= qq(
  </Folder>);
		if ($used_file) {
			$used_all = 1;
			$text_all .= $text_file;
		}
	} # End for files.

	$text_all .= qq(
  </Folder>);

	if ($used_all) {
		$fh->print($text_all);
	}
}

sub kml_write_track_timeline($)
{
	my ($fh) = @_;

	return unless $opt_kml_timeline;

	print $fh qq(
	<Folder>
		<name>Timeline</name>
		<visibility>0</visibility>
		<open>1</open>
		<Style>
			<ListStyle>
				<listItemType>checkHideChildren</listItemType>
				<bgColor>00ffffff</bgColor>
			</ListStyle>
		</Style>

);
	for (my $trackpoint=1;$trackpoint<=scalar @gpsData;$trackpoint++) {
		my $point = $gpsData[$trackpoint-1];
		print $fh qq(
		<Placemark>
			<Snippet/>
			<description><![CDATA[<b>trackpoint #$trackpoint</b><br/> <i>Latitude:</i> $point->{y} &#176;<br/> <i>Longitude:</i> $point->{x} &#176
;<br/> <i>Time:</i> $point->{dt}]]></description>
			<TimeStamp>
				<when>$point->{dt}</when>
			</TimeStamp>
			<styleUrl>#timed_track_point</styleUrl>
			<Point>
				<altitudeMode>$kml_altitudeMode</altitudeMode>
				<coordinates>$point->{x},$point->{y},$point->{z}</coordinates>
			</Point>
		</Placemark>
);
	}
	print $fh qq(
	</Folder>
);
}

sub kml_write_about($)
{
	my ($fh) = @_;

	print $fh qq(
	<Folder>
		<name>About</name>
		<visibility>0</visibility>
		<description><![CDATA[<p>Created with $program $source_release.</p>
<p>For further information, please visit the home page at:
<a href="http://www.carto.net/projects/photoTools/gpsPhoto/">http://www.carto.net/projects/photoTools/gpsPhoto/</a>.</p>
<p>To report an error please use the project page <a href="http://sourceforge.net/projects/gps2photo/">http://sourceforge.net/projects/gps2photo/</a> at <a href="http://sourceforge.net">SourceForge</a>.</p>]]></description>
		<Snippet>Created with gpsPhoto.pl.</Snippet>
	</Folder>
);
}

sub kml_write_footer($)
{
	my ($fh) = @_;

	print $fh qq(
</Document>
</kml>
);
}

sub kml_close($$)
{
	my ($fh, $file) = @_;

	close($fh) or die "Can't close file $file: $!.\n";
}

sub binary_search_s($$)
{
        my ($array,$target)=@_;
        my ($low,$high)=(0,scalar @{$array});
        while ($low<$high) {
                use integer;
                my $cur=($low+$high)/2;
		if ($array->[$cur]->{s}<$target) {
			$low=$cur+1;
		}
		else {
			$high=$cur;
		}
        }
        return $low;
}

sub interpolate_factor($$$)
{
	my ($t1, $t2, $t) = @_;
	die "$t is outside [$t1,$t2]" if $t<$t1 || $t>$t2;
	my $f = 1.0*($t-$t1)/($t2-$t1);
	# print "$t is in [$t1,$t2] at $f.\n";
	return $f;
}

sub interpolate_calc($$$)
{
	my ($x1, $x2, $f) = @_;
	my $x = 0.0 + $x1 + 1.0 * ($x2-$x1) * $f;
	# print "Interpolate in [$x1,$x2] with $f => $x.\n";
	return $x;
}

sub interpolate_linear($$$)
{
	my ($a, $b, $way) = @_;
	my $point = {};

	$point->{x} = interpolate_calc(
		$a->{x},
		$b->{x},
		$way);
	$point->{y} = interpolate_calc(
		$a->{y},
		$b->{y},
		$way);
	$point->{z} = interpolate_calc(
		$a->{z},
		$b->{z},
		$way);

	return $point;
}


# The function great_circle_waypoint() in Math/Trig.pm may be wrong.
# It is corrected in the Math-Complex-1.37 module.
{
	my $result = undef;

sub test_great_circle_waypoint()
{
	if (!defined $result) {
		my $theta0=0.0;
		my $phi0=0.0;
		my $theta1=1.0;
		my $phi1=1.0;
		my $way=0.5;
		my ($thetai, $phii) =
			great_circle_waypoint($theta0, $phi0, $theta1, $phi1, $way);
		if ($thetai<$theta0 || $thetai>$theta1 || $phii<$phi0 || $phii>$phi1 ) {
			print STDERR "WARNING: great_circle_waypoint() does not work correctly.\n";
			print STDERR "WARNING: Please install Math-Complex-1.37 or higher.\n";
			print STDERR "WARNING: I will performing the linear interpolation instead.\n";
			$result = 0;
		}
		else {
			$result = 1;
		}
	}
	return $result;
}

}

sub interpolate_great_circle($$$)
{
	if (test_great_circle_waypoint()==0) {
		$interpolate = \&interpolate_linear;
		return &{$interpolate}(@_);
	}
	my ($a, $b, $way) = @_;
	my $point = {};

	# printf "interval deg %f,%f %f,%f way %f\n", $a->{x}, $a->{y}, $b->{x}, $b->{y}, $way;
	my ($theta_a, $phi_a) = NESW($a->{x},$a->{y});
	my ($theta_b, $phi_b) = NESW($b->{x},$b->{y});
	# printf "interval rad %f,%f %f,%f way %f\n", $theta_a, $phi_a, $theta_b, $phi_b, $way;
	my ($theta_w, $phi_w) =
		great_circle_waypoint($theta_a, $phi_a, $theta_b, $phi_b, $way);
	# printf "result rad %f,%f\n", $theta_w, $phi_w;
	$point->{x} = rad2deg($theta_w);
	$point->{y} = rad2deg(pip2-$phi_w);
	# printf "result deg %f,%f\n", $point->{x}, $point->{y};
	$point->{z} = interpolate_calc(
		$a->{z},
		$b->{z},
		$way);

	return $point;
}

sub uniq(@)
{
	my %seen = ();
	my @result = grep { ! $seen{$_} ++ } @_;
	return @result;
}

sub set_option_hashlist($$$$)
{
	my ($option, $value, $values, $ref) = @_;
	if ($value eq 'list') {
		print join (' ', @{$values}) , "\n";
		exit(0);
	}
	my $found = 0;
	for (@{$values}) {
		if ($value eq $_) {
			$ref->{$_} = 1;
			$found = 1;
			last;
		}
	}
	if (!$found) {
		die "Option $option, unknown value $value.\n";
	}
}

sub set_option_radiolist($$$$)
{
	my ($option, $value, $values, $ref) = @_;
	if ($value eq 'list') {
		print join(' ', keys %{$values}), "\n";
		exit(0);
	}
	if (exists $values->{$value}) {
		${$ref} = $values->{$value};
	}
	else {
		die "Option $option, unknown value $value. Try list for a list.\n";
	}
}

sub set_kml_image_type($$)
{
	my ($option, $value) = @_;
	my @values = ('placemark', 'screenoverlay', 'groundoverlay', 'photooverlay');
	set_option_hashlist($option, $value, \@values, \%kml_image_type);
}

sub set_opt_kml_track_enable($$)
{
	my ($option, $value) = @_;
	my %values = (
		'all'		=> 0x01,
		'1'		=> 0x01,
		'usedsegment'	=> 0x12,
		'none'		=> 0x00,
		'0'		=> 0x00,
	);
	set_option_radiolist($option, $value, \%values, \$opt_kml_track_enable);
}

sub set_opt_kml_track_color($$)
{
	my ($option, $value) = @_;
        for my $v (split /,/, $value) {
                if ($v =~ /^[\dabcdef]{8}$/i) {
                        push @opt_kml_track_color, lc($v);
                }
                elsif ($v =~ /^static6$/) {
			push @opt_kml_track_color,
				'7f0000ff',
				'7f00ffff',
				'7f00ff00',
				'7fffff00',
				'7fff0000',
				'7fff00ff',
			;
		}
                elsif ($v =~ /^static12$/) {
			push @opt_kml_track_color,
				'7f0000ff',
				'7f007fff',
				'7f00ffff',
				'7f00ff7f',
				'7f00ff00',
				'7f7fff00',
				'7fffff00',
				'7fff7f00',
				'7fff0000',
				'7fff007f',
				'7fff00ff',
				'7f7f00ff',
			;
		}
		else {
                        die "Option $option: '$v' is neither a 8 digit hex number nor static6 or static12.\n";
                }
        }
}

sub set_kml_placemark_thumbnail_method($$)
{
	my ($option, $value) = @_;
	my %values = (
		'none' => \&thumbnail_none,
		'convert' => \&thumbnail_convert,
	);
	set_option_radiolist($option, $value, \%values, \$thumbnail_method);
}

sub set_opt_select($$)
{
	my ($option, $value) = @_;
	my %values = (
		'geotag' => 'geotag',
		'nogeotag' => 'nogeotag',
		'any' => 'any',
	);
	set_option_radiolist($option, $value, \%values, \$opt_select);
}

sub set_IPTC_tag($$)
{
	my ($option, $value) = @_;
	my $got_it = 0;
	foreach my $iptc (@IPTC) {
		if ($iptc->opt() eq $option) {
			$got_it = 1;
			$iptc->set_val($opt_select, $value);
			last;
		}
	}
	if (!$got_it) {
		die "Unknown IPTC option '$option'\n";
	}
}

sub get_IPTC_tag($)
{
	my ($tag, $point) = @_;
	my $value = undef;
	my $got_it = 0;
	foreach my $iptc (@IPTC) {
		next if $iptc->tag() ne $tag;
		$got_it = 1;
		$value = $iptc->get_val(1);
		last;
	}
	if (!$got_it) {
		die "get_IPTC_tag($tag): unknown IPTC tag.\n";
	}
	return $value;
}

sub set_tz_guess($$)
{
	my ($option, $value) = @_;
	my %values = (
		'15deg' => \&tz_guess_15deg,
		'zone.tab' => \&tz_guess_zone_tab,
	);
	set_option_radiolist($option, $value, \%values, \$tz_guess);
}

sub set_report_distance($$)
{
	my ($option, $value) = @_;
	my %values = (
		'none' => \&report_distance_none,
		'km' => \&report_distance_km,
		'miles' => \&report_distance_miles,
		'nautical' => \&report_distance_nautical,
	);
	set_option_radiolist($option, $value, \%values, \$report_distance);
}

sub set_report_direction($$)
{
	my ($option, $value) = @_;
	my %values = (
		'none' => \&report_direction_none,
		'degree' => \&report_direction_degree,
		'4' => \&report_direction_4,
		'8' => \&report_direction_8,
	);
	set_option_radiolist($option, $value, \%values, \$report_direction);
}

sub set_geoinfo($$)
{
	my ($option, $value) = @_;
	my %values = (
		'none' => \&get_geoinfo_none,
		'geourl' => \&get_geoinfo_geourl,
		'geonames' => \&get_geoinfo_geonames,
		'wikipedia' => \&get_geoinfo_wikipedia,
		'osm' => \&get_geoinfo_osm,
		'zip' => \&get_geoinfo_zip,
	);
	set_option_radiolist($option, $value, \%values, \$get_geoinfo);
}

sub set_geotag_source($$)
{
	my ($option, $value) = @_;
	my @values = ('exif', 'track', 'option');
	set_option_hashlist($option, $value, \@values, \%geotag_source);
}

sub set_image_action($$)
{
	my ($option, $value) = @_;
	if ($option eq 'delete-geotag') {
		$image_action = \&image_action_delete_geotag;
	}
}

sub set_interpolate($$)
{
	my ($option, $value) = @_;
	my %values = (
		'none' => undef,
		'linear' => \&interpolate_linear,
		'great-circle' => \&interpolate_great_circle,
	);
	set_option_radiolist($option, $value, \%values, \$interpolate);
}

sub set_image_file_time($$)
{
	my ($option, $value) = @_;
	my %values = (
		'modify' => \&image_file_time_modify,
		'exif' => \&image_file_time_exif,
		'keep' => \&image_file_time_keep,
	);
	set_option_radiolist($option, $value, \%values, \$image_file_time);
}

# Initialize it as empty.
my @cur_track = ();
my $cur_point;

sub Parser_process_node($@)
{
	my ($gpsfile, $type, $content) = @_;

	# print STDERR "$type\n";

	if ($type eq 'gpx' or $type eq 'trk') {
		# If there were waypoints between the track segments, they
		# must be stored as well.
		if (scalar @cur_track) {
			store_segment($gpsfile,@cur_track);
		}
		# Start with a new empty array.
		@cur_track=();
		# Recurse.
		while (my @node=splice @$content,1,2) {
			Parser_process_node($gpsfile,@node);
		}
		# Waypoints are not part of a track segment. They must be put
		# into database here.
		if (scalar @cur_track) {
			store_segment($gpsfile,@cur_track);
			@cur_track=();
		}
	} elsif ($type eq 'trkseg') {
		@cur_track=();
		while (my @node=splice @$content,1,2) {
			Parser_process_node($gpsfile,@node);
		}
		store_segment($gpsfile,@cur_track);
		@cur_track=();
	} elsif ($type eq 'trkpt' or $type eq 'wpt') {
		# Take any track point or way point.
		my $attrs = $content->[0];
		$cur_point={};
		$cur_point->{x}=$attrs->{lon};
		$cur_point->{y}=$attrs->{lat};
		while (my @node=splice @$content,1,2) {
			Parser_process_node($gpsfile,@node);
		}
		# Only points with time are needed.
		if (exists $cur_point->{dt}) {
			# Fabricate a height, if there is no.
			if (!exists $cur_point->{z}) {
				$cur_point->{z} = 0;
			}
			$lineCounter++;
			push @cur_track,$cur_point;
		}
	} elsif ($type eq 'ele') {
		$cur_point->{z}=int($content->[2] + 0.5);
	} elsif ($type eq 'time') {
		$cur_point->{dt} = $content->[2];
	}
}

sub store_segment($@)
{
	my ($gpsfile, @track) = @_;

	# Prepare date and time elements.
	foreach my $point (@track) {
		# printf STDERR "dt %s\n", $point->{dt};
		($point->{d}, $point->{t}) = util::dtexpand($point->{dt});
		# printf STDERR "d %s t %s\n", $point->{d}, $point->{t};
		my ($year,$month,$day) = split(/-/,$point->{d});
		my ($hour,$minute,$second) = split(/:/,$point->{t});
		my $secs = timegm($second,$minute,$hour,$day,$month-1,$year);
		$point->{s} = $secs;
	}

	# Append all current track segment data to the global
	# database.
	push @gpsData, @track;

	# Sort current track segement.
	@track = sort { $a->{s} <=> $b->{s} } @track;

	# Create a array reference, if it does not yet exist.
	if (!exists $gpsTracks{$gpsfile}) {
		$gpsTracks{$gpsfile} = ();
	}

	# Append the sorted track segment.
	push @{$gpsTracks{$gpsfile}}, \@track;

	printf " %d", scalar @track;
}

sub tz_guess_15deg($)
{
	my ($point) = @_;
	my $lon_deg = $point->{x};
	my $hour = floor($lon_deg/15.0 + 0.5);
	my $tz = 'GMT';
	if ($hour>0) {
		$tz .= '+';
	}
	if ($hour!=0) {
		$tz .= $hour;
	}
	my $offset = -3600 * $hour;
	printf "Guess TZ from Longitude=%f°:\nTZ=%s --timeoffset=%d\n", $lon_deg, $tz, $offset;
	return $offset;
}

sub NESW { deg2rad($_[0]), deg2rad(90 - $_[1]) }

sub tz_guess_zone_tab($)
{
	my ($point) = @_;

	my $zonefile = '/usr/share/zoneinfo/zone.tab';

	open (ZONE, $zonefile) || die "Can't open $zonefile for reading: $!\n";

	my $sourcelatdec = $point->{y};
	my $sourcelondec = $point->{x};

	my $r = 6378;   #radius of earth in kilometers

	my $closest = 999999;
	my $tzname;
	my $cc;

	my @source = NESW($sourcelondec, $sourcelatdec);

	my $closelatdec = 0;
	my $closelondec = 0;

	while (my $line = <ZONE>) {
		next if $line =~ /^\s*#/;
		# EC -0054-08936 Pacific/Galapagos Galapagos Islands
		if ($line !~ /^(\S+)\s+([+-]\d+)([+-]\d+)\s+(\S+)\s*/) {
			die "File $zonefile, line $.. Can't interpret '$line'.\n";
		}
		my $cur_cc = $1;
		my $lat = $2;
		my $lon = $3;
		my $cur_tzname = $4;

		my $latref = 1;
		my $lonref = 1;
		my ($londec, $latdec) = 0;
		
		if ($lat < 0) { 
                	$latref = -1;
               	}

		if ($lon < 0) {
			$lonref = -1;
		}

		if (length($lat) == 5) {
			$latdec = sprintf("%.4f",$latref * (substr($lat,1,2) + substr($lat,3,2)/60));
		} elsif (length($lat) == 7) {
			$latdec = sprintf("%.4f",$latref * (substr($lat,1,2) + substr($lat,3,2)/60 + substr($lat,5,2)/3600));
		} else {
			die "Unknown latitude $lat\n";
		}

		if (length($lon) == 6) {
			$londec = sprintf("%.4f",$lonref * (substr($lon,1,3) + substr($lon,4,2)/60));
		} elsif (length($lon) == 8)  {
			$londec = sprintf("%.4f",$lonref * (substr($lon,1,3) + substr($lon,4,2)/60 + substr($lon,5,2)/3600));
		} else {
			die "Unknown longitude $lon\n";
		}

		my @dest = NESW($londec, $latdec);
		my $dist = great_circle_distance(@source,@dest,$r);

		if ($closest > $dist) {
			$closest = $dist;
			$tzname = $cur_tzname;
			$cc = $cur_cc;
			$closelatdec = $latdec;
			$closelondec = $londec;
		}
	}

	# Expand time as GMT.
	my ($g_sec,$g_min,$g_hour,
	$g_mday,$g_mon,$g_year,$g_wday,$g_yday,$g_isdst) = gmtime($point->{s});

	# Set tzname.
	tzset();
	# Get current TZ.
	my ($old_std, $old_dst) = tzname();
	# Set a different TZ.
	$ENV{TZ} = $tzname;
	# Set tzname.
	tzset();

	# Interpret time as localtime.
	my $local_s = timelocal($g_sec,$g_min,$g_hour,$g_mday,$g_mon,$g_year);

	# Reset old TZ.
	$ENV{TZ} = $old_std;
	# Set tzname.
	tzset();

	my $offset = $local_s - $point->{s};

	printf "Guess TZ from Pos=(%f°,%f°) at %s %s\nClosest=(%f°,%f°) Dist=%fkm\nTZ=%s, --timeoffset=%d\n",
		$sourcelatdec, $sourcelondec,
		$point->{d}, $point->{t},
		$closelatdec, $closelondec,
		$closest,
		$tzname,
		$offset;

	return $offset;
}

sub report_distance_none($$$)
{
	my ($place, $distance, $direction) = @_;
	if (defined $direction) {
		return sprintf "%s of %s", $direction, $place;
	}
	else {
		return $place;
	}
}

sub report_distance_gen($$$$$)
{
	my ($unit, $scale, $place, $distance, $direction) = @_;
	if (defined $distance) {
		$distance = $distance / $scale;
		if ($distance < 0.05) {
			return sprintf "Taken at %s", $place;
		}
		else {
			if (defined $direction) {
				return sprintf "%.01f %s %s of %s", $distance, $unit, $direction, $place;
			}
			else {
				return sprintf "%.01f %s from %s", $distance, $unit, $place;
			}
		}
	}
	else {
		return report_distance_none($place, $distance, $direction);
	}
}

sub report_distance_km($$$)
{
	report_distance_gen("km",1.0,$_[0],$_[1],$_[2]);
}

sub report_distance_miles($$$)
{
	report_distance_gen("miles",1.609344,$_[0],$_[1],$_[2]);
}

sub report_distance_nautical($$$)
{
	report_distance_gen("nautical miles",1.852,$_[0],$_[1],$_[2]);
}

sub report_direction_none($)
{
	my ($direction) = @_;
	return undef;
}

sub report_direction_degree($)
{
	my ($direction) = @_;
	return sprintf '%i degree', rad2deg($direction);
}

sub report_direction_4($)
{
	my ($direction) = @_;
	my $open = pip2;
	my $diff = $open/2;
	my %dirs = (
		0.0 => 'N',
		pip2() => 'E',
		pi() => 'S',
		3*pip2() => 'W',
	);
	my $text=undef;
	my $dir;
	for my $dir (keys %dirs) {
		if ($direction>=$dir-$diff && $direction<=$dir+$diff) {
			$text=$dirs{$dir};
			last;
		}
	}
	return $text;
}

sub report_direction_8($)
{
	my ($direction) = @_;
	my $open = pip4;
	my $diff = $open/2;
	my %dirs = (
		0.0 => 'N',
		pip4() => 'NE',
		pip2() => 'E',
		3*pip4() => 'SE',
		pi() => 'S',
		5*pip4() => 'SW',
		3*pip2() => 'W',
		7*pip4() => 'NW',
		
	);
	my $text=undef;
	my $dir;
	for my $dir (keys %dirs) {
		if ($direction>=$dir-$diff && $direction<=$dir+$diff) {
			$text=$dirs{$dir};
			last;
		}
	}
	return $text;
}

{

my $readline=();

sub expand_iptc_value($$$)
{
	my ($iptc, $point, $geoinfo) = @_;

	my $val = $iptc->get_val($point);

	return undef unless defined $val;

	my $value = undef;
	if (
		$val eq 'guess' ||
		$val eq 'auto' ||
		$val eq 'manual'
	) {
		unless (defined $geoinfo) {
			my $lat = $point->{y};
			my $lon = $point->{x};
			return undef unless ($lat && $lon);
			$geoinfo = &{$get_geoinfo}($lat,$lon,$geturl);
			unless (defined $geoinfo) {
				die "Problem getting geoinfo for point $point->{y},$point->{x}.\n";
			}
		}
		if (exists $geoinfo->{$iptc->opt()}) {
			$value = $geoinfo->{$iptc->opt()};
			if ($val eq 'manual') {
				# Allow changing of $value.
				require Term::ReadLine;
				unless (defined $readline) {
					$readline = new Term::ReadLine $iptc->opt();
				}
				if (defined $readline) {
					# printf "readline=%s\n", $readline->ReadLine;
					my $manual;
					my $prompt;
					if ($readline->Features->{preput}) {
						# print "can preput\n";
						$prompt = sprintf "%s=", $iptc->opt();
						$manual = $readline->readline($prompt, $value);
					}
					else {
						# print "cannot preput\n";
						$prompt = sprintf "%s=%s", $iptc->opt(), $value;
						$manual = $readline->readline($prompt);
					}
					if (defined $manual && $manual ne '') {
						$value = $manual;
						if (!exists $readline->Features->{autohistory}) {
							# print "no autohistory\n";
							$readline->addhistory($manual);
						}
					}
				}
				else {
					printf "Problem initializing Readline library.\n";
				}
			}
			printf "Guess %s=%s\n", $iptc->opt(), $value;
		}
		else {
			$value = undef;
		}
	}
	else {
		$value = $val;
	}
	return $value;
}

}

sub fill_city($$$)
{
	my ($geo_info, $place_name, $distance) = @_;
	my $direction_text = undef;
	if (
		exists $geo_info->{lat} &&
		exists $geo_info->{lon} &&
		exists $geo_info->{target_lat} &&
		exists $geo_info->{target_lon}
	) {
		my $direction = great_circle_direction(
			NESW(
				$geo_info->{target_lon},
				$geo_info->{target_lat}
			),
			NESW(
				$geo_info->{lon},
				$geo_info->{lat}
			));
		# The result of great_circle_direction() is the result of rad2rad().
		# This means -2pi..2pi. We have to normalize this to [0..2pi).
		if ($direction<0) { $direction+=pi2(); }
		$direction_text = &$report_direction($direction);
		if (0) {
			printf STDERR "%f,%f -> %f,%f: %f. %s.\n", 
				$geo_info->{lat},$geo_info->{lon},
				$geo_info->{target_lat},$geo_info->{target_lon},
				$direction, $direction_text;
		}
		
	}
	my $city = &{$report_distance}($place_name, $distance, $direction_text);

	$geo_info->{city} = $city
}

sub get_geoinfo_geourl($$$)
{
	my ($lat, $lon, $geturl) = @_;
	my $geo_info = ();
	$geo_info->{lat} = $lat;
	$geo_info->{lon} = $lon;

	my $text = $geturl->("http://geourl.org/near/?lat=$lat\&long=$lon;format=rss10");
	return undef unless defined $text;

	#  Possibly write a log for fakefile.
	if (0) {
		open LOG, ">rsslog";
		print LOG $text;
		close LOG;
	}

	# Reduce answer text to a short block.
	if ($text && $text =~ /Sites near[\d\-\.,\s]+\(([^\)]+?)\)/) {
		# Define distance.
		my $distance = $text;

		$text = $1;
		# Ignore the 'Near' word.
		$text =~ s/^Near\s*//;
		# print ">>$text<<\n";

		# Get distance.
		if ($distance =~ /About (.*)? km/) {
			$distance = $1;
		}
		else {
			$distance = undef;
		}

		# Select city and state/country.
		if ($text =~ /([^,]+),\s+(.*)/) {
			fill_city($geo_info, $1, $distance);
			my $provice_state = $2;
			if ($provice_state =~ /([^,]+),\s*(.*)/) {
				$geo_info->{state} = $1;
				$geo_info->{country} = $2;
			}
			else {
				$geo_info->{country} = $provice_state;
			}
		}
	}
	return $geo_info;
}

sub get_geoinfo_geonames($$$)
{
	my ($lat, $lon, $geturl) = @_;
	my $geo_info = ();
	$geo_info->{lat} = $lat;
	$geo_info->{lon} = $lon;

	my $text;
	my $url = "http://ws.geonames.org/findNearbyPlaceName?style=full\&lat=$lat\&lng=$lon";
	if (defined $opt_language) {
		$url .= "\&lang=$opt_language";
	}
	$text = $geturl->($url);
	return undef unless defined $text;
	my $distance = undef;
	if ($text =~ m,<distance>([^<]+)</distance>,) {
		$distance = sprintf("%.01f",$1);
	}
	if ($text =~ m,<lat>([^<]+)</lat>,) {
		$geo_info->{target_lat} = $1;
	}
	if ($text =~ m,<lng>([^<]+)</lng>,) {
		$geo_info->{target_lon} = $1;
	}
	if ($text =~ m,<name>([^<]+)</name>,) {
		fill_city($geo_info, $1, $distance);
	}
	if ($text =~ m,<countryName>([^<]+)</countryName>,) {
		$geo_info->{country} = $1;
	}
	if ($text =~ m,<adminName1>([^<]+)</adminName1>,) {
		$geo_info->{state} = $1;
	}

	return $geo_info;
}

sub get_geoinfo_wikipedia($$$)
{
	my ($lat, $lon, $geturl) = @_;
	my $geo_info = ();
	$geo_info->{lat} = $lat;
	$geo_info->{lon} = $lon;

	my $text;
	my $url = "http://ws.geonames.org/findNearbyPlaceName?style=full\&lat=$lat\&lng=$lon";
	if (defined $opt_language) {
		$url .= "\&lang=$opt_language";
	}
	$text = $geturl->($url);
	return undef unless defined $text;
	my $distance = undef;
	if ($text =~ m,<distance>([^<]+)</distance>,) {
		$distance = $1;
	}
	if ($text =~ m,<lat>([^<]+)</lat>,) {
		$geo_info->{target_lat} = $1;
	}
	if ($text =~ m,<lng>([^<]+)</lng>,) {
		$geo_info->{target_lon} = $1;
	}
	if ($text =~ m,<name>([^<]+)</name>,) {
		fill_city($geo_info, $1, $distance);
	}
	if ($text =~ m,<countryName>([^<]+)</countryName>,) {
		$geo_info->{country} = $1;
	}
	if ($text =~ m,<adminName1>([^<]+)</adminName1>,) {
		$geo_info->{state} = $1;
	}

	$url = "http://ws.geonames.org/findNearbyWikipedia?lat=$lat\&lng=$lon\&maxRows=1\&radius=20";
	if ($opt_language) {
		$url .= "\&lang=$opt_language";
	}
	$text = $geturl->($url);
	my $wikidistance = undef;
	if ($text =~ m,<distance>([^<]+)</distance>,) {
		$wikidistance = $1;
	}
	if ( defined $wikidistance && defined $distance && $wikidistance < $distance ) {
		delete $geo_info->{target_lat};
		delete $geo_info->{target_lon};
		if ($text =~ m,<lat>([^<]+)</lat>,) {
			$geo_info->{target_lat} = $1;
		}
		if ($text =~ m,<lng>([^<]+)</lng>,) {
			$geo_info->{target_lon} = $1;
		}
		if ($text =~ m,<title>([^<]+)</title>,) {
			fill_city($geo_info, $1, $wikidistance);
		}
		if ($text =~ m,<summary>([^<]+)</summary>,) {
			$geo_info->{caption} = $1;
		}
	}

	return $geo_info;
}

sub get_geoinfo_osm($$$)
{
	my ($lat, $lon, $geturl) = @_;
	my $geo_info = get_geoinfo_geonames($lat, $lon, $geturl);
	my $url = "http://www.frankieandshadow.com/osm/search.xml?find=.+near+$lat%2C$lon";
	my $text = $geturl->($url);
#	print $text;
#	exit;
	if ($text =~ m,<named\s.*name='([^']+)',) {
		$geo_info->{sublocation} = $1;
	}
	return $geo_info;
}

sub get_geoinfo_zip($$$)
{
	my ($lat, $lon, $geturl) = @_;
	my $geo_info = ();
	$geo_info->{lat} = $lat;
	$geo_info->{lon} = $lon;

	my $text = $geturl->("http://ws.geonames.org/findNearbyPlaceName?style=full&lat=$lat\&lng=$lon");
	return undef unless defined $text;
	my $distance = undef;
	if ($text =~ m,<distance>([^<]+)</distance>,) {
		$distance = $1;
	}
	if ($text =~ m,<lat>([^<]+)</lat>,) {
		$geo_info->{target_lat} = $1;
	}
	if ($text =~ m,<lng>([^<]+)</lng>,) {
		$geo_info->{target_lon} = $1;
	}
	if ($text =~ m,<name>([^<]+)</name>,) {
		fill_city($geo_info, $1, $distance);
	}
	if ($text =~ m,<countryName>([^<]+)</countryName>,) {
		$geo_info->{country} = $1;
	}
	if ($text =~ m,<adminName1>([^<]+)</adminName1>,) {
		$geo_info->{state} = $1;
	}

	$text = $geturl->("http://ws.geonames.org/findNearbyPostalCodes?lat=$lat\&lng=$lon\&maxRows=1");
	my $zipdistance = undef;
	if ($text =~ m,<distance>([^<]+)</distance>,) {
		$zipdistance = $1;
		delete $geo_info->{target_lat};
		delete $geo_info->{target_lon};
		if ($text =~ m,<lat>([^<]+)</lat>,) {
			$geo_info->{target_lat} = $1;
		}
		if ($text =~ m,<lng>([^<]+)</lng>,) {
			$geo_info->{target_lon} = $1;
		}
		if ($text =~ m,<name>([^<]+)</name>,) {
			fill_city($geo_info, $1, $zipdistance);
		}
	}

	return $geo_info;
}

sub get_geoinfo_none($$$)
{
	my ($lat, $lon, $geturl) = @_;
	my $geo_info = {};

	return $geo_info;
}

sub get_url_LWP($)
{
	LWP::Simple::get(shift);
}

sub get_url_selfmade($)
{
	my ($url) = @_;

	# Separate host and path.
	unless ($url =~ m{http://([^/]+)(/.*)}) {
		warn "Can't parse URL '$url'.\n";
		return;
	}
	my $url_host = $1;
	my $url_path = $2;

	# Open  a socket.
	my $fd = IO::Socket::INET->new(
		PeerAddr => $url_host,
		PeerPort => 'http(80)',
		Proto    => 'tcp'
	);
	unless (defined $fd) {
		warn "Problem connecting to '$url_host': $@\n";
		return;
	}

	# Send the get request.
	$fd->print("GET $url_path HTTP/1.0\r\nHost: $url_host\r\nConnection: Keep-Alive\r\n\r\n");

	# Collect the answer.
	my $text = '';
	while (<$fd>) {
		$text .= $_;
	}

	# Close the socket.
	$fd->close();

	return $text;
}

sub get_url_fakefile($)
{
	my ($url) = @_;

	# Open a file.
	my $fd = IO::File->new($fakefile, 'r');
	unless (defined $fd) {
		warn "Can't open answer file '$fakefile' for reading. $!\n";
		return;
	}

	# Collect the answer.
	my $text = '';
	while (<$fd>) {
		$text .= $_;
	}

	# Close the fd.
	$fd->close();

	return $text;
}


sub thumbnail_none()
{
	return undef;
}


{
	my $check_done = 0;	# Not checkes yet.
	my $check_ok = undef;	# Pessimistic approach.

sub thumbnail_convert()
{
	my $convert = 'convert'; # Maybe some path expansion or option is needed.
	if (scalar @_ == 0) {
		unless ($check_done) {
			my $command = sprintf "convert --version";
			if (system($command) == 0) {
				$check_ok = 1;
			}
			$check_done = 1;
		}
		return $check_ok;
	}
	my ($input, $output) = @_;
	my $command = sprintf "convert \"%s\" -geometry \"%ix%i>\" \"%s\"",
		$input, $opt_kml_placemark_thumbnail_size,
		$opt_kml_placemark_thumbnail_size, $output;
	my $res = system($command);
	if ($res != 0) {
		die "Calling '$command failed', $res\n";
	}
	return 0;
}
}


# Do nothing.
sub image_file_time_modify($$$)
{
	return 0;
}


# Take the EXIF time and set the file time.
sub image_file_time_exif($$$)
{
	my ($file, $meta_in, $meta_out) = @_;
	my $DateTimeOriginal = $meta_in->exifTool->GetValue('DateTimeOriginal');
	# printf STDERR "got date: %s\n", $DateTimeOriginal;
	$meta_out->SetNewValue('FileModifyDate', $DateTimeOriginal, '', Protected =>  1);
}


# Take the file time and set the file time.
sub image_file_time_keep($$$)
{
	my ($file, $meta_in, $meta_out) = @_;
	my $old = (stat($file))[9];
	my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) =
		localtime($old);
	my $oldstring = sprintf("%4d:%02d:%02d %02d:%02d:%02d",
	$year+1900,$mon+1,$mday,$hour,$min,$sec);
	# printf STDERR "got date: %s\n", $oldstring;

	$meta_out->SetNewValue('FileModifyDate', $oldstring);
}

__END__

=pod

=head1 NAME

gpsPhoto.pl - sync GPS tracklogs with time stamps of image EXIF data

=head1 SYNOPSIS

gpsPhoto.pl [options]

 Options:
  --dir directory    Image directory. Multiple are allowed.
  -I|--image-list file     Image list file. Multiple are allowed.
  -i|--image file    Image file name. Multiple are allowed.
  --gpsdir dir       GPX track directory. Multiple options are allowed.
  --gpsfile-list list      GPX track list file. Mult. options are allowed.
  --gpsfile gpx      GPX track file. Multiple options are allowed.
  --maxtimediff seconds    maximum difference time. Default: 120.
  --maxdistance metres     maximum interpolation distance. Default: 20.
  --timeoffset seconds     Camera time + seconds = GMT. No default.
  --writecaption     image name -> IPTC Caption-Abstract & ObjectName.
  --copydate         Date of EXIF DateTimeOriginal -> IPTC DateCreated.
  --select state     Select images. Default: any ('list' for list).
  --credit "text"    "text" -> IPTC Credit.
  --city "text"      "text" -> IPTC City.
  --sublocation "text"     "text" -> IPTC Sub-location.
  --state "text"     "text" -> IPTC Province-State.
  --country "text"   "text" -> IPTC Country-PrimaryLocationName.
  --copyright "text" "text" -> IPTC CopyrightNotice.
  --source "text"    "text" -> IPTC Source.
  --keywords "text"  "text" -> IPTC Keywords.
  --caption "text"   "text" -> IPTC Caption-Abstract.
  --enable-xmp       Write meta information into an extra XMP file.
  --kml kmlfile      KML output file for Google Earth.
  --kmz kmzfile      KMZ output file for Google Earth.
  --kml-image-type=type    How put an image in KML? ('list' for list).
  --kml-image-dir=dir      KML will reference images in dir.
  --kml-track-enable=method Which tracks come into KML? ('list for list).
  --track-color AABBGGRR   KML track colour: alpha, blue, green, red.
  --track-colour AABBGGRR  KML track colour: alpha, blue, green, red.
  --track-height     Draw track with height. Default off.
  --kml-timeline     Include a track timeline. Default off.
  --kml-placemark-thumbnail-size=size   Max thumbnail size (default 200).
  --kml-placemark-thumbnail-method=method  Thumbnail method (default: none).
  --kml-placemark-thumbnail-dir=dir     Thumbnail dir (default: 'thumbs').
  --dry-run|-n       Do not change the image files.
  --image-file-time=method How to set image time ('list' for list).
  --overwrite-geotagged    Overwrite geotagged images.
  --interpolate=method     Interpolate track points. ('list' for list).
  --tz-guess=method  Guess time zone of track. ('list' for list).
  --report-distance=method Report distance from place ('list' for list).
  --report-direction=method Report direction to place ('list' for list).
  --geoinfo=method   Reverse geo-coding method. ('list' for list).
  --geotag-source=source   Use geotag from source. ('list' for list).
  --geotag=lat,lon,alt     Manual geotag definition.
  --language=type    Definition of the language code (2-letter ISO-3166-1).
  --delete-geotag    Removes all geotags of the given images.
  -V|--version       Print version.
  -h|-?|--help       Print brief help message.
  --man              Print full documentation.

Either --dir, --image-list, or --image is mandatory.

=head1 OPTIONS

=over 8

=item B<--dir directory>

A relative path name from the gpsPhoto perl script or exe file to the image
directory, this parameter is mandatory.

Multiple B<--dir> options are allowed and all found images will be processed.

=item B<--image-list file>

This option defines a text file name. Every line in the text file is an
image file name. You can generate such a file with find(1). Empty lines, lines
with white spaces in them only and lines, which begin with an '#' are ignored.

Multiple B<--image-list> options are allowed and all found images will be
processed.

=item B<--image file>

This option defines a single image file name to process.

Multiple B<--image> options are allowed and all given images will be processed.

=item B<--gpsdir dir>

Define a directory, where GPS tracks are stored. 

Multiple B<--gpsdir> options are allowed and all found GPX files will be
processed.

=item B<--gpsfile-list list>

This option defines a text file name. Every line in the text file is a
GPX file name. You can generate such a file with find(1). Empty lines, lines
with white spaces in them only and lines, which begin with an '#' are ignored.

Multiple B<--gpsfile-list> options are allowed and all found GPX files will be
processed.

=item B<--gpsfile gpx>

A relative path and file name to your GPX file, this parameter is optional if
you just want to use the IPTC metadata part of this script, if you want to work
with GPS coordinates you have to add this parameter.

Multiple B<--gpsfile> options are allowed and all track data will be combined.

=item B<--maxtimediff seconds>

The maximal allowed time difference in seconds between the image EXIF
"DateTimeOriginal" timestamp and the timestamps in the gpx file. Images that
have larger time differences than the given maximal value don't get a
coordinate; if you omit this parameter, a default of 120 seconds will be used.
Note: if more than one GPS track points fall into this time frame for a given
photo, the trackpoint with the smallest time difference will be selected.

=item B<--maxdistance metres>

This options defines the maximal allowed distance in metres between two track
points to still perform an interpolation between them. Default: 20. This option
is for track recorders, where no new trace point will be recorded, if no
movement happens (sitting on a bench taking photos). In this case the next
track point will be recorded only after I go (at least a bit) away.

The options B<--maxtimediff> and B<--maxdistance metres> are combined with
the logical "OR". To allow interpolation, two track points must be near
together in space OR in time. In both cases we perform the interpolation.

=item B<--timeoffset seconds>

A mandatory parameter to describe a timeoffset given in seconds between the
camera and the GPS device. This can be used f.e. if the GPS device records a
time in UTC time and the camera records a local time. Another purpose might be
a wrong time in the camera where the user later still knows the time-offset. A
value of 3600 means one hour time-difference where the camera is one hour
behind in time. A positive value means that the camera is behind in time, a
negative value means that the camera is ahead in time. It is recommended to
take a photo of the GPS showing the current time at the beginning of travelling
or hiking. This way one can see the current GPS time and read the camera time
in the EXIF metadata. This will tell you the timeoffset. There is no default
value!

The timeoffset can also be an expression, which contains the word 'guess'.
This word will be replaced by the time offset calculated because of the also
given B<--tz-guess> option. The resulting string will be evaluated by Perl.
Thus it is easy to cope with a camera clock, which is 10 seconds too fast and
a time zone both with the options: B<--timeoffset=guess-10 --tz-guess=15deg>.

=item B<--writecaption>

This parameter tells the script to copy the filename into the IPTC
"Caption-Abstract" and "ObjectName" - this is useful if you put names into your
filename that should be re-used as captions. This parameter is optional.
Leading digits and underbars, such as "03_..." will be stripped off and
underbars replaced by a space. The ObjectName has a maximum of 64 characters.

The effect of this option is overwritten by B<--caption>.

=item B<--copydate>

This parameter tells the script to copy the EXIF creation date to the IPTC
"DateCreated" tag. This parameter is optional.

=item B<--select state>

Select a set of images to perform IPTC options on. The state is valid until
the next B<--select> option on the command line.
This makes it possible to give different sets of images different values:
--select nogeotag --country Germany --select geotag --country auto

All possible values for B<state> can be found with the special 'list' state.
The default (when no option is given) corresponds to B<--select=any>.

=over 8

=item B<--select=geotag>

The IPTC options following on the command line act on all images, where a
geotag was found.

=item B<--select=nogeotag>

The IPTC options following on the command line act on all images, where no
geotag was found.

=item B<--select=any>

The IPTC options following on the command line act on all images.

=back

=item B<--credit "your credit text">

This parameter tells the script to copy your credit text to the IPTC "Credit"
tag. This parameter is optional.

This parameter honours the option B<--select>.

=item B<--city "your city name">

This parameter tells the script to copy your city text to the IPTC "City" tag.
This parameter is optional. This tag is limited to a maximum of 32 characters.

The special values 'guess', 'auto', and 'manual' ask by using the method
defined by B<--geoinfo> for the city.
This does not work at too remote places.
In the case of 'manual', the automatically determined value will be printed
and can be changed: Press Enter to accept the value or type in the correct
one.

This parameter honours the option B<--select>.

=item B<--sublocation "your sub-location name">

This parameter tells the script to copy your sub-location text to the IPTC
"Sub-location" tag. This parameter is optional. This tag is limited to a
maximum of 32 characters.

The special values 'guess', 'auto', and 'manual' ask by using the method
defined by B<--geoinfo> for the sublocation. Only B<--geoinfo=osm> will
in fact return an entry.
This does not work at too remote places.
In the case of 'manual', the automatically determined value will be printed
and can be changed: Press Enter to accept the value or type in the correct
one.

This parameter honours the option B<--select>.

=item B<--state "your state name">

This parameter tells the script to copy your state text to the IPTC
"Province-State" tag. This parameter is optional. This tag is limited to a
maximum of 32 characters.

The special values 'guess', 'auto', and 'manual' ask by using the method
defined by B<--geoinfo> for the state.
This does not work in all countries.
In the case of 'manual', the automatically determined value will be printed
and can be changed: Press Enter to accept the value or type in the correct
one.

This parameter honours the option B<--select>.

=item B<--country "your country name">

This parameter tells the script to copy your country text to the IPTC
"Country-PrimaryLocationName" tag. This parameter is optional. This tag is
limited to a maximum of 64 characters.

The special values 'guess', 'auto', and 'manual' ask by using the method
defined by B<--geoinfo> for the country.
This does not work at too remote places.
In the case of 'manual', the automatically determined value will be printed
and can be changed: Press Enter to accept the value or type in the correct
one.

This parameter honours the option B<--select>.

=item B<--copyright "your copyright info">

This parameter tells the script to copy your copyright text to the IPTC
"CopyrightNotice" tag. This parameter is optional. This tag is limited to a
maximum of 128 characters.

This parameter honours the option B<--select>.

=item B<--source http://www.carto.net/neumann/>

This parameter tells the script to copy your source text to the IPTC "Source"
tag. This parameter is optional. Unfortunately this tag is limited to only 32
characters!

This parameter honours the option B<--select>.

=item B<--keywords "waterfall,mountains,lakes,hotel,cablecar">

This parameter tells the script to copy your keyword text to the IPTC
"Keywords" tag. Multiple values should be comma separated and can include
spaces. This parameter is optional. Unfortunately this tag is limited
to only 64 characters!

This parameter honours the option B<--select>.

=item B<--caption "picnic under a tree">

This parameter tells the script to copy your caption text to the IPTC
"Caption-Abstract" tag. This parameter is optional and overwrites
B<--writecaption>. This tag is limited to 2000 characters!

The special value 'guess' asks by using the method defined by B<--geoinfo> for
a longer explanation of the place. It is currently implemented for
B<--geoinfo=wikipedia> only.

This parameter honours the option B<--select>.

=item B<--enable-xmp>

Write meta information into an extra XMP file. If an XMP file already exists,
also get information from there. If there is no XMP file, get the information
from the image and create a new XMP file. Only geotags are written into
XMP. With the option B<--copydate>, also the image creation date and time will
be copied into the XMP file. All the other things like IPTC tags and image
dimension (important for the KML image overlays) are currently not written
into XMP.

=item B<--kml kmlfile>

Define the optional KML file to write. It shows in Google Earth the track and
embedds all fitting images at the right place.

=item B<--kmz kmzfile>

Define the optional KMZ file to write. It shows in Google Earth the track and
embedds all fitting images at the right place. The images are embedded in full
size into the KMZ file.

=item B<--kml-image-type=type>

Define, which representation for an image is embedded into a KML file.
The option can be used multiple times.
All possible values for B<type> can be found with the special 'list' type.
The default (when no option is given) corresponds to
B<--kml-image-type=photooverlay>.

=over 8

=item B<--kml-image-type=placemark>

A placemark marks the position of the image. A thumbnail of this image is
embedded into the description of the placemark. A link from the description
references to the original file. This works for KML files only, as the
external link will be viewed by an external Web Browser, which works only
with absolute file names.

=item B<--kml-image-type=screenoverlay>

The image and a black background fill the complete 3d viewer area. This
representation is switched off by default and must be manually switched
on for every image to be viewed. This option is useful for KMZ files
because of the Google Earth deficiencies with external file links.

=item B<--kml-image-type=groundoverlay>

The image floats in the air above the position, where it was taken. This
representation is switched off by default and must be manually switched
on for every image to be viewed. This option is useful for KMZ files
because of the Google Earth deficiencies with external file links.
The size and the viewpoint for this image are such, that the Google Earth
zooming and panning can be used to examine the picture in detail.

=item B<--kml-image-type=photooverlay>

A placemark marks the position of the image. A thumbnail of this image is
embedded into the description of the placemark. A link from the description
references the original file in the GE photo viewer. This works with KML
and KMZ files.

=back

=item B<--kml-image-dir=dir>

The KML file will reference all image files as if they were stored in
the directory dir. This option is useful, if some new images should be tagged
now but they will be moved later into a global directory for all images.

=item B<--kml-track-enable=method>

By default, all tracks end up in the KML file. But this can be restricted.
All possible values for B<method> can be found with the special 'list' type.
The default (when no option is given) corresponds to
B<--kml-track-enable=all>.

=over 8

=item B<--kml-track-enable=all>

Select all tracks for appearance in the KML file. This is the default.

=item B<--kml-track-enable=1>

This is the same as B<--kml-track-enable=all> but deprecated.

=item B<--kml-track-enable=usedsegment>

Select all track segments with at least one point used for the 
track - image - correlations.

=item B<--kml-track-enable=none>

Do not put any track into the KML file.

=item B<--kml-track-enable=0>

This is the same as B<--kml-track-enable=none> but deprecated.

=back

=item B<--track-color color[,color...]>

=item B<--track-colour colour[,colour...]>

Define the track colours in the KML file. The option can be used multiple
times, every option can have multiple comma separated colours. All colours
end up in an array and every new track in the KML file selects the next
colour from this array. After the last colour is used, the array is used again
from the beginning.

The colour itself can be a 8 character hex string with 2 hex digits for the
alpha-channel (00=transparent ... ff=opaque), blue, green, and red (AABBGGRR).
Colour can also be the keyword 'static6', which means 6 bright and very different
colours. The keyword 'static12' fills the array with 12 predefined bright
colours.

The default is a one-element array. Its element has the value 7fffffff (half
transparent white).

=item B<--track-height>

Draw the track with the recorded height in the KML file. This is off by
default, which means to draw the track at the ground.

=item B<--kml-timeline>

Include a track timeline folder into the KML file. This is off by default.
The timeline feature works only in Google Earth 4 and higher. It adds
placemarks with time stamps to the full track and allows to follow the track
visually. This feature increases the KML file size significantly.

=item B<--kml-placemark-thumbnail-size=size>

Set the longer side of the thumbnail image in a KML placemark to the
given size. The default is 200.

=item B<--kml-placemark-thumbnail-method=method>

Define the method to create thumbnail images. This option is used in KML and
KMZ file creation. A thumbnail is needed for the options
B<--kml-image-type=placemark> and B<--kml-image-type=photooverlay>.
All possible values for B<method> can be found with the special 'list' method.
Default is none. When a method does not work (external dependencies are not
fulfilled), the system falls back to none automatically.

A thumbnail inherits the file name of the original image but it resides in
a different directory (see B<--kml-placemark-thumbnail-dir>).

=over 8

=item B<--kml-placemark-thumbnail-method=none>

Do not create thumbnail files. When a thumbnail file is neede in KML, the
original file is used and Google Earth has to resize the original file itself.
This is the default.

=item B<--kml-placemark-thumbnail-method=convert>

Create thumbnail files with the command C<convert>, which is part of the
ImageMagick suite from L<http://www.imagemagick.com>.

=back

=item B<--kml-placemark-thumbnail-dir=dir>

This options defines, where the thumbnails are written to on disk. If the
B<dir> is a relative path, it is interpreted as relative to the directory,
where the image is located. The default is "thumbs", and as such a relative
path.

=item B<--dry-run|-n>

No not change the image files. Default is off.

=item B<--image-file-time=method>

When the program changes the image files, the OS will change the file time
as well. This can suppressed. All possible values for B<method> can be found
with the special 'list' method.  Default is 'modify'.

=over 8

=item B<--image-file-time=modify>

Let ExifTool and the OS do what they want with the image file date and time.

=item B<--image-file-time=exif>

Set the file date and time based on the EXIF tag DateTimeOriginal.

=item B<--image-file-time=keep>

Get the image file date and time before the change and restore it afterwards.

=back

=item B<--overwrite-geotagged>

Overwrite geotagged images. Usually, if all 6 GPS related tags
(GPSLatitude, GPSLatitudeRef, GPSLongitude, GPSLongitudeRef,
GPSAltitude, and GPSAltitudeRef) are already set in an image, it will be
skipped. With this option, it will be overwritten anyway.

=item B<--interpolate=method>

Interpolate image coordinates between track points according to the three
time stamps (trackpoint before, image, trackpoint afterwards). All possible
values for B<method> can be found with the special 'list' method. Default is
none.

=over 8

=item B<--interpolate=none>

Do not interpolate but take the coordinates from the waypoint, which is
nearest.

=item B<--interpolate=linear>

Interpolate longitude and latitude separate and linear.

=item B<--interpolate=great-circle>

Interpolate also linear but along the great circle. This should be better
for widely spaced track points.

=back

=item B<--tz-guess=method>

Guess the time zone of the track. The track is represented by the middle track
point. All possible values for
B<method> can be found with the special 'list' method. The result is the 
time zone name and the needed B<--timeoffset> option, to take this time zone
into regard.

If the option B<--timeoffset> contains the word 'guess', it will be replaced
by the calculated offset.

=over 8

=item B<--tz-guess=15deg>

Calculate the time zone as difference to GMT by dividing the longitude by
15 and rounding accordingly.

=item B<--tz-guess=zone.tab>

Calculate the time zone by finding the nearest point in the zone.tab file
located at /usr/share/zoneinfo/zone.tab.

=back

=item B<--report-distance=method>

This defines the method to report not only the guessed place (city) name but
also the distance to it. All possible values for B<method> can be found with
the special 'list' method. The default is 'none'.

=over 8

=item B<--report-distance=none>

Do not report a distance from the found place. Just the place name itself.
This is the default.

=item B<--report-distance=km>

Report the distance to the found place in kilometres.

=item B<--report-distance=miles>

Report the distance to the found place in statute miles (1 statute mile = 1.609344 km).

=item B<--report-distance=nautical>

Report the distance to the found place in nautical miles (1 nautical mile = 1.852 km).

=back

=item B<--report-direction=method>

This defines the method to report not only the guessed place (city) name and
distance name but also the direction to it. All possible values for B<method>
can be found with the special 'list' method. The default is 'none'.

B<--report-distance> and B<--report-direction> can be mixed in any
combination.

=over 8

=item B<--report-direction=none>

Do not report a direction to the found place. Just the place name itself.
This is the default.

=item B<--report-direction=degree>

Report the direction to the found place as degree: 0 is north, 90 is east,
180 is south, and 270 is west.

=item B<--report-direction=4>

Report the direction to the found place as one of four possible values: N, E,
S, W.

=item B<--report-direction=8>

Report the direction to the found place as one of eight possible values: N, NE,
E, SE, S, SW, W, NW.

=back


=item B<--geoinfo=method>

This defines the method to guess geo information (city, state, country)
from the geo coordinates. This is called reverse geo coding and requires a
big (online) database of places. All possible values for B<method> can be
found with the special 'list' method. The default is 'geonames'.

=over 8

=item B<--geoinfo=geourl>

Perform the reverse geo coding by asking L<http://geourl.org>.
This web site knows the state sub division of a country only for the 
USA and even there it only returns the 2 letter code.

=item B<--geoinfo=geonames>

Perform the reverse geo coding by asking L<http://www.geonames.org>.
This is the default, because I found it more precisely than L<http://geourl.org>
at the places of interest for me. Your experience might vary. I also had the
impression, that this web site is a bit faster.

=item B<--geoinfo=wikipedia>

Perform the reverse geo coding by asking first the place database
of L<http://www.geonames.org> and then the place database from
Wikipedia (also via L<http://www.geonames.org>). If the entry from
Wikipedia is nearer than the entry from L<http://www.geonames.org>,
the city tag will be filled with the Wikipedia entry title instead.
This works best in remote areas without any nearby cities.
L<http://www.geonames.org> alone may report a distant city but
Wikipedia might know about a closer special place (for example, a
landmark, monument or location).

=item B<--geoinfo=osm>

Works like B<--geoinfo=geonames> but additionally tries to get the street
name by asking the OpenStreetMap Name Finder
L<http://www.frankieandshadow.com/osm/>. In fact the current implementation
searches for any OpenStreetMap object with a name attached near the given
location and only most likely it is a street. This additional information
is stored as IPTC sublocation.

=item B<--geoinfo=zip>

Perform the reverse geo coding by asking L<http://www.geonames.org>
for the nearest postal code. The result in bigger cities is often the city
name itself and not the name of a city district.

=item B<--geoinfo=none>

Don't perform any reverse geo coding. This should only be used, if the
internet connection is slow or not available. Then the program does not try
to connect to some remote site, which would not work anyway.

=back

=item B<--geotag-source=source>

Define the used geotag source. The option can be used multiple times.
All possible values for B<source> can be found with the special 'list' source.
The default (when no option is given) corresponds to
B<--geotag-source=exif --geotag-source=track>.

=over 8

=item B<--geotag-source=exif>

Take the geo coordinates from the image itself. Usually they were embedded by
a prior run of this program.

=item B<--geotag-source=track>

Take the geo coordinates from the track. This needs the EXIF tag
DateTimeOriginal in the image to find out, when the picture was taken.

=item B<--geotag-source=option>

Take the geo coordinates from the command line option B<--geotag>. The time
is taken from the EXIF tag DateTimeOriginal in the image.

=back

=item B<--geotag=latitude,longitude,altitude>

This option allows manual geotagging from the command line in combination with
the option B<--geotag-source=option>. The latitude is a floating point
number in degree of arc (90.0 ... -90.0). The longitude is a floating point
number in degree of arc (-180.0 .. 180.0). The altitude is an integer in
metres above (positive) or below (negative) sea level.

=item B<--language type>

This option defines the output language. The language is defined as a
two letter code (ISO-3166-1). Only very few options already honour this
option.

Currently only the place name guessing for the country, state, and city from
B<--geoinfo=wikipedia> and B<--geoinfo=geonames> will return language specific
place names. All the rest of the program (including this documentation)
remains English but this may change in the future.

=item B<--delete-geotag>

This option only removes the geotags from the given images (via B<--dir>,
B<--image-list>, or B<--image>). With this option the program does not perform
any image to track correlation actions.

=item B<--version>

Prints the program version and exits.

=item B<--help>

Prints a brief help message and exits.

=item B<--man>

Prints the manual page and exits.

=back

=head1 SEE ALSO

Homepage at L<http://www.carto.net/projects/photoTools/gpsPhoto/>.

Project Page at L<http://sourceforge.net/projects/gps2photo>.

=head1 AUTHOR

 Andreas Neumann (neumann@karto.baug.ethz.ch)
 Peter Sykora (peter_sykora@gmx.at)
 Patrick Valsecchi (patrick@thus.ch)
 Christian Brauchli (admin@bbz-sh.ch)
 Uwe Girlich (Uwe.Girlich@philosys.de)

=cut

