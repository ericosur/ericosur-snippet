#!/usr/bin/perl
#
# use ''cmdow'' to find "SSH Tunnel" cmd window and hide it
#
# cmdow (http://www.commandline.co.uk/cmdow/)
#
# 2007/01/18 by ericosur

use strict;
use warnings;


my $msg = `cmdow`;
my $win_id = undef;
my $cmd;

foreach (split /\n/, $msg)
{
	$win_id = $1 if /(0x[0-9a-fA-F]+)(.*)SSH Tunnel/;
}

if ($win_id)
{
#	print STDERR "Hide the target win id = ", $win_id;
	$cmd = sprintf "cmdow %s /hid", $win_id;
	print STDERR $cmd, "\n";
	system $cmd;
}
else
{
	print STDERR "not found\n";
}
