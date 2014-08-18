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
	my $cmd;

	chdir $dirs;
	#print "chdir $dirs\n";
	$cmd = sprintf("svn update");
	#print getcwd(),"\n";
	system $cmd;
	chdir "..";
}

sub main()
{
	my $basedir = getcwd();
	print "cwd: $basedir\n";

	my @result = process($basedir);
	foreach (@result) {
		my $localdir = "$basedir/$_";
		opensubdir($localdir);
	}
}

main;

