#!/usr/bin/perl
#
# rasmus@indigo
# Oct 29 2007
# enclose #ifndef ... #endif to the target...
#
#


use strict;

my $file = $ARGV[0] or "EmailAppUIInterface.c";
my $outfile = $file . ".out";
my $count = 0;
my $hit_count = 0;
#
# target here
#
my $target = qr[SetKeyHandler.+KEY_(LEFT|RIGHT)_ARROW];
#
#
#

print "input <$file>\n";
open FH, "$file" or die;
print "output <$outfile>\n";
open OUTFH, "> $outfile" or die;

READLINE:
while (<FH>)
{
	++$count;
#	s/\n//;
#	s/\r//;
#	print;
#	print "\n";
	if ( m/$target/ )
	{
		++ $hit_count;
		print OUTFH<<EOL;
#ifndef __MMI_UE_DISABLE_ENTRY_FUNC_BY_NAVI_KEY__	// rasmus\@indigo 2007/10/31 disable entry/exit by navi key  {
EOL
		print OUTFH;
		print OUTFH<<EOLL;
#endif	// rasmus\@indigo 2007/10/31 disable entry/exit by navi key  }
EOLL
	}
	else
	{
		print OUTFH;
	}
}
close FH;
close OUTFH;

printf "\thit: %d\ttotal: %d\n", $hit_count, $count;

__END__;

#ifndef __MMI_UE_DISABLE_ENTRY_FUNC_BY_NAVI_KEY__
#endif

KEY_LEFT_ARROW
KEY_RIGHT_ARROW
SetKeyHandler(GoBackHistory, KEY_LEFT_ARROW, KEY_EVENT_DOWN);
