#!/usr/bin/perl

use strict;
use warnings;
use Data::Dump qw(dump);

sub rename_file($$);

my $str_strict = "use strict;";
my $str_warn = "use warnings;";

my @files = glob("*.pl");

my $foo = 0;
my $bar = 0;

foreach (@files)  {

	my $inf = $_;
	s/\.pl/\.tmp/;
	my $outf = $_;

	print STDERR "$inf\n$outf\n";
	undef $/;
	open my $fh, $inf or die "$!\n";

	$_ = <$fh>;
	close $fh;

#	dump @lines;
	$foo = 1, print 's' if m/$str_strict/;
	$bar = 1, print "w" if m/$str_warn/;

	if ($foo eq 1 and $bar eq 0)  {
		s/($str_strict)/$1\n$str_warn\n/;
		open my $ofh, "> $outf" or die "$!\n";
		print $ofh $_;
		close $ofh;
		my $backup = rename_file($inf, $outf);
		print STDERR "bakcup as $backup\n";
	}
	else  {
		print STDERR "no output file\n";
	}

	($foo, $bar) = (0, 0);
}

sub rename_file($$)
{
	my ($src, $tmp) = @_;
	my $bak = $src;
	$bak =~ s/\.pl/\.bak/;

	rename $src, $bak;
	rename $tmp, $src;

	return $bak;
}
