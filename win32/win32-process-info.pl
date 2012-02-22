#!/usr/bin/perl
use strict;
use warnings;

use Win32::Process::Info;
use Data::Dumper;

my $pi;
my @info;

$pi = Win32::Process::Info->new ();
$pi->Set (elapsed_in_seconds => 0);    # In clunks, not seconds.

#my @pids = $pi->ListPids ();      # Get all known PIDs
#@info = $pi->GetProcInfo ();   # Get the max
#my %sub_proc = $pi->Subprocesses ();  # Figure out subprocess relationships.
@info = grep {$_->{Name} =~ m/perl/}
	$pi->GetProcInfo ();        # All processes with 'perl' in name.

print Dumper(@info);
