#!/usr/bin/perl
# read out the data of cooks
# -- Jul 3 1998 by Eric
# init version
# -- Jul 14 1998 by Eric
# use strict
# improve efficiency

use strict;
use Benchmark;
use vars qw( $name $power $pa $love $bear $study $quality $tech
    $tenacity $tj $fj );

sub mypause {
    print "press any key to continue...";
    <STDIN>;
}

sub myblock($$) {
    my $tmp = shift @_;
    my $lne = shift @_;
    if ( $lne eq $tmp ) {
        COMMENT: while (<COOK>) {   # <COOK> is external var.
            chop($lne = $_);
          last COMMENT if $lne eq "[end]";
            print "$lne\n";
        }
        mypause;
    }
}

#extract value from ``*keyname "name"''
sub get_str($$) {    # arg: line, keyname
    my $lne = shift @_;
    my $key = shift @_;
    return ($lne =~ /\*$key\s+\"(.*)\"/) ? $1 : "";
}

sub get_val($$) {    #arg: line, valname
    my $lne = shift @_;
    my $key = shift @_;
    # match: *key 2934 ;
    return ($lne =~ /\*$key\s+(\d+)/) ? $1 : -1;
}

my $output = "out.csv";
if (-e $output) {
    unlink $output or die "cannot unlink $output\n";
}
open(OUTCSV, ">$output");

my $dir = "d:\\bistro\\info\\person\\cook";
chdir $dir or die "cannot chdir to $dir\n";

my $i;
foreach $i (1..20) {
    my $file = "cook" . sprintf("%02d", $i) . ".psn";
    open(COOK, $file) or die "cannot open!\n";

  READLINE: while (<COOK>) {
        my $line;
        my $tmp;

#        next READLINE if /^;/;  # skip comment line begin with ``;''
#        next READLINE if /^$/;  # skip blank line
# note: because I only take var setting like ``*power 30''
# if wanna take the other things, DO NOT use this line!
        next READLINE unless /^\*/;  # proceed only start with ``*''

        chop($line = $_);

# there is no 'switch' in Perl, so I use such get-it-and-continue method
        ($name = $tmp, next READLINE) if $tmp = get_str($line, "name");
        ($power = $tmp, next READLINE) if ($tmp = get_val($line, "power")) != -1;
        ($pa = $tmp, next READLINE) if ($tmp = get_val($line, "pa")) != -1;
        ($love = $tmp, next READLINE) if ($tmp = get_val($line, "love")) != -1;
        ($bear = $tmp, next READLINE) if ($tmp = get_val($line, "bear")) != -1;
        ($study = $tmp, next READLINE) if ($tmp = get_val($line, "study")) != -1;
        ($quality = $tmp, next READLINE) if ($tmp = get_val($line, "quality")) != -1;
        ($tech = $tmp, next READLINE) if ($tmp = get_val($line, "tech")) != -1;
        ($tenacity = $tmp, next READLINE) if ($tmp = get_val($line, "tenacity")) != -1;
        ($tj = $tmp, next READLINE) if ($tmp = get_str($line, "tj"));
        ($fj = $tmp, next READLINE) if ($tmp = get_str($line, "fj"));

#        myblock("[comment]", $line);
#        myblock("[setting]", $line);

    }   # READLINE: while (<COOK>) {
    close(COOK);

    my $output_line = "$name,$power,$pa,$love,$bear,$study,$quality," .
        "$tech,$tenacity,$tj,$fj\n";
    print STDOUT $output_line;
    print OUTCSV $output_line;

}  # foreach...

