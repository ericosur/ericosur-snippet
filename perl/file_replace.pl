#!/usr/bin/perl

#
# 2006/12/27 by ericosur
#

use strict;
use warnings;


# replace text in the file

my $file = "frep.txt";

# create a demo file
open OF, ">$file" or die;

print OF<<EOS;
Dear NAME:
	Mrs. NAME has informed you that your asset would be
transferred into the account of Mrs. NAME. Hopefully Mr.
NAME you should take card about this as soon as possible.

Best Regards your son
NAME
EOS
close OF;

# replace text in the open file
open DATA, "+<$file";
my @data = <DATA>;
seek DATA, 0, 0;
foreach (@data)
{
	s/NAME/Smith/;
	print DATA $_;
}
truncate DATA, tell(DATA);
close DATA;

print "the output demo file is $file\n";
