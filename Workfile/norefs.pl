#!/usr/bin/perl

# add '''no strict 'refs'''' to specified file
# after the '''use strict'''

use strict;
use warnings;
use v5.10;

my $debug = 0;

sub insert_line($)
{
	my $ifile = shift;
	my $ifh;
	my $ofile = $ifile;
	my $ofh;
	my $bfile = $ifile;

	say $ifile;
	open $ifh, $ifile or die;
	$ofile =~ s/^(.*)\.pl/$1\.pl\.tmp/;
	$bfile =~ s/^(.*)\.pl/$1\.pl\.bak/;
	open $ofh, "> $ofile" or die;

	while ( <$ifh> )  {
		if (/^#/)  {
			print $ofh $_;
			next;
		}
		if ( m/^\s*use strict;/ )  {
			print $ofh $_;
			print $ofh "no strict 'refs';\n";
		}
		else  {
			print $ofh $_;
		}
	}

	close $ofh;
	close $ifh;

	say "output to $ofile" if $debug;
#	say "rename $ifile to $bfile" if $debug;
	rename $ifile, $bfile;
	say "rename $ofile to $ifile" if $debug;
	rename $ofile, $ifile;
}

sub process_file_list($)
{
	my $ifile = shift;
	open my $fh, $ifile or die;
	while (<$fh>)  {
		s/[\r\n]//;
		insert_line($_);
	}
	close $fh;
}

sub main()
{
	my @args = @ARGV;
	if (not @ARGV)  {
		say "no file specified, use default value ./*.pl";
		push @args, "*.pl";
	}

	while (@args)  {
		my $file = shift @args;
		if ($file =~ m/^@/)  {		# @list.txt: list.txt is file list
			$file =~ s/^@//;
			say "using file list: $file";
			process_file_list($file);
		}
		else  {
			if ($file =~ /[*?]/)  {
				my @farr = glob($file);
				foreach my $ff (@farr)  {
					insert_line($ff);
				}
			}
			else  {
				insert_line($file);
			}
		}
	}
}

main;
