#
# split plutommi/mmi/TargetOption.txt
# to one line for one define
# for viewing / comparing more conveniently
#

use strict;

# take the first line argument or file at current directory
my $file = $ARGV[0] || "TargetOption.txt";
open my $fh, $file or die;
my $fuck = <$fh>;

while ( $fuck =~ m/(\/D \"\w+\")/g )  {
	print $1,"\n";
}

close $fh;
