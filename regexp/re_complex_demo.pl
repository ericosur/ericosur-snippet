#!/usr/bin/perl
#
# small demo about perl code in regexp
#
# 2007/01/19 by ericosur

"abcdefgh" =~ m{
	(?{ print "starting match at [$`|$']\n" })
	(?:d|e|f)
}x;


# (?{ print "starting match at [$`|$']\n" })
