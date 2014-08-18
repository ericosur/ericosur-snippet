#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

my $filter_cnt = 0;
my $cnt = 0;


my $file = 'testResult.xml';
my $ofile = 'failcase.txt';

my %known = ();


sub parse_xml()
{
	my @arr = ();
	my $tpackage;
	my $tcase;
	my $total_report;

	# print header
	#$total_report = $total_report . sprintf("package,class,method,retest status,retest time\n");

	open my $fh, $file or die;
	while (<$fh>) {
		#<TestPackage name="CtsAccelerationTestCases" appPackageName="android.acceleration"
		if ( m/^\s+<TestPackage name=\"([^\"]+)\" appPackageName=\"([^\"]+)\"/ ) {
			@arr = ();
			#printf("test package: %s\n", $1);
			$tpackage = $2;
		}
		if ( m/^\s+<TestSuite name=\"([^\"]+)\">/ ) {
			push @arr, $1;
			#printf("suite:%s\n", $1);
		}
		if ( m/^\s+<\/TestSuite>/ ) {
			pop @arr;
		}
		# <TestCase name="ValueAnimatorTest" priority="">
		if ( m/^\s+<TestCase name=\"([^\"]+)\"/ ) {
			$tcase = $1;
			#printf("case:%s\n", $1);
		}
		#<Test name="testCancel" result="fail" starttime="Mon Apr 02 15:56:44 CST 2012" endtime="Mon Apr 02 15:56:44 CST 2012">
		if ( m/\s+<Test name=\"([^\"]+)\" result=\"fail\"/ ) {
			my $fail = $1;
			$cnt += 1;
			#printf("fail: %s\n", $1);
			my $cname = join('.', @arr);
			unless ( $known{$fail} ) {
				#$total_report = $total_report . sprintf("%s,%s.%s,%s\n", $tpackage, $cname, $tcase, $fail);
				$total_report = $total_report . sprintf("%s.%s\t%s\n", $cname, $tcase, $fail);
				$filter_cnt += 1;
			}
		}
	}
	#print STDERR "filtered: $filter_cnt\n";
	#print STDERR "total: $cnt\n";
	close $fh;
	return $total_report;
}

sub main()
{
	my $report = parse_xml();

	open my $ofh, "> $ofile" or die;
	print $ofh "# CTS total failed cases: $cnt\n";
	print $ofh $report;
	close $ofh;
}

main;
