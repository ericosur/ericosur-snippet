#!/usr/bin/perl

=pod

=head1 DESCRIPTION

1. Use 'ppm upgrade > list' to list the modules need to be upgraded.

2. 'perl all-upgrade.pl list.txt' to call ppm.

=cut

use strict;
use warnings;

use File::Temp qw(tempfile);

my $file = $ARGV[0];

sub main()
{
	unless ($^O eq 'MSWin32')  {
		die "Only run under MSWin32\n";
	}

    my $basedir = Win32::GetCwd();
    my $fh;

    # if specified file exists, use it
    if ( $file && -e $file)  {
        die "file not found: $file";
    } else  {
        # or use temp file at temp dir without opening it
        (undef, $file) = tempfile("pua_XXXX", OPEN => 0, DIR => $ENV{'TEMP'});
        gen_upgrade_list();
    }

    open $fh, $file or die "cannot access $file";

	while (<$fh>)  {
		m/(^\S+)/;
		if ($1)  {
			print $1,"==>\n";
			# issue command to upgrade module '$1'
			my $cmd = sprintf "cmd /c ppm upgrade $1";
			system $cmd;
		}
	}

	close $fh;
}

# List packages that there are upgrades available for.
sub gen_upgrade_list()
{
	my $cmd = "cmd /c ppm upgrade > $file";
	print $cmd,"\n";
	system $cmd;
}

main;
