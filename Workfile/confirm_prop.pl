#!/usr/bin/perl

=pod
	Script to check the properties matched to predefined values.

HOW TO USE
	you may run 'adb shell getprop > prop.txt' to generate default test cases. The format is

[keys]: [value]

Failed cases would be output to 'fail.txt'. 
Symbol '.' means pass, and 'x' means failed.

AUTHOR
	rasmus_lai@gmail.com

=cut

use strict;
use warnings;
use v5.10;

my $debug = 0;

sub load_test($)
{
	my $ff = shift;
	my %tests = ();
	my $cnt = 0;
	open my $fh, $ff or die "failed to load $ff";
	while (<$fh>)  {
		if ( m/\[(\S+)\]: \[([^]]*)\]/ )  {
			say $1,"\t",$2 if $debug;
			$tests{$1} = $2;
			++$cnt;
		} else {
			print "failed to load: $_";
		}
	}
	close $fh;
	say "$cnt cases loaded";
	return %tests;
}

sub run_test($)
{
	my $ff = shift;
	my %tests = load_test($ff);
	my ($cnt,$fail) = (0,0);
	say "please turn on USB debugging...";
	system('adb wait-for-device');
	foreach my $kk (keys %tests)  {
		my $cmd = 'adb shell getprop ' . $kk;
		my $res = `$cmd`;
		++ $cnt;
		$res =~ s/[\r\n]//g;
		if ($res eq $tests{$kk})  {
			print '.';
		} else {
			print 'x';
			++ $fail;
			output_fail_case($kk, $tests{$kk}, $res);
		}
	}
	print "\ntotal: $cnt\nfail: $fail\n";	
}

sub output_fail_case($$$)
{
	my ($kk,$ss,$rr) = @_;
	my $file = 'fail.txt';
	open my $ofh, ">> $file" or die;
	my $log = sprintf("key(%s) suppose(%s) get(%s)\n", $kk, $ss, $rr);
	print $ofh $log;
	close $ofh;
}

sub main()
{
	my $file = 'prop.txt';	# take it as test cases
	#load_test($file);
	run_test($file);
}

main;

