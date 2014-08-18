#!/usr/bin/perl
use strict;
use Spreadsheet::Read;
use Data::Dump qw(dump);

my $report_file = q(q:\\Report\\WeeklyReport\\MMI_WeeklyReport_2008_Rasmus.xls);
my $excel = ReadData($report_file);

dump($excel);
