#!/usr/bin/perl

use strict;
use v5.10;
use Encode qw(from_to);
use URI::Escape::XS;
use LWP::Simple;
use Image::Magick;

my $file = "1.txt";
my $debug = 0;

sub list_install_app($)
{
    my $f = shift;
    my $cnt = 0;
    my $ofile;
    my $appname;
    my $pkgname;

    open my $fh, $f or die;

    while (<$fh>) {
        next if ( m/^#/ );
        if ( m/(.*):/ ) {
            $appname = $1;
            next;
        } elsif ( m/(.*)/ ) {
            my $pkgname = $1;
            my $market_url = sprintf("http://market.android.com/details?id=%s", $pkgname);
            if ($debug) {
                print "market_url: $market_url\n";
            }
            my $qr_url = gen_qr($market_url);
            $ofile = sprintf("qr%04d.png", $cnt);
            my $real_file = get_qr_image($qr_url, $ofile);
            if ($debug) {
                print "real_file: $real_file\n";
            }
            sign_image($real_file, $appname);
            unlink($real_file);

            sleep(2);
            $cnt ++;
        }
        if ($debug && $cnt > 2) {
            last;
        }
    }

    close $fh;
    #print "cnt: $cnt\n";
}


sub get_qr_image($$)
{
	my $url = shift;
	my $ofile = shift;	# it's png format

	# use LWP::Simple to retrieve the generated qrcode image
	my $qr = get($url);

	if (-e $ofile)  {
		$ofile = get_new_ofile_name($ofile);
	}

	# output to file
	open my $fh, "> $ofile" or die;
	binmode $fh;
	print $fh $qr;
	close $fh;

	say "output to $ofile" if $debug;
	return $ofile;
}


sub gen_qr($)
{
	my $str = shift;
	# make sure valid chars for url
	my $safe = encodeURIComponent($str);

	# to call to google char api
	return "http://chart.apis.google.com/chart?cht=qr&chs=240x240&chl=$safe&choe=UTF-8";
}


# try qr.png qr(1).png qr(2).png qr(3).png ...
sub get_new_ofile_name($)
{
	my $fn = shift;

	while ( -e $fn )  {
		say "$fn exists" if $debug;
		if ($fn =~ m/(\d+)/ )  {	# number part exists
			say "number: $1" if $debug;
			my $num = $1 + 1;
			$fn =~ s/(\d+)/$num/;
		}
		else {
			my $ri = rindex($fn, '.');
			my $ofn = substr($fn, 0, $ri);	# before seperator
			my $ofe = substr($fn, $ri+1, length($fn) - $ri);	# after seperator
			say "ofn = $ofn" if $debug;
			say "ofe = $ofe" if $debug;
			$fn = sprintf "%s(1).%s", $ofn, $ofe;
		}
	}
    say "fn: $fn";
	return $fn;
}


#############################################################################
#
# arg1: file name
# arg2: the string would be annoted to the bottom of image
#
#############################################################################
sub sign_image($$)
{
	my $img_file = shift;
	my $annotation_text = shift;
	my $im = Image::Magick->new();
	my $fontsize = 12;

	if ( not -f $img_file ) {
		printf STDERR "%s not found, exit\n", $img_file;
		return;
	}

	my $rc = $im->Read($img_file);
	die "Cannot read $img_file: $rc" if $rc;
	my ($ww, $hh) = $im->Get('width', 'height');
	my $geom = sprintf "+15+%d", $hh - 15;
	if ($debug) {
	    printf "%s: %d, %d, %s\n", $img_file, $ww, $hh, $geom;
	}

	$im->Set(stroke => '#ffffff');
	$rc = $im->Annotate(
				  text 		 => $annotation_text,
				  font 		 => 'Lucida-Console',
				  fill		 => 'black',
				  stroke	 => 'black',
				  undercolor => 'white',
				  geometry	 => $geom,
				  pointsize  => $fontsize);
	warn $rc if $rc;

	my $ofile = make_filename($annotation_text);
	$im->Write($ofile);
	print "output: $ofile\n";# if $debug;
	undef $im;
}


#############################################################################
#
# append postfix to file name
#
sub make_filename($)
{
	my $file = shift;

    $file =~ s/[ \.-]+//g;
    $file = $file . '.png';
    print "result: $file\n" if $debug;
	return $file;
}


sub main()
{
    list_install_app($file);
}

main;
