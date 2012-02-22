#!/usr/bin/perl

# translate geo.xls into ini format

use strict;
use 5.010;
use Spreadsheet::Read;
# Data::Dump for debugging
use Data::Dump qw(dump);

# Data file: you need Geo.xls and iso-3166-2.txt

my @app_names = ();
my $report_file = 'Geo.xls';
my $xls = ReadData($report_file);

sub read_app_names()
{
# range for B1 to V1
	my @row = Spreadsheet::Read::row($xls->[1], 1);
	#dump(@row);
	foreach my $aa (@row)  {
		$aa =~ s/[ &\[\]]//g;
		if ($aa eq "")  {
			next;
		}
		push @app_names,$aa;
	}
	#dump(@app_names);
	#say '-' x 40;
}

sub read_iso3166()
{
	my $ff = 'iso-3166-2.txt';
	my %ccode = ();

	open my $fh, $ff or die;
	while (<$fh>) {
		next if /^$/;
		next if /^#/;
		if (m/^(..)\t(\w+)\s+/)  {
			my $two = $1;
			my $full = $2;
			#print("($full) => ($two)\n");
			$ccode{$full} = $two;			
		}
	}
	close $fh;
	return \%ccode;
}

sub read_country_row()
{
	my $cnum = 3;	# start from row 3, skip Androidversion
	my @row;
	my $cnt = 0;
	while (1)  {
		@row = Spreadsheet::Read::row($xls->[1], $cnum);
		$cnum++;
		my $cname = $row[0];
		#dump(@row);
		last unless $cname;
		++ $cnt;
		$cname =~ s/[ '()]//g;
		output_country($cname, \@row);
		#last if $cnt > 0;
	}
}

sub output_app_names()
{
	print("[Programs]\n");
	foreach my $ap (@app_names) {
		printf("%s=%s.apk\n", $ap, $ap);
	}
}

sub output_country($@)
{
	my $cname = shift;
	my $ref = shift;
	my ($res, $yn, $cnt);
	my @row = @$ref;

	my $rc = read_iso3166();
	my %ccode = %$rc;

	$cnt = 1;
	#dump(@row);
	#dump(%ccode);
	
	# translate full country name to 2 alpha char
	if ($ccode{$cname} ne "")  {
		printf("[%s]\t; %s\n", $ccode{$cname}, $cname);
	} else  {
		printf("[%s]\n", $cname);
	}

	foreach my $ap (@app_names)  {
		next if ($ap eq "");
		$yn = $row[$cnt++];
		if ($yn eq 'WW')  {
			$yn = 'Y';
		}
		printf("%s=%s\n", $ap, $yn);
	}
}


sub main()
{
	read_app_names();
	output_app_names();
	read_country_row();
}

main;

