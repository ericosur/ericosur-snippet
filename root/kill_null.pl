#!/usr/bin/perl
#
# 2006/12/27 by ericosur
# delete null lines
#

while ( <> )  {
	unless (/^$/)  {
		print $_;
	}
}
