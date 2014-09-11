#!/usr/bin/perl

# translate unicode-7.0.0-blocks.txt U+[0-9A-F]{4,5}

use strict;
use Image::Magick;


my $BLOCKFILE = q(unicode-7.0.0-Blocks.txt);
my $PALETTEFILE = q(palette.txt);
my $color_cnt = 0;
my @colors = ();

my $COL = 512;
my $ROW = 384;
my $BIAS = -4;
=pod
# all blocks, 1114112 pixels
my $COL = 1024;
my $ROW = 1100;
my $BIAS = 0;

# no last 4 blocks, 195066 pixels
my $COL = 384;
my $ROW = 512;
my $BIAS = -4;
=cut

my $im;
# each element in @ends is HASH(start_pos, len)
my @ends = ();
# output file name
my $gf = 'map.png';

sub read_palette()
{
	my $if = q(palette.txt);
	open my $ifh, $if or die;
	while (<$ifh>) {
		next if (m/^$/);
		next if (m/^#/);
		while ( m/([0-9A-F]+)/g ) {
			push(@colors, $1);
		}
	}
	close $ifh;

    $color_cnt = scalar(@colors);
	#print "color cnt: $color_cnt\n";
}

# draw pixels, change line if reach line boundry
sub choose_color()
{
    #my $cc = shift;
    my $color_name = sprintf("#%02x%02x%02x",
		int(rand(255)), int(rand(255)), int(rand(255)));
	#$clr = sprintf("#%s", $colors[$cc % $ALLCOLOR]);
	return $color_name;
}

my $last_pt = 0;
sub draw_pt($)
{
    my $rh = shift;
    my ($cmd, $clr) = ();
    my ($xx, $yy) = ();
    my $cjk_color = '#3366ff';

    if ($rh->{name} =~ m/CJK/) {
        $clr = $cjk_color;
    } else {
        do {
            $clr = choose_color();
        } until ($clr ne $cjk_color);
    }

    #printf("draw_pt: start(%d),len(%d)\n", $rh->{start_pos}, $rh->{len});
    for (my $ii = 0; $ii < $rh->{len}; $ii++) {
        $xx = ($rh->{start_pos} + $ii) % $COL;
        $yy = int(($rh->{start_pos} + $ii) / $COL);
        $cmd = sprintf("pixel[%d,%d]", $xx, $yy);
        printf("%s => %s          \r", $cmd, $clr);
        $im->Set($cmd => $clr);
    }
    $last_pt = $rh->{start_pos} + $rh->{len};
    #print "yy: $yy\r";
    #print "$len, $last_pt, $cur_color\n";
}

sub my_draw($)
{
    my $block_limit = shift;

	$im = Image::Magick->new;
	my $sz = sprintf("%dx%d", $COL, $ROW);
    $im->Set(size => $sz);
    $im->ReadImage('xc:black');

    for (my $ii=0; $ii<$block_limit; $ii++) {
        draw_pt($ends[$ii]);
    }
    print "\n";

    unlink $gf;
    $im->Write($gf);

    undef $im;
    print "last_pt: $last_pt\n";
}

sub read_blocks()
{
    my $cnt = 0;

    # parse block data file and store into "@ends"
    open my $ifh, $BLOCKFILE or die;
	while (<$ifh>) {
		next if ( m/^$/ );
		next if ( m/^#/ );
		# $1: start_pos, $2: end_pos, $3: block name
		if ( m/^([0-9A-F]+)\.\.([0-9A-F]+);\s+(.+)$/ ) {
            my ($m, $n, $desc) = ($1, $2, $3);
			($m, $n) = (hex($m), hex($n));
			my $bl = ($n - $m + 1);
			#if ( $desc =~ m/CJK/ ) {
			    printf("start(%X), len(%d)  ", $m, $bl);
			    printf("line(%d): %s\n", int($m/$COL), $desc);
			#} else {
			    #printf("start(%X), len(%d)\n", $m, $bl);
			#}
			my %pair = (start_pos => $m, len => $bl, name => $desc);
            push(@ends, \%pair);
			$cnt ++;
		}
	}
    close $ifh;
    return $cnt;
}

sub main()
{
#	read_palette();

    my $bcnt;
    $bcnt = read_blocks();
    print "total blocks: $bcnt\n";

    # exclude last 4 blocks to draw
    # 2F800 will jump to E0000, large gap there
	my_draw($bcnt + $BIAS);
}

main;

