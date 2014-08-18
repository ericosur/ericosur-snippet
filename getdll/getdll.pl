#!/usr/bin/perl

#
# get dll files from http://trouchelle.com/ppm/dll/
# here is a perl repo for win32
#

use strict;
use warnings;

use WWW::Mechanize;
use Data::Dumper;

my $http = q(http://trouchelle.com/ppm/dll/);
my $file = "index.html";
my $m = 'WWW::Mechanize'->new;

sub get_index()
{
	my $url = $http;
	print "fetch $url\n";
	my $ret = $m->get($url, ':content_file', $file);
	print Dumper($ret);
}

sub parse($)
{
	my $listref = shift;
	my $fh;

	open $fh, $file or die "cannot open file: $!\n";

	while ( <$fh> )  {
		#print;
		#<A HREF="/ppm/">Parent Directory</A>
		#<A HREF="charset.dll">charset.dll</A>
		if ( m/<A HREF=\"([^"]+\.dll)\">/ )  { #"
			push @$listref, $1 if $1;
			print '.';
		}

	}
	print "\n";
	close $fh;
}

sub fetch($)
{
	my $listref = shift;
	my $url;
	my $count = 0;

	foreach (@$listref)  {
		$url = $http . $_;
		if ( -e $_)  {
			$m->get($url, ':content_file', $_);
			print "fetched $_\n";
			++ $count;
		}
		else  {
			print "skipped $_\n";
		}
	}
	print "$count file fetched\n";
}

sub main()
{
	my @list = ();

	if (not -e $file)  {
		print "call get_index()\n";
		get_index();
	}
	else  {
		print "nothing...\n";
	}
}

main;

__END__;

parse(\@list);
#print join("\t", @list), "\n";
fetch(\@list);
