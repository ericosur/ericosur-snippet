#!/usr/bin/perl

=pod

=head1 DESCRIPTION

This script deletes the trailing white spaces in each line of
specified file. The original file would be renamed to B<file.bak>.

You may use the following one liner:

perl -pi.bak -e "s/\s+\n$/\n/" file.txt

=head1 USAGE

-q will omit the zero line output
-p pause after action
-h help screen

=head1 VERSION

Aug 7 1998 by ericosur	init version
Oct 29 2004 by ericosur	reviewed
Nov 29 2004 by ericosur	add wildcard support
Oct 25 2007 by ericosur	add some information

=cut

use strict;
use warnings;

use Getopt::Std;

sub process;
sub help;
sub get_filename_from_list($);

my $quiet;
my $pause;

my %my_opt;
my $opt_cmd = 'pqh';

getopts($opt_cmd, \%my_opt);	

if ($my_opt{h})  {
	help;
	exit 1;
}

$pause = $my_opt{p} || 0;
$quiet = $my_opt{q} || 0;
# print $ARGV[0], "\n";

if (@ARGV)  {
	ARGV_LOOP: foreach (@ARGV)  {
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
}
else  {
	help;
	exit 1;
}

system "pause" if $pause;

# end of main procedure

sub process
{
	my $cnt = 0;
	my $line = 0;

    if ( -f $_ )  {
        my $file_name = shift;
        my $bak_file = $file_name . ".bak";
        my $tmp_file = $file_name . ".tmp";

        open FILE, "< $file_name" or die "Can't open $file_name: $!\n";
		open OUTFILE, "> $tmp_file" or die "cannot output to $tmp_file: $!\n";

        #print STDERR "[$file_name]:\t";

      READLINE:
        while (<FILE>) {
            $line++;
            if ( /\s+\n$/ ) {
                $cnt ++;
                # print STDOUT "#$line: $_";
				s/\s+\n$/\n/;
            }
			print OUTFILE $_;
        }

        if ( ($cnt != 0) || $quiet != 1 )  {
        	print "file: $file_name\nspace line processed: $cnt\n";
        }

		close FILE;
		close OUTFILE;

		rename $file_name, $bak_file;
		rename $tmp_file, $file_name;

		$cnt = 0;
		$line = 0;
    }
}

sub help
{
	print<<EOL;
***** help message *****
usage:
	kill_ts.pl [-p][-q] file1 file2 <wildcards> ...
options:
	<q>uiet no output if no trailing-space line
	<p>ause pause after operation
	<h>elp  help message

EOL
}

sub get_filename_from_list($)
{
	my $list_file = shift;

	open my $fh, $list_file or die;
	while (<$fh>)
	{
		s/(\r|\n)//;
		#print $_;
		process($_);
	}
	close $fh;
}
