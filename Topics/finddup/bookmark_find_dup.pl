#!/usr/bin/perl
#
# Find out the duplicated URL
# in the ''bookmarks.html'
#

use strict;
use HTML::Parser ();
use Data::Dump ();

my $cnt = 0;
my $file = $ARGV[0] || "bookmarks.html";
my @url = ();

sub start(@);

sub main()
{
	# Create parser object
	my $p = HTML::Parser->new( api_version => 3,
	                     start_h => [\&start, "text, tagname, attr"],
	                     marked_sections => 1,
	                   );

	# open file as UTF8
	open (my $fh, "<:utf8", $file) || die;
	$p->parse_file($fh);

	# to find the duplicated urls
	print '-' x 20, "duplicated list", '-' x 20, "\n";
	my %dup = ();
	foreach (@url)  {
		$dup{$_} ++;

		#++ $dup{com} if m/\.com/;
		#++ $dup{net} if m/\.edu/;
		#++ $dup{org} if m/\.org/;
		#++ $dup{tw} if m/\.tw/;
	}
	print '-' x 55,"\n";
	for (keys %dup)  {
		print $_,": ",$dup{$_}, "\n" if $dup{$_} >= 2;
	}

	print STDERR "total URL count = $cnt\n";
}

sub start(@)
{
	my $max_length = 60;
	my ($text, $tagname, $attr) = @_;

	if ($tagname =~ m/a/i)  {
		#substr($text, $max_length) = "..." if length($text) > $max_length;
		#print(Data::Dump::dump($attr), "\n") if $attr;
		if ($attr && ref($attr) eq "HASH")  {
			#print Data::Dump::dump($attr), "\n";
			if (%$attr->{href})  {
				push @url, %$attr->{href};
			}
			++ $cnt;
		}
	}
}

main;
