#!/usr/bin/perl

=pod

=head1 DESCRIPTION
    draw geo sketch bitmaps

=head1 REFERENCE
    http://chinese.engadget.com/2009/08/12/geosketch/
    http://www.kongregate.com/games/Denial_Designs/geosketch

=cut

# how to run:
# perl geosketch.pl && display geosketch.png

use strict;
use warnings;

use Image::Magick;
use Config::JSON;

my $file = 'geosketch.json';
my $ofile = "geosketch.png";

my $pi = 3.14159265358979323846264338327950;

my $maxx;
my $maxy;
my $debug;
my @start = ();
my @a = ();     # current angle
my @v = ();     # angle velocity
my $dis;
my @c = ([0,0], [0,0], [0,0]);
my ($lx, $ly) = (0, 0);
my $repeat;

sub load_setting()
{
    my $cfg = Config::JSON->new($file);

    $maxx = $cfg->get("maxx") || 1000;
    $maxy = $cfg->get('maxy') || 800;
    $debug = $cfg->get('debug') || 0;
    $dis = $cfg->get('stick_len') || 80;
    $repeat = $cfg->get('repeat') || 1000;

    if (@ARGV)  {
        @v = @ARGV;
    }
    else {
        my $vref = $cfg->get("velocity");
        @v = @$vref;
    }

    my $sref = $cfg->get('start');
    @start = @$sref;

    my $aref = $cfg->get('start_angle');
    @a = @$aref;
}

# deg to rad
sub deg($)
{
    my $dd = shift;
    return ($dd * $pi) / 180;
}

sub update_coord()
{
    my ($xx, $yy) = (0, 0);
    for my $ii (0 .. 2)  {
        $a[$ii] += $v[$ii];
    }

    $c[0]->[0] = $start[0] + $dis * cos(deg($a[0]));
    $c[0]->[1] = $start[1] + $dis * sin(deg($a[0]));
    $c[1]->[0] = $c[0]->[0] + $dis * cos(deg($a[1]));
    $c[1]->[1] = $c[0]->[1] + $dis * sin(deg($a[1]));
    $c[2]->[0] = $c[1]->[0] + $dis * cos(deg($a[2]));
    $c[2]->[1] = $c[1]->[1] + $dis * sin(deg($a[2]));

    if ($debug)  {
        foreach my $z (@a)  {
            printf "(%d)\t", $z;
        }
        foreach my $v (@c)  {
            printf("(%d, %d)\t", $v->[0], $v->[1]);
        }
        print "\n";
    }
}

sub get_coord()
{
    if ($lx == 0 && $ly == 0)  {
        $lx = $c[2][0];
        $ly = $c[2][1];
    }
    my $cord = sprintf("%d,%d %d,%d", $lx, $ly, $c[2][0], $c[2][1]);
    print $cord,"\n" if $debug;
    $lx = $c[2][0];
    $ly = $c[2][1];
    return $cord;
}

sub get_random_coord()
{
    my $coordinate = sprintf("%d,%d %d,%d",
        int(rand($maxx*2/3)+40), int(rand($maxy*2/3)+40),
        int(rand($maxx*1/4)), int(rand($maxy*1/4)),
    );
    print $coordinate,"\n" if $debug;
    return $coordinate;
}

sub get_random_color()
{

    my $color = sprintf("#%02x%02x%02x",
        int(rand(255)), int(rand(255)), int(rand(255))
    );
    print "color = $color\n" if $debug;
}

sub draw($)
{
    my $im = Image::Magick->new(size => "$maxx x $maxy");
    my $rc;
    my $pix_name = shift;
    my $fill_color = '#EEEEEE';

    $rc = $im->Read('xc:black');
    warn $rc if $rc;

    for (1 .. $repeat)  {

        update_coord();
        $im->Draw(primitive => 'line',
              #points   => '0,129',
              points => get_coord(),
              fill      => $fill_color,
              strokewidth => 1,
              stroke    => $fill_color);
    }

    $im->Write($pix_name);
}

sub main()
{
    load_setting();
    draw($ofile);
    print "output to $ofile\n";
}

main;
