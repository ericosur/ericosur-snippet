#!/usr/bin/perl
# modm.pl
#
# insert timer.exe into the beginning and ending of M.bat
#


use strict;
use warnings;

#
# original file name
# temp working file name
# backup file name
#
sub change_fname($$$)
{
	my ($org, $tmp, $bak) = @_;
	rename $org, $bak;
	rename $tmp, $org;
}

# set /p WORK_VERNO=<~title.tmp


my $file = $ARGV[0] || "M.bat";
my $fh;
my $ofh;
my $para = $ARGV[1] if $ARGV[1];

open $fh, $file or die "file not found: $!\n";

my $ofile = $file . ".tmp";
my $bfile = $file . ".bak";
open $ofh, "> $ofile" or die "cannot write $ofile: $!\n";

printf "file: %s\nofile: %s\nbfile: %s\n", $file, $ofile, $bfile;

my $path = $ENV{"PATH"};

$path =~ s/;c:\\cygwin\\bin//i;
$path = "set path=" . $path;

LINE:
while ( <$fh> )  {
	if ( m/^\@echo off/ )  {
		# append ''timer'' at the beginning
		print $ofh $_;
		print $ofh "timer /nologo\n";
		print $ofh $path,"\n";
	}
	elsif ( m/^:MAKE_DONE/ )  {
		# append ''timer'' after the end
		print $ofh $_;
		print $ofh "timer /s /nologo\n";
	}
	elsif ( m/proj_select\.pl/ )  {
		print $ofh 'rem ', $_;
	}
	elsif ( m/set \/p CMD_PARA=<~cmd\.tmp/ )  {
		if ($para)  {
			print $ofh 'set CMD_PARA=', $para, "\n";
		}
		else  {
			print $ofh 'set CMD_PARA=Dusseldorf gprs', "\n";
		}
	}
	else  {
		print $ofh $_;
	}
}

close $fh;
close $ofh;

change_fname($file, $ofile, $bfile);
