#!/usr/bin/perl

use strict;
use v5.10;

use Spreadsheet::ParseExcel;
#use Spreadsheet::WriteExcel;
use Data::Dump qw(dump);

my $debug = 0;

sub list_country($)
{
	my $f = shift;
	my $e = new Spreadsheet::ParseExcel;
	my $book = $e->Parse($f);
	my $sheet_cnt = $book->{SheetCount};
	my @country_arr = ();

	my $sheet = $book->{Worksheet}[0];
	if ($debug) {
    	say "worksheet name: ", $sheet->{Name};
    	say "min row: ", $sheet->{MinRow};
    	say "max row: ", $sheet->{MaxRow};
    	say "min col: ", $sheet->{MinCol};
    	say "max col: ", $sheet->{MaxCol};
    }
	# list col #1
	my $row = 2;
	my $col = 2;
	my $max_row = $sheet->{MaxRow};
	for (my $i=$row; $i < $max_row; ++$i) {
		next unless (defined $sheet->{Cells}[$i][$col]);
		my $val = $sheet->{Cells}[$i][$col]->Value;
		push @country_arr, $val;
	}

	say STDERR "read from shipping: ", scalar(@country_arr);
	return @country_arr;
}

sub read_geo($)
{
	my $f = shift;
	my $e = new Spreadsheet::ParseExcel;
	my $b = $e->Parse($f);
	my $s = $b->{Worksheet}[0];
	my %h = ();

    if ($debug) {
	    say "worksheet name: ", $s->{Name};
	}
	# start from col0, row12
	my $max_row = $s->{MaxRow};
	my $col = 0;
	my $cnt = 0;
	for (my $i=12; $i < $max_row; ++$i) {
		next unless (defined $s->{Cells}[$i][$col]);
		my $val = $s->{Cells}[$i][$col]->Value;
		#say $val;
		++$cnt;
		$h{$val} = 1;
	}
	say STDERR "read from geo cnt = ", $cnt;
	return %h;
}

sub read_iso3166()
{
	my $ff = 'two-alpha.txt';
	my %two_full = ();
    my %full_two = ();

	open my $fh, $ff or die;
	while (<$fh>) {
		next if /^$/;
		next if /^#/;
		if ( m/^(..)\s+(.+)$/ )  {
			my $two = $1;
			my $full = $2;
			if ( defined($two) && defined($full) ) {
			    $two_full{$two} = $full;
			    $full_two{$full} = $two;
			}
			if ($debug) {
			    print("($full) => ($two)\n");
		    }
		}
	}
	close $fh;
	say STDERR "size of two_full: ", scalar(keys(%two_full));
	say STDERR "size of full_two: ", scalar(keys(%full_two));

	return %full_two;
}

sub read_iso31661alpha2()
{
	my $ff = 'iso-3166-1-alpha-2.txt';
	#my %two_full = ();
    my %full_two = ();

	open my $fh, $ff or die;
	while (<$fh>) {
		next if /^$/;
		next if /^#/;
		if ( m/^(.+);(..)$/ )  {
			my $full = $1;
			my $two = $2;
			if ( defined($two) && defined($full) ) {
			    #$two_full{$two} = $full;
			    $full_two{$full} = $two;
			}
			if ($debug) {
			    print("($full) => ($two)\n");
		    }
		}
	}
	close $fh;
	#say STDERR "size of two_full: ", scalar(keys(%two_full));
	say STDERR "size of full_two: ", scalar(keys(%full_two));

	return %full_two;
}

sub main()
{
	my $file = 'bright.xls';
	my $geo = 'geo.xls';

	my @arr = list_country($file);
	my %geo = read_geo($geo);
    my @geo_not_found = ();

   	my %full;# = read_iso3166();
   	my @alpha2_not_found = ();

	my $found_cnt = 0;
	foreach my $n (@arr) {
		if (not defined $geo{$n}) {
			say $n;
			push(@geo_not_found, $n);
		} else {
			$found_cnt ++;
		}
		if ( defined(@alpha2_not_found) ) {
			my $alpha2 = $full{uc($n)};
			if ( defined($alpha2) ) {
		    	say $n, " => ", $alpha2;
			} else {
		    	# try using partial match
		    	my $flag = 0;
		    	foreach my $fn (keys(%full)) {
		        	my $m = uc($n);
		        	if ( $fn =~ m/$m/ ) {
		            	say $n, " => ", $alpha2;
		            	$flag = 1;
		        	}
		    	}
		    	if ($flag == 0) {
		        	push(@alpha2_not_found, $n);
		    	}
			}
		}
	}
	say STDERR scalar(@geo_not_found), " countries not found at geo table";
	foreach (@geo_not_found) {
	    say "geo not found: ", $_;
    }
	if ( defined(@alpha2_not_found) ) {
		say scalar(@alpha2_not_found), " countries iso3166 alpha2 not match";
		foreach (@alpha2_not_found) {
	    	say "alpha2 not found: ", $_;
		}
		say STDERR $found_cnt, " country names matches";
	}
}

main;

