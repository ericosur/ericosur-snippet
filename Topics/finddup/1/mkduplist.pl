#!/usr/bin/perl

#@
#@ mymd5.pl
#@
#@ July 17 2002 by ericosur
#@ test on Digest::MD5
#@
#
#  fix the bug without using binary mode

use strict;
use Digest::MD5;

# my $md5;
# my $file = $ARGV[0] || $0;

my $outfile = "filedata.ph";
my $filelist = "filelist.txt";

open OFH, "> $outfile" or die;
open FLH, "< $filelist" or die;


print OFH '@files = (';
print OFH "\n";

my $count = 0;

while (<FLH>)
{
	my $line;
	my $file;

	s/\r//;
	s/\n//;

	$file = $_;

	die "cannot open $!\n" unless (-e $file);
	$line  = make_checksum($file);
	print OFH $line;
	print "$count...\n" if ++$count % 20 == 0;
}


print OFH ");\n1;";

close OFH;
close FLH;

print "total line: $count\n";
print "output file: $outfile\n";


sub make_checksum()
{
	my $md5;
	my $file = shift;

#	die "cannot open $!\n" unless (-e $file);
	# print "check file <$file>\n";

	# md5 hash

	open FH, $file;
	binmode(FH);
	$md5 = Digest::MD5->new->addfile(*FH)->hexdigest;
	close FH;

	$file =~ s/\'/\\\'/g;

	my $ret = sprintf "{'file' => '%s', 'hash' => '%s'},\n", $file, $md5;
	return $ret;

#	print "$file:\t$md5\n";
}
