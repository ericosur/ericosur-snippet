#!/usr/bin/perl

use strict;

sub main()
{
	my $inf = 'system.img';
	my $outf = 'pad.img';
	my $total_len = 536870912;
	my $ret;
	my $write_len = 0;
	my $buf;
	my $bufsize = 500*1024;

	open my $ifh, $inf or die;
	binmode $ifh;
	open my $ofh, "> $outf" or die;
	binmode $ofh;

	# read common part and output
	while (1) {
		$ret = read($ifh, $buf, $bufsize);
		last if ($ret eq 0);
		print $ofh $buf;
		$write_len += $ret;
	}

	print "write_len: $write_len\n";
	# perform padding
	my $pad_len = $total_len - $write_len;
	print "pad len: $pad_len\n";
	
#=pod
	for (my $i=0; $i<$pad_len; $i++) {
		print $ofh "\0";
	}	
#=cut

	close $ifh;
	close $ofh;

}

main;


