#!/usr/bin/perl
#
# 2008/02/25
# to view VersionInfo within specified files
#

use strict;
use warnings;

use if $^O eq "MSWin32", "Win32::File::VersionInfo";
use Getopt::Std;

my $proc = \&get_version_info;
my %opts = ();

my $verbose = 0;

# process command line file names and wildcards
sub process_arg()
{
	if (not @ARGV)  {
		print "$0 [-v] <filenames>\n";
		exit -2;
	}

	getopts("v", \%opts);
	$verbose = $opts{'v'};

	for (@ARGV)  {
		# wildcards file names
		if ( m/\*|\?/ )  {		# if contains '*' or '?'
			#print "glob...'$_'\n";
			my @filelist = glob($_);
			for ( @filelist )  {
				&$proc($_) if ( -f $_ );	# file only
			}
		}
		# file list from command line
		elsif ( m/^@/ )  {
			s/^@//;
			get_filename_from_list($_);
		}
		# file names from command line without wildcards
		else  {
			&$proc($_) if ( -f $_ );	# file only
		}
	}
}

sub get_version_info($)
{
	my $file = shift;

	exit (-1) if (not -f $file);

	print $file, ":\n";
	my $foo = GetFileVersionInfo ($file);
	if ( $foo ) {
		for my $k (sort keys %$foo )  {
			my $v = $foo->{$k};
			if ( ref $v eq 'HASH' )  {
				for my $k2 (sort keys %$v)  {	#	while ( my ($k2, $v2) = (each %$v) )  {
					my $v2 = $v->{$k2};
					if ( ref $v2 eq 'HASH' )  {
						#	while ( my ($k3, $v3) = (each %$v2) )  {
						for my $k3 (sort keys %$v2)  {
							my $v3 = $v2->{$k3};
							print_out(3, $k3, $v3);
							#printf "3: %s => %s\n", $k3, $v3;
						}
					}
					else  {
						print_out(2, $k2, $v2);
						#printf "2: %s => %s\n", $k2, $v2;
					}
				}
			}
			else  {
				print_out(1, $k, $v);
				#printf "1: %s => %s\n", $k, $v;
			}
		}
	}
}

#
# modify regex in this sub if you want to filter out useless infomation
#
sub print_out($$$)
{
	my ($num, $key, $value) = @_;

	if ($verbose)  {
		printf "\t%d: %s => %s\n", $num, $key, $value;
	} elsif ($key =~ m/FileVersion/i)  {
		# print out if there is 'ver' sub string inside
		printf "\t%d: %s => %s\n", $num, $key, $value;
	}
}

sub test_function
{
	my $system_root = $ENV{"SystemRoot"};
	my $system32_dir = $system_root . "\\system32\\";

	my @filelist = glob($system32_dir . "*.dll");
	#get_version_info($system_root . "\\system32\\cmd.exe");
	foreach (@filelist)  {
		print "$_:\n";
		get_version_info($_);
	}
}

# read file name from list file
sub get_filename_from_list()
{
	my $list_file = shift;
	open my $fh, $list_file or die;

	while (<$fh>)  {
		s/\r//;
		s/\n//;

		&$proc($_);
	}

	close $fh;
}


sub main
{
	die "only work at MSWin32" if ($^O ne "MSWin32");
	process_arg();
}

main;
