#!/usr/bin/perl

=pod
algorithm of __Sieve of Eratosthenes__
wiki: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
and reference: http://www.csie.ntnu.edu.tw/~u91029/SieveOfEratosthenes.html

Prime Sieve of Eratosthenes
http://www.algorithmist.com/index.php/Prime_Sieve_of_Eratosthenes

may use the following command to produce video file
mencoder mf://*.jpg -mf w=772:h=772:fps=4:type=jpg \
    -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o output.avi

=cut

use strict;
use warnings;
use Image::Magick;
use Config::Simple;

#
# modify the sieve.ini to get different result
#
my $ini_file = 'sieve.ini';
my %config = ();

# could be customized
my $max_size;
my $max_col;
my $max_row;
my $x_padding;
my $y_padding;
my $x_space;
my $y_space;
my $file_pattern;
my $optimized;
my $drawing;

# derived values
my $max_value;
my $maxx;
my $maxy;

# global values
my $pass_count = 0;
my $draw_count = 0;

# sub prototypes
sub delete_multiple($$);
sub draw_black_dot($);
sub draw_init_array();
sub draw_array($);
sub fill_array($);
sub show_array($);
sub show_prime($);

# load_setting() {{{
sub load_setting()
{
	if (not -e $ini_file)  {
		warn "cannot found [$ini_file], use default\n";
	}

	Config::Simple->import_from($ini_file, \%config);

	$max_size = $config{'setting.max_size'} || 100;
	$max_col = $config{'setting.max_col'} || 10;
	$max_row = $config{'setting.max_row'} || 10;
	$x_padding = $config{'setting.x_padding'} || 1;
	$y_padding = $config{'setting.y_padding'} || 1;
	$x_space = $config{'setting.x_space'} || 5;
	$y_space = $config{'setting.x_space'} || 5;
	$file_pattern = $config{'setting.file_pattern'} || "sieve%03d.gif";
	$optimized = $config{'setting.optimized'} || 1;
	$drawing = $config{'setting.drawing'} || 0;

	#derived values
	$max_value = $max_size - 1;
	$maxx = $x_padding * ($max_col+1) + $x_space * $max_col;
	$maxx = 640 if ($maxx == 0);
	# make sure the size is multiple of 4
	if ($maxx % 4)  {
		$maxx = $maxx + 4 - ($maxx % 4);
	}
	$maxy = $y_padding * ($max_row+1) + $y_space * $max_row;
	$maxy = 480 if ($maxy == 0);
	# make sure the size is multiple of 4
	if ($maxy % 4)  {
		$maxy = $maxy + 4 - ($maxy % 4);
	}
}
# load_setting() }}}

# show_setting() {{{
sub show_setting()
{
	printf("maxsize: %d\nmax_col: %d\tmax_row: %d\nx_padding: %d\ty_padding: %d
x_space: %d\ty_space: %d\nfile_pattern: %s\noptimized: %d\ndrawing: %d\n",
		$max_size, $max_col, $max_row, $x_padding, $y_padding, $x_space, $y_space,
		$file_pattern, $optimized, $drawing);
	printf("Ouput iamge dimension: %d x %d\n", $maxx, $maxy);
}
# show_setting() }}}

# fill_array($) {{{
sub fill_array($)
{
    my $r = shift;
	my $debug = 0;

    for (1..$max_size)  {   # notice: index 0 is ignored
        push @$r, 1;
    }
    $$r[0] = 0;

    if ($debug)  {
   		print "size = ", (scalar @$r), "\n";
	   	for my $xx (@$r)  {
   			print $xx," ";
   		}
   		print "\n";
   	}
}
# file_array($) }}}


sub delete_multiple($$)
{
    my $aref = shift;
    my $start_p = shift;
    my $n = scalar @$aref;
    my $inc = $start_p;
	my $next_p;
	my $debug = 0;

	$pass_count ++;
	if ($debug)  {
		printf "start_p(%d),inc(%d)\n", $start_p, $inc;
	}

    # cannot start with 1, 0 or negatives
    if ($start_p <= 1)  {
        die "cannot be zero or one!";
    }

	$next_p = $start_p;

	if ($optimized)  {
		$start_p = $start_p * $start_p;
	} 	else  {
		$start_p = $start_p + $inc;
	}

	if ($debug)  {
		printf "start_p(%d),inc(%d),next_p(%d)\n", $start_p, $inc, $next_p;
	}
	my @deleted_idx = ();
    for (my $i = $start_p; $i <= $n; $i += $inc)  {
    	#print "mark pos: $i-1\n" if $debug;
        $$aref[$i-1] = 0;
        push @deleted_idx, ($i-1);
    }
	print "\n" if $debug;
	show_array($aref) if $debug;

	draw_black_dot(\@deleted_idx);
#	draw_array($aref);

    if ( $next_p >  sqrt($max_value) )  {
        return; # the left numbers would be primes
    }
    else  {
    	if ($debug)  {
        	print "==> start_p = ", $start_p, "\n";
        	print "==> next_p=", $next_p,"\n";
        }
        for (my $j = $next_p; $j < $n; ++ $j)  {   # to find the next availible {{{
			print "j = $j($$aref[$j])\n" if $debug;
			if ($$aref[$j] != 0)  {
				print "f: pos($j) not zero\n" if $debug;
				$next_p = $j+1;
				print "f: next_p = $next_p\n" if $debug;
				last;
			}
        } # }}}
        print "found next_p=", $next_p, "\n" if $debug;
        delete_multiple($aref, $next_p);
    }
}

sub shoot_array($)
{
    my $aref = shift;
    my $n = scalar @$aref;
    my $shoot_times = $max_value * 10;

    for (my $i = 0; $i < $shoot_times; ++$i)  {
        my $k = int(rand($n));
        $$aref[$k] = 0;
    }
}


sub show_array($)
{
	my $r = shift;

    foreach (@$r)  {
        print $_," ";
    }
    print "\n";
}

sub show_prime($)
{
	my $r = shift;
	my $idx = 0;
	my $cnt = 0;

	foreach (@$r)  { # {{{
		if ($_ != 0)  {
			printf("%d\t", $idx+1);
			++ $cnt;
		}
		$idx ++;
	} # }}}
	print "\n";
	print "total: $cnt found\n";
}

sub get_coord($)
{
    my $idx = shift;
    my $debug = 0;

#    print "get_coord(): $idx\n" if $debug;
#	printf "space: %d, %d\n", $x_space, $y_space;

#	-- $idx;
	my ($x1, $y1, $x2, $y2) = (0, 0, 0, 0);
	my $col = $idx % $max_col;
	my $row = int($idx / $max_col);
	if ($debug)  {
		printf "idx: %d(%d,%d) ", $idx, $col, $row;
	}

	$x1 = $x_padding * $col + ($col) * $x_space;
	$y1 = $y_padding * $row + ($row) * $y_space;
	$x2 = $x1 + $x_space;
	$y2 = $y1 + $y_space;

	my $cord = sprintf("%d,%d %d,%d", $x1, $y1, $x2, $y2);
	print $cord,"\n" if $debug;
    return $cord;
}

# draw_black_dot() only draw the deleted dot, not the whole array {{{
sub draw_black_dot($)
{
	if ($drawing == 0)  {
		print ".";
		return;
	}
    my $r = shift;
	my $im = Image::Magick->new();
	my $rc;
	my $debug = 0;
	my $fill_color = 'black';

    my $prev_pix_name = sprintf($file_pattern, $draw_count-1);
    print "draw_black_dot(): read from $prev_pix_name...\n" if $debug;

    $rc = $im->Read($prev_pix_name);
	warn $rc if $rc;

	print "draw dot at {\t" if $debug;
	foreach my $ii (@$r)  { # {{{
		print $ii,"\t" if $debug;
	    $im->Draw(primitive => 'rectangle',
			  #points	=> '0,129 199,169',
			  points => get_coord($ii),
			  fill		=> $fill_color,
			  strokewidth => 1,
			  stroke	=> $fill_color);
	} # }}}
	print "}\n" if $debug;
	my $pix_name = sprintf($file_pattern, $draw_count);
	$im->Write($pix_name);
	print "draw_black_dot(): write to $pix_name\n" if 1; #$debug;
    $draw_count ++;
} # }}}

#
# at first, only one dot at location 0 (number 1)
# need not draw every number in the array
#
sub draw_init_array()
{
	# turn on/off output pictures
	if ($drawing == 0)  {
		print ".";
		return;
	}
	my $im = Image::Magick->new(size => "$maxx x $maxy");
	my $rc;
	my $debug = 0;
	$rc = $im->Read('xc:red');
	warn $rc if $rc;
	my $fill_color = 'black';
    $im->Draw(primitive => 'rectangle',
		  points => get_coord(0),
		  fill		=> $fill_color,
		  strokewidth => 1,
		  stroke	=> $fill_color);
    my $pix_name = sprintf $file_pattern, $draw_count;
    print "draw_init_array(): output to $pix_name...\n";
    $im->Write($pix_name);
    $draw_count ++;
}

#
# draw_array(array)
#
sub draw_array($)
{
	# turn on/off output pictures
	if ($drawing == 0)  {
		print ".";
		return;
	}

    my $r = shift;
	my $im = Image::Magick->new(size => "$maxx x $maxy");
	my $rc;
	my $debug = 0;

	$rc = $im->Read('xc:black');
	warn $rc if $rc;

    my $array_size = scalar @$r;
    if ($debug)  {
    	print "array_size = ", $array_size,"\n";
    	print "line at ", __LINE__,"\n";
    }

    my $fill_color = 'black';
    my $idx = 0;
    foreach my $ii (@$r)  { # {{{
		if ($ii == 0)  {
			$fill_color = 'black';
			#print "b";
		} else  {
			$fill_color = 'red';
			#print "y";
		}

        $im->Draw(primitive => 'rectangle',
    		  #points	=> '0,129 199,169',
    		  points => get_coord($idx),
    		  fill		=> $fill_color,
    		  strokewidth => 1,
    		  stroke	=> $fill_color);
        $fill_color = 'black';
        $idx ++;
    } # }}}
	print "idx = $idx\n" if $debug;
    my $pix_name = sprintf $file_pattern, $draw_count;
    print "output to $pix_name...\n";
    $im->Write($pix_name);
    $draw_count ++;
}

sub main()
{
    my @foo = ();

	load_setting();
	show_setting();
	#exit;		# debugging on loading settings

    fill_array(\@foo);
#    show_array(\@foo);
	draw_init_array();		# draw_array(\@foo);

    delete_multiple(\@foo, 2);
    show_prime(\@foo);
}


main;

__END__;

=pod
The improvement:
// 1 to 65536 (1028x1028 gif)

rev.380
real    11m29.240s
user    11m22.795s
sys     0m6.120s

temp:1	// using draw_black_dots()
real    3m29.070s
user    3m23.397s
sys     0m5.464s

temp:2	// turn off debug in draw_black_dots()
real    3m26.480s
user    3m19.804s
sys     0m5.772s

temp:3 (rev 381)	// add draw_init_array()
real    3m5.277s
user    2m59.871s
sys     0m5.340s

=cut
