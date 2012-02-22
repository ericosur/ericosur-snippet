#!/usr/bin/perl

# an easy example to fetch a file from URL
# same as wget ...

use strict;
use warnings;
use WWW::Mechanize;

my $mech = WWW::Mechanize->new( autocheck => 1 );

# try to fetch a png file from my own pagecreator@google
# http://ericosur.googlepages.com/abc.png

my $url = q(http://ericosur.googlepages.com/abc.png);
my $file = 'tmp.png';	# default name
if ( $url =~ m!\/([^/]+)$! )  {
	$file = $1;
}
print "fetch from: ", $url, "\n";
print "output to: ", $file, "\n";

$mech->get($url, ":content_file" => $file);

__END__;
