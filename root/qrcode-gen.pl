#!/usr/bin/perl
use strict;
use warnings;

use GD::Barcode::QRcode;
use Digest::MD5  qw(md5 md5_hex md5_base64);

#
# [in] output file name
# [in] the png
#
sub output_png($$)
{
	my ($outfile, $png) = @_;

	open FH, "> $outfile" or die;
	binmode FH;

	print FH $png;
	close FH;

	print "output to $outfile\n";
}

my $img_file = "qr.png";

#my $str = q(mailto:ericosur@gmail.com);
my $str =<<EOL;
NAME1:Rasmus
TEL1:0939064810
MAIL1:ericosur\@gmail.com
EOL

my $gd = GD::Barcode::QRcode->new($str, {Version => 6, ModuleSize => 6});

my $png = $gd->plot->png;

output_png($img_file, $png);


# MD5 value into base64 format
my $digest = md5_hex($png);
print "digest: ", $digest, "\n";

