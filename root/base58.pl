#!/usr/bin/env perl

# refer to b64.pl, numbase.pl as well

# NOTE: Encode::Base58 is required
# shorten URL service "flic.kr/p/" does not work?
#
# python module: base58
# cat file | base58
#

use strict;
use warnings;
use v5.10;
use Encode::Base58;

# use if win32
use if $^O eq 'MSWin32', 'Win32::Clipboard';

my $prefix = q(flic.kr/p/);

# http://www.flickr.com/photos/ericosur/5339543818/
my $num = $ARGV[0] || '5339543818';
my $short_url = $prefix . encode_base58($num);
say  $short_url;

if ($^O eq 'MSWin32')  {
	# put the shorten url into clipboard
	print STDERR "copy url to clipboard...";
	Win32::Clipboard::Set($short_url);
}
