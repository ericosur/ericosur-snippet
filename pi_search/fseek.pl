#!/usr/bin/perl

use strict;

my $file = "pigg.txt";
my $goto_addr = $ARGV[0] || 0;
my $buf_size = $ARGV[1] || 128;
my $buf;

open my $ifh, $file or die;

seek $ifh, $goto_addr, 0;
my $real_read = read $ifh, $buf, $buf_size;
print $buf;
close $ifh;
printf "\nreal_read: %d\nbuf_size = %d\npos: %d\n",
	$real_read, $buf_size, $goto_addr;
