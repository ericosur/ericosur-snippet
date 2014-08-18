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
	my ($ct, $ut) = ();
	my ($pct, $put) = ();
	my ($yy, $MM, $dd, $hh, $mm, $ss) = ();

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

			# parse: 2013-07-26 09:35:33.851
			$ct =~ m/(\d+)-(\d+)-(\d+) (\d+):(\d+):(\d+\.\d+)/;
			($yy, $MM, $dd, $hh, $mm, $ss) = ($1, $2, $3, $4, $5, $6);

			#print "prev: $bakline";
			#printf "line(%d) // Sending event %d, subcnt(%d)\n", $lcnt, $val, $subcnt;
			printf "diff: %d\n", ($ut-$put) if $put != 0;
			printf "ln(%s)\tevent(%s)\t%s\t%s\n", $lcnt, $val, $ct, $ut;
			printf "%s_%s_%s  %s_%s_%s\n", $yy, $MM, $dd, $hh, $mm, $ss;
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

    if (-e $myfile) {
	    process_file($myfile);
	} else {
	    my @ff = glob("*monkey.txt");
	    foreach (@ff) {
	        process_file($_);
	    }
	}
}

main;
