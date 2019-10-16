#!/usr/bin/env perl
=pod

=head1 NOTE

To list figlet fonts by its own font type.
''B<figlist>'' would list control files as well, not only font files.

B<figlet> is a ASCII art program.

=cut

use strict;

die "cannot run in win32" if $^O eq "MSWin32";	# cannot run under win32

my $figlet_path = '/usr/share/figlet/';
my @fl = glob($figlet_path . '*.flf');	# list only figlet font file
foreach (@fl)  {
	m/\/(\w+)\.flf$/;
	my $cmd = "figlet -f $1 $1";
	print $1,"\n";
	system $cmd;
}

