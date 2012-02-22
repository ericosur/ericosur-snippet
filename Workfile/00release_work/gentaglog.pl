#!/usr/bin/perl

use strict;
use warnings;
use 5.010;
use Getopt::Std;

my $g_opt_short = 0;
my $g_opt_tail = 0;

sub help_message()
{
	print<<EOL;
-h			this message
-s			short form
-t <num>	tail number
EOL
}

sub read_tags($)
{
	my $tagfile = shift;
	my @tags = ();
	my $fh = \*DATA;

	if ( -e $tagfile )  {
		say STDERR "read tags from $tagfile";
		open $fh, $tagfile or die;
	} else  {
		say STDERR "read from DATA section";
	}

	while (<$fh>)  {
		s/[\r\n]//;
		if ( length($_) )  {
			push(@tags,$_);
		}
	}
	return @tags;
}

sub main()
{
	my %opts = ();
	getopts('sht:',\%opts);

	$g_opt_tail = $opts{'t'};

	if ( $opts{'h'} )  {
		help_message();
	}
	elsif ( $opts{'s'} )  {
		$g_opt_short = 1;
		display();
	}
	else  {
		display();
	}
}

sub display()
{
	my $file = $ARGV[0] // 'ap-tags';
	my @tags = read_tags($file);
	my $arr_size = scalar @tags;
	my $logname = `date +%m%d%H%M`;
	my $prefix = 'repo forall -p -c git log';
	my $cmd;
	my @lines = ();

	$logname =~ s/[\r\n]//g;

	for (my $i=0; $i<$arr_size-1; $i++)  {
		# git log <old_tag>..<new_tag>
		if ($g_opt_short == 1)  {
			$cmd = sprintf("%s..%s", $tags[$i], $tags[$i+1]);
		} else  {
			$cmd = sprintf("%s --pretty=oneline %s..%s > %s-%d.log", 
				$prefix, $tags[$i], $tags[$i+1], $logname, $i);
		}
		push @lines, $cmd;
		if ($g_opt_tail == 0)  {
			say $cmd;
		}
		#system $cmd;
	}

	if ($g_opt_tail > 0)  {
		for (my $i=0; $i<$g_opt_tail; $i++)  {
			say pop @lines;
		}
	}
}

main;

# you may provide a file with these tags
# from old to new
__DATA__
0.H02400.00500jaJPN.110502.0-duke
0.H02700.00500GEN-enFR.110510.0-duke
0.H03000.00500GEN-enFR.110520.0
HEAD
