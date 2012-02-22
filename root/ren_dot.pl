#!/usr/bin/perl
#
# replace extra dot in file name to space
#

use strict;
use warnings;

use File::Basename;
use lib 'd:/ericosur-google';
use Ericosur;

sub main()
{
	my $input_fname = $ARGV[0] or die "please specify a filename to rename";
	do_rename($input_fname);
}

sub from_list()
{
	my $file = "list.txt";
	my $fh;
	my $cnt;

	open $fh, $file or die "cannot open $file: $!\n";
	while ( <$fh> )  {
		$cnt = 0;
		s/\n//;
		my $input_name = $_;
		++$cnt while (m/\./g);

		if ($cnt > 1)  {	# only one dot
			print "($cnt): <$input_name>\n";
			do_rename($input_name);
		}
	}

	close $fh;

}

sub do_rename()
{
	my $path = shift;

	# add more if more file types need to process
	my @exts = qw(.chm .pdf .txt .zip .rar .ace .cue .flac .ape);

	my $old_fname = $path;	# old complete file name
	my $new_fname;

	# the composition of this filename
	my ($file, $dir, $ext) = fileparse($path, @exts);

	$file =~ s/[\._]/ /g;

	$new_fname = sprintf "%s%s%s", $dir, $file, $ext;
	sep();
	#show("old", $old_fname);
	show("new", $new_fname);

	if ($old_fname eq $new_fname)  {
		print "not rename\n";
	}
	else  {
		rename $old_fname, $new_fname;
		print "renamed\n";
	}
}


#
# main procedure here
#
if (@ARGV)  {
	main();
}
else  {
	from_list();
}
