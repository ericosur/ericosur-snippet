#!/usr/bin/env perl -w

# from http://gist.github.com/130012

use strict;
use v5.10;
use Net::Twitter;
use DateTimeX::Easy;
use YAML;

my $username = $ARGV[0] || die "Give me an twitter username\n";

sub timecard_image_url {
    my @times = @_;
    my @x;
    my @y;
    my @z;
    my $xy = {};

    for my $dt (@times) {
        $xy->{ $dt->hour }{ $dt->wday - 1 }++;
    }

    for my $day (0..6) {
        for my $hour (0..23) {
            my $size = $xy->{$hour}{$day} || 0;
            push @x, $hour;
            push @y, $day;
            push @z, $size;
        }
    }

    local $" = ",";
    return "http://chart.apis.google.com/chart?cht=s&chs=900x300&chxt=x,y&chxl=0:||0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23||1:||Sun|Mon|Tue|Wed|Thu|Fri|Sat|&chm=o,333333,1,1.0,25,0&chds=-1,24,-1,7,0,20&chd=t:@x|@y|@z";
}

my $twit = Net::Twitter->new();

my @status_times =
    map { DateTimeX::Easy->parse($_->{created_at}) }
    map { @{ $twit->user_timeline({ id => $username, page => $_, count => 200 }) or die YAML::Dump($twit->get_error) } } 1..2;

say timecard_image_url(@status_times);
say "Time card generated with " . @status_times . " tweets";
 