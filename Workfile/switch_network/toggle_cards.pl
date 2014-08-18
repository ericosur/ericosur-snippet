#!/usr/bin/env perl
#
# need 'devcon.exe' in path
# to toggle wireless and LAN card
#

use strict;
use warnings;

#
# you need change if hardware changed
#
my $lan_card = q(pci\ven_10ec*dev_8139*);
my $lan_status = 999;	# 999: none, 1: enable, 0: disable
my $wifi_card = q(usb\vid_a727*pid_6893*);
my $wifi_status = 999;


sub main()
{
	my $lan_status = get_status($lan_card);
	if ($lan_status)  {
		print "go wifi\n";
		go_wifi();
	}
	else  {
		print "go lan\n";
		go_lan();
	}
}


sub test()
{

	$lan_status = get_status($lan_card);
	print "lan card = $lan_status\n";
	toggle_status($lan_card, !$lan_status);

	sleep 1;

	$wifi_status = get_status($wifi_card);
	print "wifi card = $wifi_status\n";
	toggle_status($wifi_card, !$wifi_status);
}


sub go_wifi()
{
	toggle_status($wifi_card, 1);
	toggle_status($lan_card, 0);
}


sub go_lan()
{
	toggle_status($lan_card, 1);
	toggle_status($wifi_card, 0);
}


# arg1: hardware string
# arg2: 1: turn on, 0: turn off
#
sub toggle_status($$)
{
	my $cmd;
	my $dev = shift;
	my $act = shift || 0;
	my %action = (0 => 'disable', 1 => 'enable');

	$cmd = sprintf("devcon %s %s", $action{$act}, $dev);
	print $cmd,"\n";
	system $cmd;
}


sub get_status($)
{
	my $cmd;
	my $result;
	my $dev = shift;
	my $status = 999;

	$cmd = sprintf("devcon status %s", $dev);
	$result = `$cmd`;
	#print $result;

	if ($result =~ m/disabled/i)
	{
		$status = 0;
		print "disabled\n";
	}
	elsif ($result =~ m/running/i)
	{
		$status = 1;
		print "running\n";
	}

	return $status;
}


main;

__END__;
