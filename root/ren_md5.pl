#!/usr/bin/perl
# append filename with md5 checksum

use strict;
use warnings;

use Digest::MD5;
use Getopt::Std;

my %my_opt = ();

sub main
{
	getopts('chr', \%my_opt);	# -c -h -r are boolean values

	process_arg()
}

sub myproc($)
{
	my $file = $_;
	if ($my_opt{'c'})  {
		check_file($_);
	}
	elsif ($my_opt{'r'})  {
		remove_checksum($_);
	}
	else  {
		rename_file($_);
	}
}

# process command line file names and wildcards
sub process_arg()
{
	if (not @ARGV or $my_opt{h})  {
		print<<EOL;		# show help message

append md5 checksum to filename

	ren_md5.pl -h -c <filename> [[filename1] filename2 ... wildcard]

	-h		this help message
	-c		perform md5 check with the digest value from file name
	-r		remove the checksum from file name
	wildcards	*.jpg *.txt IMG_????.jpg
EOL

		exit(1);
	}
	if ($my_opt{'c'} && $my_opt{'r'})  {	# cannot use at the same time
		print STDERR "cannot use -c and -r at the same time\n";
		exit(999);
	}

	for (@ARGV)  {
		# wildcards file names
		if ( m/\*|\?/ )  {		# if contains '*' or '?'
			#print "glob...'$_'\n";
			my @filelist = glob($_);
			for ( @filelist )  {
				myproc($_) if ( -f $_ );	# file only
			}
		}
		# file list from command line
#		elsif ( m/^@/ )  {
#			s/^@//;
#			get_filename_from_list($_);
#		}
		# file names from command line without wildcards
		else  {
			myproc($_) if ( -f $_ );	# file only
		}
	}
}

#
# Input a filename like IMG_0123_980582db43955e92a800e224f1a610b6.jpg
# and validate the md5 checksum
#
sub check_file($)
{
	my $file = shift;
	my $recorded_sum;
	my $calculated_sum;

	if (-f $file)  {
		if ($file =~ m/^(.*)_([0-9A-Fa-f]{32})\.(.*)$/)  {
			$recorded_sum = $2;
			#printf "(%s)(%s)(%s)\n", $1, $2, $3;
			$calculated_sum = calc_md5($file);
			if ($recorded_sum eq $calculated_sum)  {
				print STDERR "$file: checksum ok\n";
			}
			else  {
				print STDERR "checksum not matched\n";
			}
		}
		else  {
			print STDERR "cannot found checksum from filename\n";
		}
	}
	else  {
		print STDERR "file <$file> not found\n";
	}

	return $calculated_sum;
}

sub remove_checksum($)
{
	my $file = shift;
	my $newf;
	my $oldf = $file;

	if (-f $file)  {
		if ($file =~ m/^(.*)_[0-9A-Fa-f]{32}\.(.*)$/)  {
			if ( length($1) >= 1 )  {
				$newf = $1 . "." . $2;
				print STDERR "oldf = $oldf\n";
				print STDERR "newf = $newf\n";
				rename $oldf, $newf if not -f $newf;
			}
		}
		else  {
			print STDERR "$file: file pattern is not matched\n";
		}
	}
	else  {
		print STDERR "<$file> not found\n";
	}

	return $newf;
}

sub rename_file($)
{
	my $file = shift;
	my $md5sum;
	my $oldf;
	my $newf;

	if (-f $file)  {
		$oldf = $file;
		$md5sum = calc_md5($file);

		#print "len=", length($md5sum), "\n";

		if ($file =~ m/(.+)\.(.*)$/)  {
			$newf = sprintf "%s_%s.%s", $1, $md5sum, $2;
			print "newf:", $newf, "\n";
		}
		if (not -f $newf)  {
			rename $oldf, $newf;
		}
		else  {
			print STDERR "file already exists, no action taken\n";
		}
	}
	else  {
		print STDERR "no such file\n";
	}

	return $newf;
}

sub calc_md5($)
{
	my $md5;
	my $fh;
	my $file = shift;
	my $digest = Digest::MD5->new();

	#print $file, "\n";

	# md5 hash
	open $fh, $file or die;
	binmode($fh);
	$md5 = $digest->addfile(\$fh)->hexdigest;
	close $fh;

	undef $digest;
	#print $md5,"\n";
	return $md5;
}

main;


=pod

=head1 NAME

ren_md5.pl

=head1 SYNOPSIS

ren_md5.pl IMG_0123.JPG
ren_md5.pl -c IMG_0123_980582db43955e92a800e224f1a610b6.jpg
ren_md5.pl -r image_0b667c6431269de338dbe20b6c762e11.png

=head1 DESCRIPTION

Append md5 checksum into specified file name. For example, change IMG_0123.jpg into
''IMG_0123_21fac4b338b98518f419e3642ffd0606.jpg''. Use '-c' to check the md5sum with
the value in filename. Use '-r' to remove the md5 checksum portion from filename.

=head1 NOTE

The length of hex string of md5 sum is 32.

=cut
