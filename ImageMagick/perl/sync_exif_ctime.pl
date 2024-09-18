#!/usr/bin/perl

# change mtime, atime of specified file from its
# CreateDate in exif

use strict;
use Image::ExifTool ':Public';
#use Data::Dump qw(dump);
use Time::Local;
use DateTime;

my $debug = 0;
my $verbose = 0;
my $count_change = 0;
my $count_scan = 0;

sub sep()
{
	print '-' x 80,"\n";
}

sub get_epoch_from_str($)
{
	my $str = shift;
	my $epoch = 0;
	my ($yy, $mon, $dd, $hh, $mm, $ss) = ();

	if ( $str =~ m/(\d+):(\d+):(\d+) (\d+):(\d+):(\d+)/ )  {
		$yy = $1;
		$mon = $2;
		$dd = $3;
		$hh = $4;
		$mm = $5;
		$ss = $6;
		$epoch = timelocal($ss, $mm, $hh, $dd, $mon-1, $yy);
		if ($debug)  {
			print "epoch: ", $epoch, "\n";
		}
	}

	return $epoch;
}

sub get_exif_createdate($)
{
	my $file = shift;
	my $info;
	my $ret = 0;
	my $tag = 'CreateDate';

	$info = ImageInfo($file, $tag);
	if ($info)  {
		$ret = $info->{$tag};	# 1999:12:31 12:50:30
		print "ret: ", $ret, "\n" if $debug;
		return get_epoch_from_str($ret);
	}
	else  {
		return 0;
	}
}

sub get_mtime($)
{
	my $file = shift;

	my ($atime,$mtime,$ctime) = (stat($file))[8..10];

	return $mtime;
}

sub show_epoch_in_str($)
{
	my $ep = shift || 0;
	my $dt = DateTime->from_epoch( epoch => $ep );
	my $ret = $dt->ymd . ' ' . $dt->hms;

	print $ret, " UTC\n";
}

sub process($)
{
	my $file = shift;
	return unless ( -e $file );

	# get CreateDate from exif
	my $exif_time = get_exif_createdate($file);
	# get mtime of file
	my $n = get_mtime($file);
	my $is_equal = ($exif_time == $n);

    $count_scan ++;
    if ($verbose) {
        print "file: $file\n";

	    print("exif createdate: ", $exif_time, "\n") if $verbose;
	    show_epoch_in_str($exif_time) unless $is_equal;

	    print("ctime: ", $n,"\n") if $verbose;
	    show_epoch_in_str($n) unless $is_equal;
    }

    if ($is_equal) {
        print "$file exif_time equal to mtime, skip...\n";
    } else {
        # chage atime, mtime of specified file
		if ( utime($exif_time, $exif_time, $file) ) {
            warn "couldn't touch $file: $!";
        } else {
            $count_change ++;
        }
	}
}


sub get_filename_from_list($)
{
	my $list_file = shift;

	open FH, $list_file or die;
	while (<FH>)
	{
		tr/\r\n//;
		#print $_;
		process($_);
	}
	close FH;
}


sub main()
{
	#
	# most completely glob / argv here
	#
	if (@ARGV)  {
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

		printf("%d files changed\n", $count_change);
		printf("%d files scanned\n", $count_scan);
	}
	else  {
		print "sync file ctime from exif CreateDateTime\n\n";
		printf "sync_ctime.pl <filename> [\@list file] [filenames...] \n";
	}
}

main;
