#!/usr/bin/perl
#
# In the bookmarks.html exported from firefox, there is
# icon data from website.
#

use strict;
use MIME::Base64;

sub write_icon($$)
{
	my ($type, $data) = @_;
	my $num = int(rand(8999)+1000);
	my $ext;

	if ( $type =~ m/icon/i )  {
		$ext = '.ico';
	} elsif ( $type =~ m/png/i )  {
		$ext = '.png';
	} elsif ( $type =~ m/gif/i )  {
		$ext = '.gif';
	} elsif ( $type =~ m/jpeg/i )  {
		$ext = '.jpg';
	}

	my $fname = $num . $ext;
	print "file: $fname\n";

	my $bin = decode_base64($data);
	open my $ofh, "> $fname" or die;
	binmode $ofh;
	print $ofh $bin;
	close $ofh;
}


my $ifile = $ARGV[0] || 'bookmarks.html';

# ICON="data:image/png;base64,iVBORw0...
my $myre = qr(ICON=\"data:(.+);(.+),([a-zA-Z0-9/+=]+)\");

print STDERR "read from: $ifile\n";
open my $ifh, $ifile or die "cannot find $ifile: $!";

while (<$ifh>) {
	if ( m/$myre/ )  {
		# $type: MIME type, $encoding: base64, $data: the b64 encoded data
		my ($type, $encoding, $data) = ($1, $2, $3);
		write_icon($1, $3);
	}
}

close $ifh;

=pod

=head1 NOTE

Put bookmarks.html from firefox at the same directory with this script.

> wicon.pl

Icons stored within bookmarks would be extracted.

=cut

