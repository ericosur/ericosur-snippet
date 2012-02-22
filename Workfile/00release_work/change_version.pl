#!/usr/bin/perl

#
# to modify config_system_version.sh and touch buildinfo.sh
#

use strict;
use warnings;
use 5.010;

my $tag;

sub gettag()
{
	# specify a file 'ap-tag' containing version label
	# eg: 0.H03001.00500GEN-enFR.110520.0
	my $tagfile = $ARGV[0] // "ap-tag";
	say "tag file: $tagfile";
	open my $tagfh, $tagfile or die "cannot open tag file: $tagfile...";
	$tag = <$tagfh>;
	$tag =~ s/[\r\n]//;
	close $tagfh;

	say "tag: $tag";
}

sub update_version_file()
{
	my $file = 'device/pega/duke/config_system_version.sh';
	open my $fh, "> $file" or die;

	print $fh "export BUILD_NUMBER=", $tag, "\n";	

	close $fh;
}

sub touch_buildinfo_sh()
{
	my $sfile = 'build/tools/buildinfo.sh';
	my $cmd = 'touch ' . $sfile;
	say $cmd;
	system $cmd;
}

sub main()
{
	gettag();
	update_version_file();
	touch_buildinfo_sh();
}


main;

