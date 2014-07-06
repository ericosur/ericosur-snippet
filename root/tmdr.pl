#!/usr/bin/perl

# simple time duration calculation
# tmdr.pl <time1> <time2>
# in the format of HH.mmss
#

use strict;

sub check_val($)
{
    my $val = shift;
    my @v = ();

    if ($val =~ m/(\d+)\.(\d\d)(\d\d(\d\d\d)?)/) {
        $v[0] = $1;
        $v[1] = $2;
        #warn "exceed range" if $v[1] > 59;
        $v[2] = $3;
        if ($v[2] >= 1000) {
            $v[2] = $v[2] / 1000;
        }

    }
    #print ">> @v <<\n";
    return @v;
}

sub show_val($)
{
    my $rr = shift;
    my @vv = @$rr;
    #print ">> @vv <<\n";
    printf "%d:%02d:%02.3f\n", $vv[0], $vv[1], $vv[2];
}

sub add_val($$)
{
    my ($r1, $r2) = @_;
    my @res = (0, 0, 0);
    my $carr = 0;

    # ss part
    $res[2] = $r1->[2] + $r2->[2];
    while ($res[2] >= 60) {
        $res[2] -= 60;
        $carr ++;
    }

    # mm part
    $res[1] = $r1->[1] + $r2->[1] + $carr;
    $carr = 0;
    while ($res[1] >= 60) {
        $res[1] -= 60;
        $carr ++;
    }

    # hh part
    $res[0] = $r1->[0] + $r2->[0] + $carr;

    return @res;
}

sub sub_val($$)
{
    my ($r1, $r2) = @_;
    my @res = (0, 0, 0);
    my $carr = 0;

    # ss part
    $res[2] = $r1->[2] - $r2->[2];
    while ($res[2] < 0) {
        $res[2] += 60;
        $carr --;
    }

    # mm part
    $res[1] = $r1->[1] - $r2->[1] + $carr;
    $carr = 0;
    while ($res[1] < 0) {
        $res[1] += 60;
        $carr --;
    }

    # hh part
    $res[0] = $r1->[0] - $r2->[0] + $carr;

    return @res;
}

sub addv($$)
{
    my ($m, $n) = @_;
    my @mm = check_val($m);
    my @nn = check_val($n);
    my @rr = add_val(\@mm, \@nn);
    my $res = sprintf("%d:%02d:%02.3f", $rr[0], $rr[1], $rr[2]);
    return $res;
}

# will make sure $m > $n
sub subv($$)
{
    my ($m, $n) = @_;
    my $swapped = 0;
    if ($m < $n) {
        ($m, $n) = ($n, $m);
        $swapped = 1;
    }
    my @mm = check_val($m);
    my @nn = check_val($n);

    #print "mm:",@mm,"\n";
    #print "nn:",@nn,"\n";
    my @rr = sub_val(\@mm, \@nn);
    my $res = sprintf("%d:%02d:%02.3f", $rr[0], $rr[1], $rr[2]);
    if ($swapped) {
        $res = '-' . $res;
    }
    return $res;
}

sub fmt($)
{
    my $v = shift;
    my @rr = check_val($v);
    my $res = sprintf("%d:%02d:%02d", $rr[0], $rr[1], $rr[2]);
    return $res;
}

sub main()
{
    my $ts = $ARGV[0] // "0.5959";
    my $te = $ARGV[1] // "0.0001";
    my $res;

    $res = addv($ts, $te);
    printf("%s add %s => %s\n", fmt($ts), fmt($te), $res);
    $res = subv($ts, $te);
    printf("%s sub %s => %s\n", fmt($ts), fmt($te), $res);
}

main;
