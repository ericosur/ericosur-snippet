#!/usr/bin/perl

use strict;

# settings
my $prj_dir = 'c:\\projects';   # no trailing '#' needed
my $tmp_dir = 'c:\\temp\\';     # trailing '#' needed
my $all_list = 'prjlist.$$$';
my $to_comp_list = 'complist.$$$';
my $no_comp_list = 'nocomp.$$$';
my $version = 'v0.1 Aug 6 1998 by Eric';

print "Perl script using RAR to backup $prj_dir $version\n";

chdir $prj_dir or die "chdir to $prj_dir failed\n";
system "dir /s/b/a-d *.* >$tmp_dir$all_list";
system "dir /s/b *.arj > $tmp_dir$no_comp_list";
system "dir /s/b *.zip >>$tmp_dir$no_comp_list";

open(FILE, "<$tmp_dir$all_list") or die "cannot open $all_list: $!\n";
open(OUTFILE, ">$tmp_dir$to_comp_list") or die "cannot output $to_comp_list: $!\n";
my $cnt = 0;

# make a list of files which need to compress
print "$0: process file list...\n";
LOOP:
while ( <FILE> ) {
    $cnt ++;
    next LOOP if /^\s/;
    next LOOP if /\.arj$/i;
    next LOOP if /\.zip$/i;
    print OUTFILE $_;
}   # while (...)
close(OUTFILE);

# compressor settings
my $rarpath = 'c:\\progra~1\\winrar\\';     # trailing '#' is needed
my $rarbin = 'winrar95.exe';
my $action = 'a -tl -rr -ri12 -mdE -m4 -s';
my $arc_path = 'c:\\temp\\';                # trailing '#' is needed

die "cannot find $rarpath$rarbin\n" unless -e $rarpath . $rarbin;
# compress plain files...
my $arc_file = $arc_path . 'test.rar';
my $cmd = "$rarpath$rarbin $action $arc_file \@$tmp_dir$to_comp_list";
print "$cmd\n";
system $cmd;

# just storing the archive files (*.arj *.zip)
# -m0 (storing) will override -m4 (best compression)
$cmd = "$rarpath$rarbin $action -m0 $arc_file \@$tmp_dir$no_comp_list";
print "$cmd\n";
system $cmd;

print "\n$0: delete temp files\n";
my $i;
foreach $i ($all_list, $to_comp_list, $no_comp_list) {
    unlink "$tmp_dir$i" if -e "$tmp_dir$i";
}

print "$0: total files processed: $cnt\n";
