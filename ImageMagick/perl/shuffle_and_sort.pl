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

my $max_size = 20;
my $max_value = $max_size;
my $debug = 0;

# for output images
my $draw_image = 1;
my $maxx = 480;
my $maxy = 320;
my $draw_count = 0;   # for draw_array()
my $anim_gif = 'anim.gif';  # the final result
my $file_pattern = "array%04d.gif";

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


# it would alter the input array by reference
sub shuffle_ref(\@)
{
    my $aref = shift;
    my $n = scalar @$aref;

    if ($debug)  {
        print "before...\n";
        show_array(@$aref);
        print "n = $n\n";
    }

    my $cnt = 0;
    while ($n > 1)  {
        my $k = int(rand($n));
        $n --;
        if ($debug)  {
            printf "arr[%d], arr[%d] (%d,%d)\t", $n, $k, $$aref[$n], $$aref[$k];
        }
        ($$aref[$n], $$aref[$k]) = ($$aref[$k], $$aref[$n]);
        printf "%d(%d,%d) => ", ++$cnt, $n, $k if $debug;
        if ($draw_image)  {
            #draw_array($aref, $n, $k);   #show_array(@$aref);
        }
    }
    if ($debug)  {
        print "\nafter...\n";
        show_array(@$aref);
    }
}


sub bubble_sort(\@)
{
    my $aref = shift;
    my $n = scalar @$aref;

    for (my $ii=0; $ii<$n-1; ++$ii)  { # O(n^2) {{{
        for (my $jj=$ii; $jj<$n; ++$jj)  {
            if ($$aref[$ii] > $$aref[$jj])  {
                ($$aref[$ii], $$aref[$jj]) = ($$aref[$jj], $$aref[$ii]);
                if ($draw_image)  {
                    draw_array($aref, $ii, $jj);
                }
            }
        }
    } # }}}
}


sub shell_sort(\@)
{
    my $aref = shift;
    my $n = scalar @$aref;
    my $gap = int($n/2);
    my $moved;

    for ( $gap=$n; $gap>0; $gap=int($gap/2))  { # {{{
        do  {
            $moved = 0;
            for (my $ii=0; $ii<$n - $gap; $ii++)  {
                if ($$aref[$ii] > $$aref[$ii + $gap])
                {
                    ($$aref[$ii], $$aref[$ii + $gap]) = ($$aref[$ii + $gap], $$aref[$ii]);
                    draw_array($aref, $ii, $ii+$gap) if ($draw_image);
                    $moved = 1;
                }
            }
        } while ($moved);
    } # }}}
}


sub show_array(@)
{
    foreach (@_)  {
        printf "%02d  ", $_;
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
#    print "array_size = ", $array_size,"\n";
    print "$fr, $to\n";
    my $fill_color = 'black';
    for my $ii (0..$array_size)  {
        $fill_color = 'yellow' if ($ii == $fr);
        $fill_color = 'red' if ($ii == $to);
#        print "b4 draw: $ii, $val[$ii]\n";
        $im->Draw(primitive => 'rectangle',
    		  #points	=> '0,129 199,169',
    		  points => get_coord($ii, $val[$ii]),
    		  fill		=> $fill_color,
    		  strokewidth => 2,
    		  stroke	=> 'white');
        $fill_color = 'black';
    }

    my $pix_name = sprintf $file_pattern, $draw_count;
    print "output to $pix_name...\n";
    $im->Write($pix_name);
    $draw_count ++;
}


sub make_animate_gif($)
{
    my $source_file = $file_pattern;
    my $output_file = shift;

    $source_file =~ s/%04d/????/;

    if ($draw_image)  {
        # call convert of ImageMagick to produce animated gif
        my $cmd = "convert $source_file $output_file";
        $cmd = 'cmd /c ' . $cmd if ($^O eq "MSWin32");
        system $cmd;
        print "the result anim gif: ", $output_file, "\n";
        sleep 1;
        if (0)  {
	        print "remove temp gif...\n";
	        for my $ii (0..$draw_count-1)  {
	            my $pix_name = sprintf $file_pattern, $ii;
	            if ( -e $pix_name )  {
	                unlink $pix_name;
	            }
	        }
		}
    }
}


sub main()
{
    my @foo;
    my @bar;

    for (1..1)  { # {{{
        @foo = ();
        #@foo = gen_array_with_random_number();
        @foo = fill_array();

        shuffle_ref(@foo);
        @bar = @foo;

        $file_pattern = "bub%04d.gif";
        $draw_count = 0;
        ($draw_image) ? draw_array(@foo,-1,-1) : show_array(@foo);
        print "bb$_: ";
        show_array(@foo);
        bubble_sort(@foo);
        show_array(@foo);
        make_animate_gif("bubble.gif");

        $file_pattern = "shl%04d.gif";
        $draw_count = 0;
        ($draw_image) ? draw_array(@bar,-1,-1) : show_array(@bar);
        print "sh$_: ";
        show_array(@bar);
        shell_sort(@bar);
        show_array(@bar);
        make_animate_gif("shell.gif");
    } # }}}
}

main();
exit(0);
