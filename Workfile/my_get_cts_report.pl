#!/usr/bin/perl

# http://10.193.95.212/cts/avalon/2012.03.21_11.15.59/2012.03.21_11.15.59/2012.03.21_11.15.59/cts_result.css

my $host = "http://10.193.95.212/cts/";
my $prj = "avalon";
my $dateid = $ARGV[0] || die "Need specify dateid, like 2012.03.21_01.43.52";
my @apps = qw(cts_result.css cts_result.xsl logo.gif newrule-green.png testResult.xml);
my $cmd;

foreach my $app (@apps) {
	$cmd = sprintf("curl -O %s%s/%s/%s/%s/%s", $host,
		$prj, $dateid, $dateid, $dateid, $app);
	print $cmd,"\n";
	system $cmd;
}

my $files = join(' ', @apps);
$cmd = sprintf("zip %s.zip %s", $dateid, $files);
system $cmd;
$cmd = "del " . $files;
system $cmd;
