#!/usr/bin/perl
=pod

=head1 USAGE

count_ts.pl [-q] a.txt [b??.txt [c*.txt] ...]

=head1 NOTE

Count lines with trailing spaces. Accept wildcards by using C<glob()>.
Use C<-q> to omit the output if that file without trailing spaces.

=head1 SEE ALSO

see a simple trailing space version of ts.pl

=cut

use strict;
use warnings;
use Getopt::Std;

my $quiet = 0;

sub main
{
	unless (@ARGV)  {
		print "usage: count_ts.pl [-q] file1 file2 *.txt ...\n";
	}

	my %my_opt;
	getopts('q', \%my_opt);	# -o & -i are boolean value, -f take argument
	if ( $my_opt{'q'} )  {
		$quiet = 1;
	}
	#print "quiet: ", $quiet, "\n";

	while (@ARGV)  {
		my $ff = shift @ARGV;
		if ( $ff =~ m/\*|\?/ )  {			# if contains '*' or '?'
			#print "glob...'$_'\n";
			foreach my $fl ( glob($ff) )  {
				process($fl) if ( -f $fl );	# file only
			}
		}
		else  {		# without wildcard
			process($ff);
		}
	}
}

sub process($)
{
	my $cnt = 0;
	my $line = 0;
	my $f = shift;

    if ( -f $f )  {
        open(FILE, $f) or die "Can't open $f: $!";
        #print STDERR "[$f]:\t";

      READLINE:
        while (<FILE>) {
            $line++;
            if ( /\s+\n$/ ) {
                $cnt ++;
                # print STDOUT "#$line: $_";
            }
        }
		close FILE;

		if ($cnt != 0)  {
			print "$f: $cnt\n";
		}
		elsif ($quiet == 0 && $cnt == 0)  {
       		print "-$f: $cnt\n";
       	}


		$cnt = 0;
		$line = 0;
    }
}

main;
