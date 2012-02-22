#!/usr/bin/perl

# add '''no strict 'refs'''' to specified file
# after the '''use strict'''

use strict;
use warnings;
use 5.010;

my $debug = 0;

sub insert_line($)
{
	my $ifile = shift;
	my $ifh;
	my $ofile = $ifile;
	my $ofh;
	my $bfile = $ifile;

	open $ifh, $ifile or die;
	$ofile =~ s/^(.*)\.pl/$1\.pl\.tmp/;
	$bfile =~ s/^(.*)\.pl/$1\.pl\.bak/;
	open $ofh, "> $ofile" or die;

	while ( <$ifh> )  {
		if (/^#/)  {
			print $ofh $_;
			next;
		}
		if ( m/^\s*use strict;/ )  {
			print $ofh $_;
			print $ofh "no strict 'refs';\n";
		}
		else  {
			print $ofh $_;
		}
	}

	close $ofh;
	close $ifh;

	say "output to $ofile" if $debug;
	say "rename $ifile to $bfile";
	rename $ifile, $bfile;
	say "rename $ofile to $ifile";
	rename $ofile, $ifile;
}

sub main()
{
	if (not @ARGV)  {
		die "please specify script to process!";
	}

	while (@ARGV)  {
		insert_line(shift @ARGV);
	}
}

main;
