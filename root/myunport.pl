#!/usr/bin/env perl

use strict;

sub help()
{
  print<<EOL;

  myunport.pl - uninstall deactivated port packages

  \$ port installed > list.txt
  \$ perl myun.pl

EOL
}

sub main()
{
  my $fn = 'list.txt';
  if (not -e $fn) {
    $fn = 'tmp-list.txt';
    system("port installed > $fn");
  }
  open my $fh, $fn or help();

  while (<$fh>) {
    if ( m/^\s/) {
      s/^\s+//;
      if ( /\(active\)/ ) {
        next;
      }
      s/[\r\n]//;
      my $pn = $_;
      my $cmd = sprintf("sudo port uninstall %s", $pn);
      print $cmd,"\n";
      system($cmd);
    }
  }

  close($fh);
  unlink($fn);
}

main;
