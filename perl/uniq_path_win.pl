#!/usr/bin/perl

use strict;
use warnings;

die "only work at MSWin32" if ($^O ne "MSWin32");
use if $^O eq "MSWin32","Win32";
use if $^O eq "MSWin32","Win32::Clipboard";
use Env qw(@PATH $PATH);

sub uniq(@)
{
	my %seen = ();
	my @result = grep { ! $seen{$_} ++ } @_;

	while ( my ($k,$v) = each(%seen) )  {
		print STDERR "==> duplicated: ", $k, "\n" if $v > 1;
	}
	return @result;
}

sub shorten_path($)
{
	my $arg = shift;

	$arg =~ s/[\r\n]//g;
	if (! -e $arg || ! -d _)  {
		print STDERR "==> <$arg> not exists ?\n";
		return;
	}

	my $short = Win32::GetShortPathName($arg);

	if ($short)  {
		$short =~ s(\\$)();		# remove the trailing ''\''
		return $short;
	}
	else  {
		return $arg;
	}
}

sub main
{
	print STDERR "==> before count: ", $#PATH+1, "\n";
	#@PATH = map { shorten_path($_) } @PATH;
	#print STDERR "==> after count: ", $#PATH+1, "\n";
	#print STDERR join(';', @newp), "\n";

	@PATH = uniq(@PATH);
	print STDERR "==> after count: ", $#PATH+1, "\n";
	#print $#PATH, "\n";

	print STDERR "==> result has already copied into clipboard\n";
	Win32::Clipboard()->Set($PATH);
	print $PATH,"\n";
}

main;
