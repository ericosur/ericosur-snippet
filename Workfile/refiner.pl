#!/usr/bin/perl

#
# �ѩ� project.cfg �̭��� APPLICATIONS �H�� FEATURE
# �o����ܼƭȤӪ����H�[��νs��A�ҥH�w��o�����
# �ưʤ@�I��}�A�Ȫ����e�|�̷Ӧr�����ǱƦC�B�W�߬�
# �@��@��A��K���M�s��C
#
# ���ɮרä��|�Q��g�A��z�L���ɦW��b $mycfgfile
# �o���ܼơC
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
