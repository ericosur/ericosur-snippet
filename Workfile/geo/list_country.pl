#!/usr/bin/perl

use strict;
use 5.010;

use Spreadsheet::ParseExcel;
use Spreadsheet::WriteExcel;
use Data::Dump qw(dump);


sub list_country($)
{
	my $f = shift;
	my $e = new Spreadsheet::ParseExcel;
	my $book = $e->Parse($f);
	my $sheet_cnt = $book->{SheetCount};
	my @country_arr = ();
	
	my $sheet = $book->{Worksheet}[0];
#	say "worksheet name: ", $sheet->{Name};
#	say "min row: ", $sheet->{MinRow};
#	say "max row: ", $sheet->{MaxRow};
#	say "min col: ", $sheet->{MinCol};
#	say "max col: ", $sheet->{MaxCol};

	# list col #1
	my $row = 0;
	my $col = 1;
	my $max_row = $sheet->{MaxRow};
	for (my $i=0; $i < $max_row; ++$i) {
		next unless (defined $sheet->{Cells}[$i][$col]);
		my $val = $sheet->{Cells}[$i][$col]->Value;
		push @country_arr, $val;
	}
	
	say "read from shipping: ", scalar(@country_arr);
	return @country_arr;
}

sub read_geo($)
{
	my $f = shift;
	my $e = new Spreadsheet::ParseExcel;
	my $b = $e->Parse($f);
	my $s = $b->{Worksheet}[0];
	my %h = ();

	say "worksheet name: ", $s->{Name};
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
	say "read from geo cnt = ", $cnt;
	return %h;
}

sub main()
{
	my $file = 'shipping_country.xls';
	my $geo = 'geo.xls';

	my @arr = list_country($file);
	my %geo = read_geo($geo);

	my $notfound_cnt = 0;
	my $found_cnt = 0;
	foreach my $n (@arr) {
		if (not defined $geo{$n}) {
			say $n;
			$notfound_cnt ++;
		} else {
			$found_cnt ++;
		}
	}
	say $notfound_cnt, " countries not found at geo table";
	say $found_cnt, " country names matches";
}

main;

