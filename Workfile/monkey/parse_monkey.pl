#!/usr/bin/perl

use strict;

#my $myfile = "20130610_110231_monkey.txt";
my $myfile = "mm.txt";

sub process_file($)
{
    my $file = shift;
	my $lcnt = 0;
	my $val = 0;
	my $subcnt = 0;
	my $bakline;
	my ($ct, $ut) = (0, 0);
	my ($pct, $put) = (0, 0);

	open my $fh, $file or die;
	while (<$fh>) {
		++$lcnt;
		# // Sending event #473300
		if ( m/\/\/ Sending event #(\d+)/ ) {
			if ($val == $1) {
				#print "duplicated...\n";
			}
			$val = $1;
			$bakline =~ m/calendar_time:(.+)  system_uptime:(\d+)/;
			($ct, $ut) = ($1, $2);
			#print "prev: $bakline";
			#printf "line(%d) // Sending event %d, subcnt(%d)\n", $lcnt, $val, $subcnt;
			printf "%s\t%s\t%s\t%s\n", $lcnt, $val, $ct, $ut;
			printf "diff: %d\n", ($ut-$put) if $put != 0;
			$subcnt = 0;
			($pct, $put) = ($ct, $ut);
		}
		if ( m/^:/ ) {
			++ $subcnt;
		}
		$bakline = $_;
	}
	close $fh;
}

sub main()
{
	process_file($myfile);
}

main;
