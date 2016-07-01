#!/usr/bin/env perl

# http://programmingpraxis.com/2014/12/19/diana-cryptosystem/
# http://home.earthlink.net/~specforces/spdiana.htm

use strict;
#use Data::Dump qw(dump);

my $a2z = q(ABCDEFGHIJKLMNOPQRSTUVWXYZ);
my $z2a = scalar reverse $a2z;
my $Z2A = $z2a;

#print $a2z,"\n";
#print $z2a,"\n";

sub shiftbyone($)
{
    my $str = shift;
    my $head = substr($str, 0, 1);
    my $tail = substr($str, 1, 25);
    #printf("h:%s, t:%s\n", $head, $tail);
    my $res = $tail . $head;
    #print "res: $res\n";
    return $res;
}

sub print_table()
{
    for my $cc (split(//, $a2z)) {
        print $cc, ": ", $a2z, "\n";
        print " : ", $z2a, "\n";
        print "\n";
        $z2a = shiftbyone($z2a);
    }
}

sub showotp($)
{
    my $res = shift;
    $res = uc($res);
    $res =~ s/ //g;
    print $res;
}


sub space_every5($)
{
    my $str = shift;
    my $i=0;
    my $j=0;
    for my $cc (split(//,$str)) {
        $i ++;
        print $cc;
        if ($i%5==0) {
            print " ";
            $j++;
        }
        if ($j!=0&&$j%5==0) {
            print "\n";
            $j=0;
        }
    }
    print "\n";
}

sub main()
{
    print_table();
}

main;
