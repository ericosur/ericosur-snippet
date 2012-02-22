#!/usr/bin/perl

# process ``c:\scandisk.log'' reported by SCANDSKW.exe
# it will remove un-necessary block if no error report...
# -- Aug 10 1998 by Eric
# init version
use strict;

print STDERR "Remove unnecessary records in SCANDISK.LOG" .
    " Aug 10 1998 by Eric\n";
my $log_full_path = "c:\\scandisk.log";
my $block_begin = '\*\*\*\*\*';     # more...
my $block_end = "-----";       # more...

die "no log file to process\n" unless (-e $log_full_path);
open LOGFILE, $log_full_path or die "cannot open: $!\n";

my @block;
my @tmp;
my $b_block_need = 1;
LOOP:
  while( <LOGFILE> ) {
    next LOOP if /^\n$/;        # skip blank line
    $b_block_need = 1 if /$block_begin/;
    
    if ( $b_block_need and /$block_end/ ) {
        push @block, @tmp;
        print STDERR " 發生錯誤!保留此記錄\n";
    }
    if ( m[\b(\d+:\d+)\b.*\b(\d+/\d+/\d+)] ) {
        print STDERR "Time taking scandisk at $2 $1:" 
    }
    if ( /找不到任何錯誤/ ) {
        print STDERR " 沒有錯誤!\n";
        $b_block_need = 0;
    }

#    print $_;
    push @tmp, $_;
  }

close(LOGFILE);

unlink $log_full_path;
if (scalar @block == 0) {
    print STDERR "No records remain!\n";
}
else {
    open LOGTOFILE, ">$log_full_path" or die "cannot write log $!\n";
    print LOGTOFILE @block;
    close LOGTOFILE;
}
