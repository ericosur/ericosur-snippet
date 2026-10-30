#!/usr/bin/perl

# strip mail header from saved E-mail message

use strict;
use utf8;

opendir THISDIR, "." or die "cannot open dir\n";
my @dir_entry = grep /\.txt$/, readdir THISDIR;
closedir THISDIR;

foreach (@dir_entry) {
    my $b_body = 0;
    my $in_file = $_;
    my $out_file = $_ . '.tmp';
    die "$in_file.bak already exists\n" if -e "$in_file.bak";
    my @output_content = ();

    open FILEIN, '<:encoding(big5)', $in_file or die "cannot read $in_file\n";
    open FILEOUT, '>:encoding(big5)', $out_file or die "cannot write $out_file\n";

  LINE:
    while ( <FILEIN> ) {
        $b_body = 1 if ($b_body == 0 and /^作者/);
        next LINE if $b_body == 0;
        push @output_content, $_;
    }   # while (...)
    $b_body = 0;
    close FILEIN;
    # strip the tail lines
    splice @output_content, -2 if @output_content >= 2;
    print FILEOUT @output_content;
    close FILEOUT;
    rename $in_file, "$in_file.bak" or die "cannot rename to bak\n";
    rename $out_file, $in_file or die "cannot rename to org\n";
}   # foreach (...)
