#!/usr/bin/perl
use strict;
use warnings;

#use utf8;

my $cnt = 0;
my $ofh;
my $out_file = "20080412.gpx";

sub main()
{
	my @gpx_list = glob('s*.gpx');
	#print STDERR join("\n", @gpx_list), "\n";

	my @sorted = sort { $a cmp $b } @gpx_list;
	#print STDERR join("\n", @gpx_list), "\n";

	open $ofh, "> $out_file" or die;
	xml_header();
	for (@sorted)  {
		++ $cnt;
		one_file($_);
#		print $cnt, "\n";
	}
	xml_footer();
	close $ofh;
}

sub one_file()
{
	my $ifile = shift;
	my $start_copy = 0;

	print $ifile,"\n";

	open my $ifh, $ifile or die;

	while (<$ifh>)  {
		$start_copy = 1 if m/<trk>/;
		if ( m/^<name>Track (\d+)<\/name>/i )  {
			printf $ofh "<name>Track %03d</name>\n", $cnt;
		}
		else  {
			print $ofh $_ if $start_copy;
		}
		$start_copy = 0 if m/<\/trk>/;
	}

	close $ifh;
}

sub xml_header
{
	print $ofh <<XMLEOL;
<?xml version="1.0" encoding="UTF-8"?>
<gpx
 version = "1.1"
creator = "TimeMachineX - http://www.wintec.com.tw"
xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
xmlns = "http://www.topografix.com/GPX/1/1"
xsi:schemaLocation = "http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.topografix.com/GPX/gpx_overlay/0/3 http://www.topografix.com/GPX/gpx_overlay/0/3/gpx_overlay.xsd http://www.topografix.com/GPX/gpx_modified/0/1 http://www.topografix.com/GPX/gpx_modified/0/1/gpx_modified.xsd">
<!-- merged by $0 by ericosur -->
<metadata>
<bounds maxlat="25.030723" maxlon="121.508378" minlat="23.348706" minlon="120.403589"/>
</metadata>
XMLEOL
	;
}

sub xml_footer
{
	print $ofh <<XMLEOL;
</gpx>
XMLEOL
}

main;
