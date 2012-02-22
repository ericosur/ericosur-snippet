#!/usr/bin/perl

# add number to image resource

use strict;

my $file = 'CustImgRes.c';
my $ofile = '00CustImgRes_addnum.c';

my $flag = 0;
my $cnt;

open my $fh, $file or die;
open my $ofh, "> $ofile" or die;

while (<$fh>)  {
	if ($flag == 0)  {
		if ( m/mtk_nCustImageNames/ )  {
			$flag = 1;
			$cnt = 1;
		}
		print $ofh $_;
	}
	elsif ($flag == 1)  {
		if ( m/^\(U8\*\)/ )  {
			printf $ofh "/* %d */ %s", $cnt, $_;
			++ $cnt;
		}
		else  {
			print $ofh $_;
		}
	}
}

close $fh;
close $ofh;
