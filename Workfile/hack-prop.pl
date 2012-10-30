#!/usr/bin/perl

use strict;

my $path = "device/toshiba/ast/";
my $ifile = "system.prop";
my $ofile = "system.prop.tmp";
my $bfile = "system.prop.bak";

sub modify_prop()
{
    open my $ifh, $ifile or die;
    open my $ofh, "> $ofile" or die;

    my $flag = 0;
    while ( <$ifh> ) {
    	if (m/^persist.service.adb.enable\s*=\s*(.*)$/) {
    		$flag = 1;
    		print $ofh "persist.service.adb.enable=1\n";
    		print "searched and modify\n";
    	} else {
    		print $ofh $_;
    	}
    }

    # never set it before
    if ($flag == 0) {
    	print $ofh "persist.service.adb.enable=1\n";
    	print "append adb enable\n";
    }

    close $ofh;
    close $ifh;
}

sub main()
{
    my $cmd;

	chdir $path or die;
	$cmd = "git reset --hard HEAD";
	system($cmd);

	modify_prop();
	if (-e $bfile) {
	    unlink $bfile;
	}
	rename $ifile, $bfile;
	rename $ofile, $ifile;
}

main;
