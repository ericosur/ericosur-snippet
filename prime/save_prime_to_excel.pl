#!/usr/bin/perl

use strict;
use warnings;
use v5.10;
#use Spreadsheet::ParseExcel;
use Spreadsheet::WriteExcel;
use Data::Dumper;

=pod

This script demos how to create a new excel file.
It would be possible to create excel file under linux.

The max number of rows in Excel 2003 or older is 65536.
So the row beyond 65536 would be written in another worksheet.
http://cpansearch.perl.org/src/JMCNAMARA/Spreadsheet-WriteExcel-2.37/examples/row_wrap.pl

=cut

# max number of row in excel
my $max_row = 65536;

sub parse_text_and_save_excel($$)
{
	my $inf = shift;
	my $outf = shift;
	say "in: $inf, out: $outf";
	my $workbook = Spreadsheet::WriteExcel->new($outf);
    # Add a worksheet
    my $worksheet = $workbook->add_worksheet();
    my ($row, $col) = (0, 0);
    my $cnt = 0;
    
	open my $fh, $inf or die;
	while (<$fh>)  {
		if (m/^(\d+)\s+(\d+)/)  {
			if (defined($1)) {
				++ $cnt;
				my ($id, $num) = ($1, $2);
				#say $num;
				$worksheet->write($row, $col, $id);
				$worksheet->write($row, $col+1, $num);
				++ $row;
				if ($row == $max_row)  {
					$worksheet = $workbook->add_worksheet();
					$row = 0;
				}
			}
		}
	}
	say "cnt: $cnt";
	close $fh;
	$workbook->close();
}

sub main()
{
	my $file = "prime_100k.txt";
	my $excel_file = $file;
	$excel_file =~ s/txt/xls/;
	parse_text_and_save_excel($file, $excel_file);
}

main;
