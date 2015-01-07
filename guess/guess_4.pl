#!/usr/bin/perl

# ?A?B list
# sort hash by value

use strict;
use warnings;

my @total = ();

# from 0000 to 9999
sub list_all
{
    my $str;
    for (0..9999)  {
        $str = sprintf "%04d", $_;
        if (is_duplicate($str))  {  # no duplicated number
            next;
        }
#       if (is_lead_zero($str))  {  # no start with 0
#           next;
#       }
        #print $str,"\n";
        push @total, $str;
    }
}

sub is_duplicate($)
{
    my $value = shift;

    if (length($value) ne 4)  {
        #die "length is not 4";
        return 1;
    }

    my %dup = ();
    for (split //, $value)  {
        $dup{$_} ++;
        #print "$_\t";
    }
    #print "\n";
    for (keys %dup)  {
        #print $_, ":", $dup{$_}, "\n";
        if ($dup{$_} > 1)  {
            return 1;
        }
    }
    return 0;
}

sub is_lead_zero
{
    my $value = shift;

    if ( $value =~ m/^0\d{3}/ )  {
        return 1;
    } else  {
        return 0;
    }
}

# [in] answer
# [in] guess
# [out] (aa, bb)
sub get_ab
{
    my ($ans, $guess) = @_;
    my ($a, $b) = (0, 0);

    for my $i (0..3)  {
        for my $j (0..3)  {
            my $mm = substr($guess, $i, 1);
            my $nn = substr($ans, $j, 1);
            if ($mm eq $nn)  {
                if ($i eq $j)  {
                    $a ++;
                }
                else  {
                    $b ++;
                }
            }
        }
    }
    my $result = sprintf "%dA%dB", $a, $b;
    return $result;
}

sub main()
{
    my %ags = ();
    my %bgs = ();
    my $ans;

    # 0 <= $ans <= 9999, and check if valid
    do {
        $ans = int(rand(10000));
    } until ( !is_duplicate($ans) );

    list_all();
    for my $tt (@total)  {
        # $res = "0A3B"...
        my $res = get_ab($ans, $tt);
        $ags{$res} ++;
        # if first used, put an empty array for it
        if ( ref($bgs{$res}) ne 'ARRAY' ) {
            $bgs{$res} = [];
        }
        # push( $bgs{'1A2B'}, '1234' )
        my $rr = $bgs{$res};
        push(@$rr, $tt);
    }

    # print out the result
    my $cnt = $#total + 1;
    my $sum = 0;
    printf("for answer: %s\n", $ans);
    print "total = ", $cnt,"\n";

    for my $k (sort {$ags{$a} <=> $ags{$b}} keys %ags)  {
        printf "%s: %s (%.2g%%)\n", $k, $ags{$k}, ($ags{$k}*100/$cnt);
        $sum += $ags{$k};
        if ($ags{$k} < 20) {
            my $rr = $bgs{ $k };
            foreach ( @$rr ) {
                print $_,", ";
            }
            print "\n";
        }
    }
    warn if $sum != $cnt;
}

main;
