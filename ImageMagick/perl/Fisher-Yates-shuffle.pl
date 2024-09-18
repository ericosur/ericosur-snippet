#!/usr/bin/perl
#
# demo of "Fisher-Yates shuffle
# reference from: http://en.wikipedia.org/wiki/Fisher-Yates_shuffle
#
# using Image::Magick to produce animated gif images to
# visualized the suffling
#

use strict;
use warnings;
use Image::Magick;

my $max_size = 12;
my $max_value = $max_size;
my $debug = 0;

# for output images
my $maxx = 480;
my $maxy = 320;
my $draw_count = 0;   # for draw_array()
my $anim_gif = 'anim.gif';  # the final result

sub gen_array_with_random_number()
{
    my @arr = ();
    my $var;

    for (1..$max_size)  {
        $var = int(rand(100));
        push @arr, $var;
    }
    return @arr;
}


sub fill_array()
{
    my @arr = ();

    for (1..$max_size)  {
        push @arr, $_;
    }
    return @arr;
}


sub shuffle(\@)
{
    my $aref = shift;
    my @arr = @$aref;

    if ($debug)  {
        print "before...\n";
        show_array(@arr);
    }

    my $n = scalar @arr;
    print "n = $n\n" if $debug;
    while ($n > 1)  {
        my $k = int(rand($n));
        $n --;
        if ($debug)  {
            printf "arr[%d], arr[%d] (%d,%d)\t", $n, $k, $arr[$n], $arr[$k];
        }
        ($arr[$n], $arr[$k]) = ($arr[$k], $arr[$n]);
    }

    if ($debug)  {
        print "\nafter...\n";
        show_array(@arr);
    }
}


sub shuffle_ref(\@)
{
    my $aref = shift;

    if ($debug)  {
        print "before...\n";
        show_array(@$aref);
    }
    my $n = scalar @$aref;

    print "n = $n\n" if $debug;

    my $cnt = 0;
    while ($n > 1)  {
        my $k = int(rand($n));
        $n --;
        if ($debug)  {
            printf "arr[%d], arr[%d] (%d,%d)\t", $n, $k, $$aref[$n], $$aref[$k];
        }
        ($$aref[$n], $$aref[$k]) = ($$aref[$k], $$aref[$n]);

        if ($debug) {
            printf "%d(%d,%d) => ", ++$cnt, $n, $k;
        }

        draw_array($aref, $n, $k);   #show_array(@$aref);
    }
    if ($debug)  {
        print "\nafter...\n";
        show_array(@$aref);
    }
}


sub show_array(@)
{
    foreach (@_)  {
        printf "%02d ", $_;
    }
    print "\n";
}


sub get_coord($$)
{
    my ($idx, $val) = @_;
    my $x_padding = 10;
    my $x_space = ($maxx - 2*$x_padding) / $max_size;
    my $y_padding = 10;
    my $y_space = ($maxy - 2*$y_padding) / $max_value;
    my ($x1, $y1, $x2, $y2);

#    print "get_coord(): $idx, $val\n";

    $x1 = $x_padding + $idx * $x_space;
    $y1 = $maxy - $y_padding;
    $x2 = $x1 + $x_space -1 ;
    $y2 = $maxy - ($y_padding + $val * $y_space);

    return sprintf("%d,%d %d,%d", $x1, $y1, $x2, $y2);
}


sub draw_array(\@$$)
{
    my @val = @{ shift @_ };
    my ($fr, $to) = @_;
	my $im = Image::Magick->new(size => "$maxx x $maxy");
	my $rc;

	$rc = $im->Read('xc:black');
	warn $rc if $rc;

    my $array_size = $#val;
    if ($debug) {
#    print "array_size = ", $array_size,"\n";
        print "f($fr), t($to)\n";
    }

# yellow: from, red: to, green: not moved
    my $fill_color = 'black';
    for my $ii (0..$array_size)  {
        if ($fr == $to) {
            $fill_color = 'green' if ($ii == $fr);
        } else {
            $fill_color = 'yellow' if ($ii == $fr);
            $fill_color = 'red' if ($ii == $to);
        }
#        print "b4 draw: $ii, $val[$ii]\n";
        $im->Draw(primitive => 'rectangle',
    		  #points	=> '0,129 199,169',
    		  points => get_coord($ii, $val[$ii]),
    		  fill		=> $fill_color,
    		  strokewidth => 2,
    		  stroke	=> 'white');
        $fill_color = 'black';
    }

    my $pix_name = sprintf "arr%02d.gif", $draw_count;
    #print "output to $pix_name...\n";
    $im->Write($pix_name);
    $draw_count ++;
}


sub main()
{
    my @foo;

    for (1..1)
    {
        #@foo = gen_array_with_random_number();
        @foo = fill_array();

        draw_array(@foo,-1,-1);
        #show_array(@foo);

        shuffle_ref(@foo);
        draw_array(@foo,-1,-1);

        #print "#$_: ";
        #show_array(@foo);
    }

    # call convert of ImageMagick to produce animated gif
    my $cmd = "convert -delay 150 arr??.gif $anim_gif";
    if ($^O eq "MSWin32")  {
    	$cmd = "cmd /c " . $cmd;
    }
    print "cmd: $cmd\n" if $debug;
    system $cmd;

    print "the result animation gif: ", $anim_gif, "\n";
    sleep 1;

    print "remove temp gif...\n" if $debug;
    for my $ii (0..$draw_count-1)  {
        my $pix_name = sprintf "arr%02d.gif", $ii;
        if ( -e $pix_name )  {
            unlink $pix_name;
        }
    }
}

main;
