#!/usr/bin/perl
﻿use strict;

my @files = qw(gb2312_to_ucs2_table.txt ucs2_to_gb2312_table.txt);
my @ofiles = qw(g2u.txt u2g.txt);

sub write_table($$)
{
	my ($ifile, $ofile) = @_;

	my $line = 0;
	my $debug = 0;
	my $octet = 0;

	my ($ifh, $ofh);
	print STDERR "from: $ifile\nto: $ofile\n";

	open $ifh, $ifile or die;
	open $ofh, "> $ofile" or die;
	binmode $ofh;

	while (<$ifh>)  {
		++ $line;
		s/[\n{}]//g;
		s/^\s+//;
		next if /^#/;
		next if /^$/;
		print "<$_>\n" if ($debug);

		while ( m/0x([0-9A-F]{4})/g )  {
			++ $octet;
			#print $ofh $octet, "\t", $1, "\n" if $1;
			print $ofh $1, "\n" if $1;
		}
		last if ($debug && $line > 3 );
	}

	close $ifh;
	close $ofh;

	print STDERR "octet = $octet\n";
}

########## main start here ##########
foreach my $ff (@files)  {
	my $oo = shift @ofiles;
	write_table($ff, $oo);
}
