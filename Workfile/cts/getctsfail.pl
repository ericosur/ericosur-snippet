#!/usr/bin/perl

use strict;
use warnings;
use 5.010;

my $file = 'testResult.xml';
my %known = (
	testExponentParsing => 1,
	testNamedFloats => 1,
	testSuffixParsing => 1,
	testVerifierTyping => 1,
	test_valueOf_String1 => 1,
	test_valueOf_String2 => 1,
	testInspectSslAfterConnect => 1,
	testMeasureTextWithLongText => 1,
	testAccessAllowFileAccess => 1,
);


sub main()
{
	my @arr = ();
	my $tcase;
	my $filter_cnt = 0;
	my $cnt = 0;

	open my $fh, $file or die;
	while (<$fh>) {
		# <TestPackage name="CtsAnimationTestCases"
		if ( m/^\s+<TestPackage name=\"([^\"]+)\"/ ) {
			@arr = ();
			#printf("test package: %s\n", $1);
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
				printf("%s.%s %s\n", $cname, $tcase, $fail);
				$filter_cnt += 1;
			}
		}
	}
	print STDERR "filtered: $filter_cnt\ntotal: $cnt\n";
	close $fh;
}


main;