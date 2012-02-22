#!/usr/bin/perl
#
# opendir test
#
# 2006/12/27 by ericosur

use strict;
use warnings;

use Cwd;

sub process($);
sub opensubdir($);


sub process($)
{
	my $basedir = shift;
	my @subdirs = {};

	if ( defined $basedir )  {
		opendir(DIR, $basedir) || die "can't open dir $!\n";
		@subdirs = grep { -d "$basedir/$_" && !(/^\./) } readdir(DIR);
		closedir DIR;
		foreach (@subdirs)  {
			my $localdir = "$basedir/$_";
			process($localdir);
		}
	}

	return @subdirs;
}

sub opensubdir($)
{
	my $dirs = shift;

	print "$dirs\n";
}

sub main()
{
	my $basedir = getcwd();
	print "cwd: $basedir\n";

	my @result = process($basedir);
	foreach (@result) {
		my $localdir = "$basedir/$_";
		#print "$localdir\n";
		opensubdir($localdir);
	}
}

main;

