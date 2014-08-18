#!/usr/bin/perl

# strip mail header from saved E-mail message

use strict;

opendir THISDIR, "." or die "cannot open dir\n";
my @dir_entry = grep /\.txt$/, readdir THISDIR;
closedir THISDIR;

foreach (@dir_entry) {
    my $b_body = 0;
    my $in_file = $_;
    my $out_file = $_ . '.tmp';
    my @output_content = ();

    open FILEIN, $in_file or die "cannot read $in_file\n";
    open FILEOUT, "> $out_file" or die "cannot write $out_file\n";

  LINE:
    while ( <FILEIN> ) {
        $b_body = 1 if ($b_body == 0 and /^§@ªÌ/);
        next LINE if $b_body == 0;
        push @output_content, $_;
    }   # while (...)
    $b_body = 0;
    close FILEIN;
    # strip the tail lines
    my $i;
    for ($i=0; $i<2; $i++) {
        pop @output_content;
    }
    print FILEOUT @output_content;
    close FILEOUT;
    rename $in_file, "$in_file.bak" or warn "cannot rename to bak\n";
    rename $out_file, $in_file or warn "cannot rename to org\n";
}   # foreach (...)
