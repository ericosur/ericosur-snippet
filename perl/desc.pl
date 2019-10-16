#!/usr/bin/env perl
=pod

=head1 NOTE

B<desc.pl> is a small script to show 'description' field from the
result of 'apt-cache show pkgname'. Only installed packages contain
correct description.
=cut

use strict;
use warnings;
use Getopt::Std;

die 'run only in linux' if $^O ne 'linux';

my $debug = 0;

sub mygrep($)
{
	my $res = shift;
	my $flag = 0;
	my @cc = split /\n/, $res;

	foreach my $ln ( @cc )  {
		print STDERR $ln,"\n" if $debug;
		if ( $ln =~ m/^Description[^:]*:/ )  {
			$flag = 1;
		}
		if ($flag == 1)  {
			if ( $ln =~ m/^Bugs:/ )  {
				$flag = 0;
				print STDERR "exit...\n" if $debug;
				last;
			}
			print $ln,"\n";
		}
	}
	return $res;
}

sub main()
{
	if (!@ARGV)  {
		die "你需要指定一個套件名稱 (may use dpkg -l)";
	}
 	my %my_opt;
	getopts('d', \%my_opt); # -o & -i are boolean value, -f take argument
	$debug = $my_opt{'d'} || 0;

	my $cmd = 'apt-cache show ' . $ARGV[0];
	my $cnt = `$cmd`;
	mygrep($cnt);
}

main;

