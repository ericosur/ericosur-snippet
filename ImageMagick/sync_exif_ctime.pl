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
my $count = 0;

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
	print "file => $file\n";

	my $exif_time = get_exif_createdate($file);
	print("exif createdate: ", $exif_time, "\n") if $verbose;
	show_epoch_in_str($exif_time);

	# get mtime of file
	my $n = get_mtime($file);
	print("ctime: ", $n,"\n") if $verbose;
	show_epoch_in_str($n);

	# chage atime, mtime of specified file
	if ($exif_time)  {
		my $rr = utime $exif_time, $exif_time, $file;
		if ($rr)  {
			print("rr = $rr\nutimed\n") if $verbose;
			$count ++;
		}
	}
	else  {
		print("nothing done\n") if $verbose;
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

		printf "%d files processed\n", $count;
	}
	else  {
		print "sync file ctime from exif CreateDateTime\n\n";
		printf "sync_ctime.pl <filename> [\@list file] [filenames...] \n";
	}
}

main;
