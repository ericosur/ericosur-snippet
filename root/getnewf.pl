#!/usr/bin/perl
#
# code snippet from
# http://www.perlmonks.org/?node_id=410615
#

#
# 找出日期在 $date 之後的檔案
#

use strict;
use warnings;

use POSIX ();

my $date = 20100101;

open my $fh, "list.txt" or die;


while (<$fh>)  {
	s/[\r\n]//;
	my $file = $_;
	my $mtime = (stat($file))[9];
	if ($mtime)  {
		my $st = POSIX::strftime("%Y%m%d", localtime($mtime));
		if ( int($st) > $date )  {
			print "$file: $st\n";
		}
	}
}

close $fh;
