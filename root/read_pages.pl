#!/usr/bin/perl

# I am using a apk "chrome to phone".
# It could share links between android to pc.
# It links my dropbox account and create ''My Dropbox/PhonetoChrom/pages''
# The content is in the format of JSON, with a javascript function embedded.
# This script will strips the function enclosure and show the url.

use strict;
use warnings;
use v5.10;

use Config::JSON;
use Data::Dump qw(dump);
#use if $^O eq "MSWin32", "Encode qw(from_to)";
use Encode qw(from_to);
use Time::Local;

my $file = "pages";
my $tmp = "d:/tmp.json";

sub strip_func()
{
	my $cont;

	open my $fh, $file or die;
	while (<$fh>)  {
		s/[\r\n]//;
		$cont = $cont . $_;
	}
	close $fh;
	#print $cont;

	my $tmp_cont;
	if ($cont =~ m/showPages\((.*)\)/ )  {
		$tmp_cont = $1;
	}
	open my $ofh, "> $tmp" or die;
	print $ofh $tmp_cont;
	close $ofh;
}


sub load_setting()
{
	my $cfg = Config::JSON->new($tmp);

	my $rp = $cfg->get("pages");
	my @arr = @$rp;

#	dump(@arr);

	say '-' x 40;
	foreach my $rh (@arr)  {
		my $title = $rh->{"title"};
		if ($^O eq "MSWin32" && $title)  {
			from_to($title, "UTF8", "BIG5");
			say $title if $title;
		}
		my $myurl = $rh->{"url"};
		say $myurl if $myurl;

		my $date = $rh->{'date'};
		# perl/unix date+%s only 10 digits, but json date has 13 digits
		show_date($date/1000) if $date;

		say '-' x 40;
	}

}

sub show_date($)
{
	my $epoch = shift;
	#say $epoch;
	my ($ss,$mm,$hh,$mdd,$mmm,$year,$wday,$yday,$isdst) = localtime($epoch);

	return unless $year;

	printf("%04d-%d-%02d\t",($year+1900),($mmm+1),$mdd);
	printf("%02d:%02d:%02d\n", $hh, $mm, $ss);
}

sub main()
{
	strip_func();
	load_setting();
}

main;
