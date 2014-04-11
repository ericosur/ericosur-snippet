#!/usr/bin/perl

use strict;
use Getopt::Std;

my $cnt = 0;

sub check_file($)
{
    my $f = shift;
    my $cmd = sprintf("mediainfo \"%s\"", $f);
    my $of = "output-result.txt";
    my $output;

    open my $ofh, ">> $of" or die;
    #print "+" x 80, "\n";
    if (-e $f) {
        $cnt ++;
        #system($cmd);
        $output = `$cmd`;
        print $ofh $output;

    } else {
        printf("file [%s] not found!\n", $f);
    }
    #print "-" x 80, "\n";
    close $ofh;
    print "result is saved as $of\n";
}

sub open_flist($)
{
    my $flist = shift;
    open my $fh, $flist or die;
    while (<$fh>) {
        s/[\r\n]//g;
        my $ff = $_;
        printf("check_file: %s\n", $ff);
        check_file($ff);
    }
    close $fh;
    printf("%d files checked\n", $cnt);
}

sub help()
{
    print<<EOL;
$0 -h -d <dir> -f <file list>

    -h            this help message
    -d <dir>      specify directory contains media files
    -f <file>     specify media files
    -l <file>     specify file list

    will use "filelist.txt" as media file list if available at CWD.

EOL
}

sub main()
{
    my %opts = ();
	my $optcmd = 'd:f:l:h';
    my $flist = "filelist.txt";

	getopts($optcmd, \%opts);

	if ($opts{h})  {
		help();
		exit 1;
	}

	if ($opts{d})  {
		print $opts{d},"\n";
	} elsif ($opts{f}) {
		print $opts{f},"\n";
	} elsif ($opts{l}) {
		print $opts{l},"\n";
		$flist = $opts{l};
		open_flist($flist);
	} else {
	    if ( -e $flist ) {
	        print "use CWD file list\n";
	        open_flist($flist);
	    } else {
	        help();
	    }
    }
}

main;
