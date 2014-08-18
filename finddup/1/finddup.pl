#!/usr/bin/perl

#use strict;

#
# 2006/12/27 by ericosur
#

require 'filedata.ph';

my $cnt = 0;
my $dup = 0;

foreach my $ii (@files)
{
#	printf "%s\n", $ii->{file};

innerloop:
	foreach my $jj (@files)
	{
		$cnt ++;
		if ( $ii->{hash} eq $jj->{hash} )
		{
			if ( $ii->{file} eq $jj->{file} )
			{
				# exact the same file, skip
				next innerloop;
			}
			else
			{
				$dup ++;
				printf "  %s\n# %s\n", $ii->{file}, $jj->{file};
				#printf "%s\n", $ii->{file};
				#print "<$dup>...", if ++$dup % 10 == 0;

			}
		}
#		print "$cnt...\n" if $cnt % 100 == 0;
	}
}

printf "cnt = %d, dup = %d\n", $cnt, $dup;
