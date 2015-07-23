#!/usr/bin/perl
#
# get registry data demo
# list all the tips of the day from registry
#
# 2007/10/12 by ericosur
#

use strict;
use warnings;

no strict 'refs';
use Win32::TieRegistry;

sub main()
{
	LINE:
	while (<DATA>)  {
		s/\n//;
		next LINE if /^#/;
		last LINE if /^$/;

		print '-' x 60, "\n";
		printf "==> Read registry value from:\n%s\n", $_;

		$Registry->Delimiter("\\");

		my $pair = $Registry->{$_};
		printOut($pair, $_);

		undef $pair;
	}
}

sub printOut(\%$)
{
	my $rh = shift;
	my $name = shift;

	print '=' x ((76-length($name))/2), "<$name>", "=" x ((76-length($name))/2), "\n";
	for (keys %$rh)  {
		my $k = $_;
		$k =~ s!^[\/\\]!!;
		if (ref($rh->{$_}) eq "Win32::TieRegistry")  {
			printf "[%s]=[%s]\n", $k, $rh->{$_} if $k;
			printOut($rh->{$_}, $_);
		}
		else  {
			printf "[%s]=[%s]\n", $k, $rh->{$_} if $k;
		}
	}
}

main();

# the key path is copy from regedit.exe GUI
__DATA__
#HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

__END__


>> reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment"

	print "-"x40,"\n";
	print %$pair->{"Environment"}->{"Path"};
