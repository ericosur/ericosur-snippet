#!/usr/bin/perl

=pod
=head1 NOTE
use google chart api to generate qr code
this script is for win32
remove from_to() and clipboard to support linux
=cut

use strict;
use warnings;
use v5.10;

use Encode qw(from_to);
use URI::Escape::XS;
use LWP::Simple;
use Getopt::Std;
# use if win32
use if $^O eq 'MSWin32', 'Win32::Clipboard';

my $debug = 0;

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
			say "found number!" if $debug;
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

	return $fn;
}

# test function for get_new_ofile_name()
sub test()
{
	my $f = 'qr.png';
	my $n;

	while (@ARGV)  {
		shift @ARGV;
		$n = get_new_ofile_name($f);
		say "touch $n";
		system "touch $n";
	}
}

# $url: url of chartapi
# $ofile: output fname
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

	say "output to $ofile";
}

sub help()
{
	print<<EOL;
take URL to generate QRcode image

url2qr.pl [options] url1 [url2 ...]

-h	this help message
-o 	specify the output file name (default: qr.png)
EOL
}

sub main()
{
	my %my_opt;

	if (!@ARGV)  {
		$my_opt{h} = 1;
	}

	getopts("o:h", \%my_opt);
	if ($my_opt{h})  {
		help();
		return;
	}

	while (@ARGV)  {
		my $str = shift @ARGV;

		# it would be local encoding in win32, translate to utf-8
		from_to($str, "BIG5", "UTF8");
		my $url = gen_qr($str);
		say $url;

		# copy it to win32 clipboard (only win32)
		if ($^O eq 'MSWin32')  {
			Win32::Clipboard->Set($url);
		}

		if ($my_opt{o})  {
			my $ofile = $my_opt{o};
			get_qr_image($url, $ofile);
		}
	}
}

main;
#test;
