#!/usr/bin/perl

use strict;
use v5.10;

sub list_unit($)
{
    my $f = shift;
    my $level = 0;
    my $line_no = 0;
    my $line_text;
    my $tag;
    my $flag = -1;
    my %val;
    my $unit_count = 0;

    open my $fh, $f or die;
    while (<$fh>) {
        ++ $line_no;
        s/[\r\n\s]//g;
        $line_text = $_;

        if ( m/\[(\w+)\]/ ) {
            $level ++;
                if ($1 eq "unit") {
                $flag = $level;
                %val = ();
                print "$line_no ($level): $line_text\n";
            }
        } elsif ( m/\[\/(\w+)\]/ ) {
            $level --;
            if ($1 eq "unit") {
                $flag = -1;
                dump_value(\%val);
                print "$line_no ($level): $line_text\n";
                %val = ();
                $unit_count ++;
                next;
            }
        }

        if ($flag == $level) {
            #say "# $line_text";
            my $ret = get_value($line_text, $line_no, \%val);
            if ($ret) {
                #print "$line_no: match $ret\n";
            }
        }
    }
    close $fh;

    say "total unit count: $unit_count";
}

sub dump_value($) {
    my $rr = shift;
    for my $kk (keys(%$rr)) {
        say "\t$kk -> $rr->{$kk}";
    }
}

sub get_value($$$) {
    my $text = shift;
    my $lineno = shift;
    my $rr = shift;
    my $found = "";
    my @token = ("name", "type", "experience",
        "hitpoints", "max_experience", "max_hitpoints");

    #print "gv: [$ln] => ";
    foreach my $tt (@token) {
        #my $pat = qr($tt);
        if ($text =~ m/^$tt=(.*)/) {
            $found = $tt;
            $rr->{$lineno} = $text;
            #say "match: $tt => $1";
            last;
        }
    }
    return $found;
}

sub main()
{
    my $file = $ARGV[0] // "a2b";
    list_unit($file);
}

main;
