#/usr/bin/perl

#
# 列出 \\10.1.211.150\Project(1|2|3) 下面的檔案至 out\d\d\d\d.txt
# 在使用前需要先回答該 server 的密碼
#
# 2006/12/27 by ericosur

use strict;

# get time to compose the
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime;
my $date = sprintf "%02d%02d", $mon + 1, $mday;
#print "$date\n";

my $base_path = "\\\\10.1.211.150\\Project";
my $output_file = "out$date.txt";

print "result output to $output_file\n";

foreach my $idx (1 .. 3)
{
	my $target = $base_path . $idx;
	print "$target\n";

	my $issue = "dir \/s\/b\/a-d $target >> $output_file";
	system $issue;
}

# prepare tmp file name
my $tmp_file = $output_file . ".tmp";
open FH, $output_file or die "cannot open $output_file: $!\n";
open OH, "> $tmp_file" or die "write error $!\n";

# strip the $base_path of every line
while ( <FH> )
{
	s(\\\\10\.1\.211\.150\\Project\d)()i;
	print OH $_;
}

close FH;
close OH;

# delete the original file and rename temp file
unlink $output_file;
rename $tmp_file, $output_file;
