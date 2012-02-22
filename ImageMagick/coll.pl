#!/usr/bin/perl

#
# make collage image from specified images
# support wildcard
#

use strict;
use warnings;

use Image::Magick;

sub main();
sub process($);
sub get_filename_from_list($);
sub add_image($);
sub print_wh($$);

# total, bmp, gif, jpeg, png, unknown
my %count = ();
my ($outW, $outH) = (1024*2, 768*2);
my $outimage = Image::Magick->new;

# suggestion number of images to add into collection
# 先加入的圖會被後面的覆蓋
my $image_upper_limit = 40;

sub main()
{
	if (@ARGV)  {
		$outimage->Set(size=>"${outW}x${outH}");
		$outimage->Read('xc:black');

		foreach (@ARGV)  {
			if ( /\*|\?/ )  {			# if contains '*' or '?'
				#print "glob...'$_'\n";
				my @filelist = glob($_);
				foreach ( @filelist )  {
					process($_) if ( -f $_ );	# file only
				}
			}
			elsif ( /@/ ) {
				s/@//;
				get_filename_from_list($_);
			}
			else  {		# without wildcard
				process($_);
			}
		}
		# show the result
		foreach (keys %count)  {
			printf "%s => %s\n", $_, $count{$_};
		}

		# write the output image
		my $out_image = "collage.jpg";
		print "writing $out_image...\n";
		$outimage->Write($out_image);
	}
	else  {
		printf "\n%s <filename> [\@list file] [filenames...] \n", $0;
	}
}


# just take one argument and print it out
sub process($)
{
	my $file = shift;
#	print "$file: ";

	# only files are accepted
	if (-f $file)  {
		++ $count{total};
		#print "add_image($file)\n";

		if ( $count{total} <= $image_upper_limit )  {
			add_image($file);
		}
		else  {
			print '.';
		}
	}
}


sub get_filename_from_list($)
{
	my $list_file = shift;

	open FH, $list_file or die;
	while (<FH>)
	{
		s/[\r\n]//;
		#print $_;
		process($_);
	}
	close FH;
}

sub print_wh($$)
{
#	my ($ww, $hh) = @_;
#	printf "ww(%d), hh(%d)\n", $ww, $hh;
}


sub last_part($)
{
	my $str = shift;

	my $ii = rindex($str, '\\');
	#print $ii,"\n";

	if ( $ii != -1)  {
		return substr($str, $ii+1, length($str)-$ii-1);
	}
	return $str;
}


sub add_image($)
{
	my $fnam = shift;
	my $img = Image::Magick->new;
	my $err = $img->Read($fnam);
	die "Problem reading $fnam: $err" if $err;
	my ($w, $h) = ();

	# count::add
	print "add_image(${fnam})\n";
	++ $count{add};

	# resize
	($w, $h) = $img->Get('width','height');
	print_wh($w, $h);

	if ($w > $h)  {
		$img->AdaptiveResize(width => '320', height => '240');
	}
	else  {
		$img->AdaptiveResize(width => '240', height => '320');
	}

	($w, $h) = $img->Get('width','height');
	print_wh($w, $h);

	# add border
	my $mask = Image::Magick->new;
	my ($mw, $mh) = ($w+20, $h+80);	# need more config
	$mask->Set(size=>"${mw}x${mh}");
	$mask->Read("xc:#ffffff");	# white
	$mask->Composite(image => $img, x => '10', y => '10');

	$img  = $mask;	# overwrite
	undef $mask;

	($w, $h) = $img->Get('width','height');
	print_wh($w, $h);

	# annotate
	my $geo = sprintf '+8+%d', $h-18;
	my $label = last_part($fnam);
	#font=>'AR-MingtiM-BIG-5',
	$img->Annotate(text=>$label, geometry=>$geo, font=>'Arial',
					pointsize => 16, stroke => 'black',
					encoding=> 'UTF-8');
#	($w, $h) = $img->Get('width','height');

	# random rotate, the angel would be (-22.5 to + 22.5, ie +- pi/4 )
	my $rot = rand() * 45 - 22.5;
	print "rot = $rot\n";

	$img->Rotate(degrees=>$rot, color=>'black');
	$img->Transparent(color => 'black');

	($w, $h) = $img->Get('width','height');
	my ($x, $y) = ( rand()*($outW-$w), rand()*($outH-$h) );
	print_wh($x, $y);

	$outimage->Composite(image=>$img, x=>$x, y=>$y);
	undef $img;

# done
}


main();
