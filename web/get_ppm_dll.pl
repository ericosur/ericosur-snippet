#!/usr/bin/perl

# to fetch dll files from $url sites

use strict;
use warnings;
use WWW::Mechanize;
use Data::Dump qw(dump);

my $mech = WWW::Mechanize->new( autocheck => 1 );
my $url = q(http://trouchelle.com/ppm/dll/);
my $regex = qr/dll/;
my $action = $ARGV[0] || 0;

if ( $action == 0 )  {
	print <<EOL;
Only list the URL, no action would be performed.
Use ''$0 1'' to perform actual downloading.
EOL
}

$mech->get($url);

# for example: http://trouchelle.com/ppm/dll/intl.dll
# text_regex to filter URL
my @links = $mech->find_all_links(
    text_regex => $regex );

my $cnt = 0;
foreach (@links)  {
	last if (++ $cnt > 10);		# for testing, only download 10 files
	print "fecth: ", $_->url_abs(), " ...\n";
	my $file = $_->url();
	next if (-f $file);		# skip if exists
	if ($action)  {
		$mech->get($_->url_abs(), ":content_file" => $file);
	}
	else  {
		#print "no D/L action...\n";
	}
	#print dump($_);
}
print "\n";
