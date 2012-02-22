#!/usr/bin/perl
#﻿
# rename all subdir with '_' to '-' in the current sub folder
# the pattern: ``^(\d+)_(\d+)_(\d+)(.*)$''
#
# use ''rdir.pl go'' would take the changes
#

use strict;
use warnings;
use Cwd;

sub getsubdir($)
{
	my $basedir = shift;
	my @subdirs = {};

	if ( defined $basedir )  {
		opendir(DIR, $basedir) || die "can't open dir $!\n";
		@subdirs = grep { -d "$basedir/$_" && !(/^\./) } readdir(DIR);
		closedir DIR;
	}

	return @subdirs;
}

sub main
{
	my $basedir = getcwd();
	my @sd = getsubdir($basedir);
	my $go = 0;

	if ($ARGV[0] && $ARGV[0] eq 'go')  {
		$go = 1;
	}

	my ($oldf, $newf);
	foreach (@sd)  {
		$oldf = $_;
		if ( s[^(\d+)_(\d+)_(\d+)(.*)$][$1-$2-$3$4] )  {
			$newf = $_;
			print STDERR ">>> rename $oldf, $newf -> ";
			if ($go == 1)  {
				rename $oldf, $newf;
				print STDERR "done\n";
			}
			else {
				print STDERR "preview\n";
			}
		}
	}
}

main;

__END__;
