#!/usr/bin/perl
#
# query the fonts could be used by Image::Magick
#
# 2007/11/15 by ericosur

use strict;
use warnings;

use Image::Magick;

#my $im = Image::Magick->new();
#my @fonts = $im->QueryFont();

my @fonts = Image::Magick->QueryFont();

for (@fonts)
{
	print $_, "\n";
}

#undef $im;
