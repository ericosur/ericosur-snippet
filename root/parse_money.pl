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
use v5.10;
use Data::Dump qw(dump);
use DateTime;
use Date::Calc qw(:all);

my $deadline = 0;
# will auto alter it if it is past
my ($DEADYEAR, $DEADMONTH, $DEADDAY) = (2016, 10, 3);
my %hash = ();
my %hash_to_sort = ();

sub get_today()
{
    # get date of today
    my (undef,undef,undef,$day,$month,$year,undef,undef,undef) = localtime;
    $year += 1900;
    $month += 1;

    $DEADYEAR = $year;
    $DEADMONTH = $month;
}

sub parse_file($)
{
    my $file = shift;
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
                my @dup = show_one_record(\@data);
                addToHash(\@dup);
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
        my @dup = show_one_record(\@data);
        addToHash(\@dup);
        $dirty = 0;
        dump(@data) if $debug;
        print "\n" if $debug;
        @data = ();
    }

    close $fh;
    print STDERR "cnt: $cnt\n" if $debug;
}

sub addToHash($)
{
    my $rf = shift;
    my @dt = @$rf;

    if ($dt[0] ne "") {
        $hash{$dt[0]} = $rf;
        $hash_to_sort{$dt[0]} = $rf->[6];
    }
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

# in: (year, month, day)
sub get_date_delta($$$)
{
    my ($dy,$dm,$dd) = @_;
    my ($ty, $tm, $tday) = Today();

    #printf("%04d/%02d/%02d\n", $dy, $dm, $dd);
    my $delta = Delta_Days($ty, $tm, $tday, $dy, $dm, $dd);

    #print $delta,"\n";
    return $delta;
}

sub show_one_record($)
{
    my $rf = shift;
    my @dt = @$rf;
    my @dup = ();

    my $expd = $dt[2];
    my $dist = -1;
    my $distdead = -1;
    if ( $expd =~ m/(\d+)\/(\d+)\/(\d+)/ ) {
        $distdead = getDaysTillDead($1, $2, $3);
        $dist = getDaysTillToday($1,$2,$3);
        #print "$1-$2-$3\n";
        push @dup, @dt;
        push @dup, $distdead;
        push @dup, $dist;
        push @dup, ($distdead<0)?"ok":"n/a";
    }

    if ($dt[0] eq "") {
        #print STDERR "no account id, skip\n";
        return;
    }
=pod
    my $output = sprintf("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%d\"\n",
        $dt[0], $dt[1], $dt[2], $dt[3], $dt[4], $dist);
    my $output = sprintf("\"%s\",\"%s\",\"%s\",\"%s\",\"%d\",\"%d\",\"%s\"\n",
        $dt[0], $dt[2], $dt[3], $dt[4], $distdead, $dist,
        ($distdead<0)?"ok":"" );
    print $output;
=cut
    return @dup;
}

sub show_one_array(@)
{
    my $rf = shift;
    my @dt = @$rf;
    my $output = sprintf("\"%s\",\"%s\",\"%s\",\"%s\",\"%d\",\"%d\",\"%s\"\n",
        $dt[0], $dt[2], $dt[3], $dt[4], $dt[5], $dt[6], $dt[7]);
    print $output;

}

sub show_deadline()
{
    #$deadline = getdays(2016, 1, 1);
    #print "days to deadline: $deadline\n";

    $deadline = getDaysTillToday($DEADYEAR, $DEADMONTH, $DEADDAY);
    my $str_deadline = sprintf("%04d/%02d/%02d", $DEADYEAR, $DEADMONTH, $DEADDAY);
    print STDERR "next deadline date: ", $str_deadline, "\n";
    print STDERR "days to deadline: ", $deadline, "\n";
}

sub main()
{
    my $delta = 0;
    get_today();
    # go forward one month if deadline date is overdue
    do {
        if ($delta <= 0) {
            $DEADMONTH += 1;
            if ($DEADMONTH > 12) {
                $DEADYEAR += 1;
                $DEADMONTH -= 12;
            }
        }
        $delta = get_date_delta($DEADYEAR, $DEADMONTH, $DEADDAY);
        #printf("delta: %d\n", $delta);
    } while ($delta < 0);

    show_deadline();
    my $fn;
    if ($ARGV[0]) {
        $fn = $ARGV[0];
    } else {
        $fn = "money.txt";
    }
    parse_file($fn);

    # sort records by distance from today
    foreach my $no (sort { $hash_to_sort{$a} <=> $hash_to_sort{$b} or $a cmp $b } keys %hash_to_sort) {
        show_one_array($hash{$no});
    }
}

main;
