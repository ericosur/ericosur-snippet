#!/usr/bin/perl

#
# 由於 project.cfg 裡面的 APPLICATIONS 以及 FEATURE
# 這兩個變數值太長難以觀察及編輯，所以針對這兩個變
# 數動一點手腳，值的內容會依照字母順序排列且獨立為
# 一行一行，方便比對和編輯。
#
# 原檔案並不會被改寫，整理過的檔名放在 $mycfgfile
# 這個變數。
#
# now we have no such file to use, so such is only for reference
#
# Dec 2 2004 by ericosur
#

use strict;
use warnings;


print STDERR "########## project.cfg refiner ##########\n";

my $cfgfile = $ARGV[0] || "project.cfg";
my $mycfgfile = $cfgfile . ".refined";

unless ( -e $cfgfile )  {
	die "cannot locate $cfgfile\n";
}

print STDERR "process [$cfgfile] and output to [$mycfgfile]\n";

open CFG, "< $cfgfile" or die "cannot read $!\n";
unlink $mycfgfile if ( -e $mycfgfile );
open MYCFG, "> $mycfgfile" or die "cannot write $!\n";

LOOP:
while ( <CFG> )  {

	/(\w+)=(.+)/;
	my $lhs = $1;
	my $rhs = $2;

	if ( $lhs eq "APPLICATIONS" || $lhs eq "FEATURE" )  {

		my @app = split / /, $rhs;
		my @sorted = sort {$a cmp $b} @app;

		print MYCFG $lhs . "= \\\n";
		foreach (@sorted)  {
			print MYCFG "\t$_ \\\n";
		}
		print MYCFG "\n";
	}
	else {
		print MYCFG $_;
	}

}

close CFG;
close MYCFG;

print "done!\n";
