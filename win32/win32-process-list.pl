#!/usr/bin/perl
use strict;
use warnings;

use Win32::Process::List;
use Win32::Process;

my $P = Win32::Process::List->new();
my %tasklist= $P->GetProcesses();

# here ''sort {$a <=> $b} @array'' to sort keys by numeric
foreach my $pid (sort {$a <=> $b} keys %tasklist)  {
    print "$pid $tasklist{$pid}\n"
	#Win32::Process::KillProcess($pid, $errcode);
}
