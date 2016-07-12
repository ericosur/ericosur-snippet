#!/usr/bin/env perl
#
# money spreadsheet from chinatrust bank
# how to use:
# browse bank webpage
# copy the text of table content
# paste it into "money.txt"
# add "#" to comment out title description
#
# the line with "ok" means this money account
# could be used before deadline date
#
# remember, it calculate distance of two dates
# so, dist = abs(d1 - d2);
#
# perl parse_money.pl 1> a.csv 2> /dev/null

use strict;
use Data::Dump qw(dump);
use DateTime;
use Date::Calc qw(:all);

my $deadline = 0;
my ($DEADYEAR, $DEADMONTH, $DEADDAY) = (2016, 7, 3);

sub process() {
    my $file = 'money.txt';
    my $debug = 0;
    my $verbose = 0;
    my $cnt = 0;
    my $dirty = 0;
    my @data = ();

    show_csvtitle();
    open my $fh, $file or die;
    while (<$fh>) {
        if (m/^#/) {
            next;
        }
        if (m/^\s+(\d+)/) {
            # account id fetched
            if ($dirty) {
                # output it and clean dirty flag
                show_verbose(\@data) if $verbose;
                show(\@data);
                $dirty = 0;
                dump(@data) if $debug;
                print "\n" if $debug;
                @data = ();
                $cnt ++;
            }
            push @data, $1; # 定存帳號
        } elsif ( m/--\s+([0-9\/]+)/ ) {
            push @data, $1; # 開戶日
        } elsif ( m/^([0-9\/]+)\s+(\d+月)$/) {
            push @data, $1; # 到期日
            my $mon = $2;
            $mon =~ s/月/mo/;
            push @data, $mon; # 週期
        } elsif ( m/^([0-9,\.]+)\s+到期/ ) {
            push @data, $1; # 金額
        } elsif ( m/續存/ ) {
            if ($debug) {
                print "get last line of one record";
            }
            $dirty = 1; # the last line of one record
        }
        print STDERR $_ if $debug;
    }

    # the last record...
    if ($dirty) {
        # output it and clean dirty flag
        show_verbose(\@data) if $verbose;
        show(\@data);
        $dirty = 0;
        dump(@data) if $debug;
        print "\n" if $debug;
        @data = ();
    }

    close $fh;
    print STDERR "cnt: $cnt\n" if $debug;
}

sub show_csvtitle()
{
    if ( $^O eq 'MSWin32' ) {
        printf("\"account id\",\"expired date\",\"cycle\",\"amount\",\"due day\",\"due today\",\"available\"\n");
    } else {
        printf("\"定存帳號\",\"到期日\",\"週期\",\"金額\",\"距離到期日\",\"距離今日\",\"可用\"\n");
    }
}

sub show_verbose($)
{
#    print "show_verbose\n";
    my $rf = shift;
    my @dt = @$rf;
    printf("定存帳號：%s\n開戶日：%s\t到期日：%s\n",
        $dt[0], $dt[1], $dt[2]);
    printf("週期：%s\t金額：%s\n",
        $dt[3], $dt[4]);
    print '-' x 40, "\n";
}

# yy, mm, dd
sub getDaysTillDead($$$)
{
    my ($yy, $mm, $dd) = @_;
    my $dt_dead = DateTime->new(
            year => $DEADYEAR,
            month => $DEADMONTH,
            day => $DEADDAY);
    my $dt_exp = DateTime->new(
            year => $yy,
            month => $mm,
            day => $dd);
    my $days = $dt_dead->delta_days($dt_exp)->delta_days;
    #print STDERR "getdays: target date: ", $dte, "\n";

    if ($dt_exp > $dt_dead) {
        #print STDERR "overdue\n";
        return $days;
    } else {
        return -$days;
    }
    #return $days;
}

# yy, mm, dd
sub getDaysTillToday($$$)
{
    my ($yy, $mm, $dd) = @_;
    my $dt = DateTime->now;
    my $dte = DateTime->new(
            year => $yy,
            month => $mm,
            day => $dd);
    my $days = $dt->delta_days($dte)->delta_days;
    #print STDERR "getdays: target date: ", $dte, "\n";
    return $days;
}

sub show($)
{
    my $rf = shift;
    my @dt = @$rf;

    my $expd = $dt[2];
    my $dist = -1;
    my $distdead = -1;
    if ( $expd =~ m/(\d+)\/(\d+)\/(\d+)/ ) {
        $distdead = getDaysTillDead($1, $2, $3);
        $dist = getDaysTillToday($1,$2,$3);
        #print "$1-$2-$3\n";
    }

    if ($dt[0] eq "") {
        #print STDERR "no account id, skip\n";
        return;
    }
#    my $output = sprintf("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%d\"\n",
#        $dt[0], $dt[1], $dt[2], $dt[3], $dt[4], $dist);
    my $output = sprintf("\"%s\",\"%s\",\"%s\",\"%s\",\"%d\",\"%d\",\"%s\"\n",
        $dt[0], $dt[2], $dt[3], $dt[4], $distdead, $dist,
        ($distdead<0)?"ok":"" );
    print $output;
}

sub show_deadline()
{
    #$deadline = getdays(2016, 1, 1);
    #print "days to deadline: $deadline\n";

    $deadline = getDaysTillToday($DEADYEAR, $DEADMONTH, $DEADDAY);
    my $str = sprintf("todays to deadline(%04d/%02d/%02d): %d\n",
        $DEADYEAR, $DEADMONTH, $DEADDAY, $deadline);
    print STDERR $str;
}

sub main()
{
    show_deadline();
    process();
}

main;
