#!/usr/bin/perl

# split boshimay_radicals.txt into
# different category files cat[000-099].txt
# seperated by "^## ..."

use strict;

my $file = 'boshiamy_radicals.txt';
my $ccnt = 1;
my @arr;

open my $fh, $file or die;
while (<$fh>) {
    if ( /^##/ ) {
        #print $ccnt, "\n";
        push @arr, $ccnt;
        #print $_;
    }
    $ccnt ++;
}
close $fh;
#print '=' x 40, "\n";

my $start = 0;
my $end = 0;
my @ranges;
my $fcnt = 0;
LOOP:
foreach my $i (@arr) {
    if ($start eq 0) {
        $start = $i;
        next LOOP;
    } else {
        if ($end eq 0) {
            $end = $i - 1;
        } else {
            # do nothing
        }
    }
    #printf("%d to %d\n", $start, $end);
    my @rr = [$start, $end];
    push @ranges, @rr;
    my $ofile = sprintf("cat%03d.txt", $fcnt);
    my $cmd = sprintf("sed -n %d,%dp %s > %s", $start, $end, $file, $ofile);
    printf("%s\n", $cmd);
    system($cmd);
    $fcnt ++;
    $start = $end + 1;
    $end = 0;
}

# foreach my $h (@ranges) {
#     my @a = @$h;
#     printf("%d to %d\n", $a[0], $a[1]);
# }
#