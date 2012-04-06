#!/usr/bin/perl

# gen cmd from txt

use strict;

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
	testScrollTo => 1,
);


my $file = $ARGV[0] // "failcase.txt";
#print "open $file...\n";
open my $fh, $file or die;
while (<$fh>) {
	if ( m/^(\S+) (\S+)/ ) {
		my ($cname, $mname) = ($1, $2);
		unless ( $known{$mname} )  {
			printf("run cts -c %s -m %s\n", $cname, $mname);
		} else {
			#print STDERR "skip\n";
		}
	}
}
close $fh;
