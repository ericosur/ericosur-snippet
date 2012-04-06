#!/usr/bin/perl

# http://10.193.95.212/cts/avalon/2012.03.21_11.15.59/2012.03.21_11.15.59/2012.03.21_11.15.59/cts_result.css

use strict;
use Getopt::Std;

sub help()
{
	print<<EOL;
-p specify project name like 'avalon' or 'sphinx'
-d specify dateid, it is MUST
EOL
}

sub main()
{
	my @apps = qw(cts_result.css cts_result.xsl logo.gif newrule-green.png testResult.xml);
	my $host = "http://10.193.95.212/cts/";
	my $prj; # = "avalon";
	my $dateid; # = $ARGV[0] || die "Need specify dateid, like 2012.03.21_01.43.52";
	my $cmd;

	my %opts;
	my $optcmd = 'd:p:hast';

	getopts($optcmd, \%opts);

	if ($opts{h})  {
		help();
		exit 1;
	}

	$prj = "";
	if ($opts{a})  {
		$prj = 'avalon';
	} elsif ($opts{s}) {
		$prj = 'sphinx';
	} elsif ($opts{t}) {
		$prj = 'titan';
	} elsif ($opts{p}) {
		$prj = $opts{p};
	}

	$dateid = $opts{d} || die "Need specify dateid, like 2012.03.21_01.43.52";
	die "Need specify project id" if ($prj eq "");

	foreach my $app (@apps) {
		$cmd = sprintf("curl -O %s%s/%s/%s/%s/%s", $host,
			$prj, $dateid, $dateid, $dateid, $app);
		print $cmd,"\n";
		system $cmd;
	}

	my $files = join(' ', @apps);
	$cmd = sprintf("mkdir %s", $dateid);
	system $cmd;
	$cmd = sprintf("mv %s %s", $files, $dateid);
	system $cmd;

	#$cmd = sprintf("zip %s.zip %s", $dateid, $files);
	#system $cmd;
	#$cmd = "del " . $files;
	#system $cmd;
}

main;
