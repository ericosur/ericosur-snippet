#!/usr/bin/perl

# findpi.pl

use strict;
use Term::ANSIColor qw(:constants);

my $file = "pigg.txt";
my $ifh;
my $win_len = 1024 * 1024;	# 1MB buffer
my $look_len = 25;
my $debug = 0;

my $p = $ARGV[0] || "064810";
my $slide_len = length($p);

open $ifh, $file or die;
print STDERR "OPEN $file to search <$p>\n";
my $fpos = 0;
my $buf;
my $flag = 0;	# 1 if actual read size smaller than desired
my $c = 0;	# the cound to read from file
my ($ff, $tt) = (0, 0);

OUTER:
while ( 1 )  {

	my $realread = read $ifh, $buf, $win_len;
	$c ++;

	if ($realread < $win_len)  {
		print STDERR "buffer read is smaller than expected\n" if $debug;
		print STDERR "fpos: ", $fpos, "\n";
		$flag = 1;
	}

	$tt = $ff + $realread;
	printf STDERR "from %d to %d\n", $ff, $tt if $debug;

	$buf =~ s/\s+//g;
	#print $buf,"\n";
	while ( $buf =~ m/$p/g )  {
		my $pp = pos($buf);
		printf "found at %d\n", $ff + $pp - length($p);

		my ($mm, $nn) = ($`, $');
		print substr($mm, length($mm)-$look_len, $look_len);
		print BOLD, YELLOW, $p, RESET;
		print substr($nn, 0, $look_len),"\n";
	}

	last if $flag;
	$fpos = tell $ifh;
	my $spos = $fpos - $slide_len + 1;
	seek $ifh, $spos, 0;
	$ff = tell($ifh);
	print STDERR "ff: ", $ff, "\n" if $debug;

	#last if $c > 5;
}

close $ifh;
print "c: $c\n" if $debug;
