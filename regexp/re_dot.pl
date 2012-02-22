#!/usr/bin/perl
#
# some regex practice
#

use strict;

my @qrs = (
	qr((.*[.])[^be]*$),	# the result does not we want
	qr((.*[.])(?=bat$|exe$)(.*)$),	# use neg lookahead
	qr((.*[.])(?!bat$|exe$)(.*)$),	# use neg lookahead
	qr((.*[.])^(bat)$),		# it's wrong and match nothing
);

while (<DATA>)  {
	s/\n//;
	for my $regex (@qrs)  {
		if ( m/$regex/ )  {
			printf "(%s) matches /%s/\n", $_, $regex;
			print "\t$1 => $1\n" if $1;
		}
	}
}

__DATA__
autoexec.bat
tempture.bc
sendmail.cf
ssh.conf
cmd.exe
averylog.execute
news.rc
