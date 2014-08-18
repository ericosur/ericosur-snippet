#!/usr/bin/env perl

#
# to patch test.pac
#
#
# to find this line:
# if (myIpAddress() == "10.193.82.64")
#

use strict;
use warnings;

use Sys::Hostname;
use Socket;

sub get_localip()
{
	my ($addr) = inet_ntoa( (gethostbyname(hostname()))[4] );
	return $addr;
}

# arg1: file to patch
# arg2: string to patch
sub patch_pac($$)
{
	my $ifile = shift;
	my $str = shift;

	die "file not found" if (not -e $ifile);
	my $ofile = $ifile;
	$ofile =~ s/\.pac/\.tmp/;

	open my $ifh, $ifile or die;
	open my $ofh, "> $ofile" or die;

	while (<$ifh>)  {
		if ( m/myIpAddress\(\) == \"([^\"]+)\"/ )  {
			print "found! $1\n";
			print $ofh $_;
			if ($1 ne $str)  {
				print "insert!\n";
				print $ofh <<EOL;
		|| (myIpAddress() == "$str")
EOL
			}
		}
		else  {
			print $ofh $_;
		}
	}

	close $ifh;
	close $ofh;

	my $bakname = $ifile;
	$bakname =~ s/\.pac/\.bak/;
	rename $ifile, $bakname;
	rename $ofile, $ifile;
}


sub main()
{
	my $ip;

	$ip = get_localip();
	print "ip = $ip\n";

	patch_pac("test.pac", $ip);
}

main;
