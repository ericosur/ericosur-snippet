#!/usr/bin/perl
#
# help me to issue git-pull commands from local bsp directory 
# to local branch
#
# need pull_git.conf and selected_git.txt
#

use strict;
use warnings;
use v5.10;

my $from;
my $to;
my $bsp_dir;
my @arr;
my $opt_actual_run = 0;
my $opt_test_run = 0;
my $ini_name = 'pull-git.conf';

# module list for pulling
my $list;

sub get_conf($)
{
	my $ini = shift;
	open my $fh, $ini or die;
	while (<$fh>)  {
		next if /^$/;
		next if /^#/;
		s/[\n\r]//;
		say $_;
		eval($_);
	}
	close $fh;
}

sub open_list($)
{
	my $ff = shift;
	open my $fh, $ff or die;
	while ( <$fh> ) {
		next if m/^#/;
		s/[\r\n]//;
		push @arr,$_;
	}
	close $fh;
}

sub compose_cmd($)
{
	my $org = shift;
	my $cmd;

	foreach (@arr)  {
		my $dir = $org . '/' . $_;
		die "cannot chdir to $dir" unless chdir $dir;
		$cmd = sprintf("git pull %s %s/%s  %s:%s",
			($opt_test_run ? "--no-commit" : " "), 
			$bsp_dir, $_, $from, $to);
		say $cmd;
		system $cmd if ($opt_actual_run || $opt_test_run);
		die unless chdir $org;
	}
}

sub main()
{
	$opt_actual_run = 0;
	$opt_test_run = 0;
	if (defined($ARGV[0]))  {
		if ($ARGV[0] eq 'go')  {
			$opt_actual_run = 1;
		} elsif ($ARGV[0] eq 'test')  {
			$opt_test_run = 1;
		}
	}

	get_conf($ini_name);

	if ($opt_actual_run == 1)  {
		say "NOTE: it will pull the repository!";
	} elsif ($opt_test_run == 1)  {
		say "NOTE: test run";
	} else  {
		say "NOTE: not really execute the command!";
	}
	say "pysical pwd: ", `pwd -P`;
	say "please CONFIRM and press ENTER to continue...";
	my $tmp = <STDIN>;
	my $pwd = $ENV{'PWD'};
	open_list($list);
	compose_cmd($pwd);
}

main;

