#!/usr/bin/perl

#
# use ''dir /s/b *.pl > list.txt''
# run this script
#
# the output would translate:
# 1. current working directory into ''.''
# 2. back slash ''\'' into slash ''/''
#
# input:  D:\script\test\aparture.pl
# output: ./test/aparture.pl
#
# 2007/03/21 by ericosur

use strict;
use warnings;

use Cwd;

#
# return like 'D:/script'
# same as Cwd::cwd()
#
sub get_dos_cwd()
{
	$_ = `echo %cd%`;
	s/\r//;
	s/\n//;
	s/\\/\//g;
	return $_;
}

sub main()
{
	my $listfile = $ARGV[0] || "list.txt";
	my $content;

	my $CWD = get_dos_cwd();
	print "get_dos_cwd(): ", $CWD, "\n";
	print "use Cwd: ", cwd(),"\n";

	if (-f $listfile)  {
		print "list exists\n";
		open FH, "< $listfile" or die "cannot open: $!\n";
		undef $/;
		$content = <FH>;	# read the whole file in (not good if the file is very large)
		close FH;
	}
	else  {
		print "no list file found, try to make one...\n";
		if ( $^O eq 'MSWin32' )  {
			$content = `cmd /c dir /s /b`;	# you cannot just use `dir /s /b` to call DOS command
		} elsif ($^O eq 'linux')  {
			# use 'find' exclude files under .svn/
			$content = `find . -path '*/.svn' -prune -o -type f`;
		}
	}

	#print "1:<$content>\n";

	my $count = 0;
	LOOP:
	for (split /\n/, $content)  {
		s/\\/\//g;	# \ --> /
		s/$CWD/\./;

		print $_, "\n";
		$count ++;
	}

	print STDERR "# count = $count\n";

}

main;
