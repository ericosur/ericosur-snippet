#!/usr/bin/perl
#
# launch the default browser if -b is sepecified
#

use strict;
use warnings;

die "only under win32" if $^O ne "MSWin32";

use if $^O eq "MSWin32", "ActiveState::Win32::Shell qw(BrowseUrl)";
use if $^O eq "MSWin32", "Win32::Clipboard";
use Getopt::Std;

my %opts = ();

getopts('b', \%opts);

my $url =  <<EOL;
http://flickr-gmap-show.googlecode.com/svn/trunk/flickr-gmap-photoset.html?photoset_id=
EOL

if (!$ARGV[0])  {

	warn "Need specify photoset number...\n";
	warn "You need complete by yourself\n";
}
else  {
	$url =~ s/\n//;
	$url = $url . $ARGV[0];
	print $url, "\n";

	# launch browser with this URL
	if ($opts{b})  {
		BrowseUrl($url);
	}
	Win32::Clipboard::Set($url);
}

=pod

=head1 NAME

gmap-url.pl - compose a gmap URL to view your geotagged flickr set in google map

=head1 SYNPOPIS

gmap-url.pl [flickr set number]

And the result would print out and copy it into clipboard thus you could paste
into your browser.

For example:
http://www.flickr.com/photos/ericosur/sets/B<72157600887696692>/
the "72157600887696692" is the set number.

=cut
