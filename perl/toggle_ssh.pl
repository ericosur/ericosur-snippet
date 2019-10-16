#!/usr/bin/perl
#
# use cmdow to find "SSH Tunnel" cmd window and hide it
#
# 2007/05/08 by ericosur

use strict;
use warnings;


my $msg = `cmdow`;
my $win_id = undef;
my $status;
my $cmd;
my $postfix;
my $target = 'ericosur@deb';

foreach (split /\n/, $msg)
{
	if (/(0x[0-9a-fA-F]+).*(Vis|Hid).*$target/)
	{
		$win_id = $1;
		$status = $2;
	}
}


if ($win_id && $status)
{
	printf "%s : %s\n", $win_id, $status;

	hide_win($win_id) if ($status eq "Vis");
#	$postfix = "/hid" if ($status eq "Vis");

	show_win($win_id) if ($status eq "Hid");
#	$postfix = "/vis" if ($status eq "Hid");

}
else
{
	print STDERR "not found or not matched\n";
}

sub hide_win()
{
	my $win_id = shift;
	my $cmd = sprintf "cmdow %s /hid", $win_id;

	print STDERR $cmd, "\n";
	system $cmd;
}

sub show_win()
{
	my $win_id = shift;
	my $cmd = sprintf "cmdow %s /vis /act", $win_id;;

	print STDERR $cmd, "\n";
	system $cmd;
}

=pod

=head1 NAME

	toggle_ssh.pl

=head1 USAGE

	just run ''toggle_ssh.pl''

=head1 DESCRIPTION

This script uses ''cmdow'' as utility to hide/reveal the putty terminal
window. It will search the window ID of ssh connection (it was set previously).

The target to be searched is defined at ''$target''.

=cut
