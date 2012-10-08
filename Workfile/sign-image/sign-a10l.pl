#!/usr/bin/perl

use strict;
use 5.010;

my $exp_script = "sg.exp";
my $odir = "test-sign";
my $intermediate = "signed-target-files.zip";
my $certdir = "/home/rasmus/duke";

sub sign_first()
{
    my $REPLACE_FILE=`find ./dist/ -name 'tostab12AL-target_files*zip'`;
    $REPLACE_FILE =~ s/[\r\n]//;
    #say $REPLACE_FILE;

    my $script=<<SCRIPTEOL;
#!/usr/bin/expect

spawn ./build/tools/releasetools/sign_target_files_apks -d $certdir -e motiv_theme_1_Strong.apk= -e motiv_theme_2_Medium.apk= -e motiv_theme_3_Soft.apk= -e motiv_theme_4_None.apk= REPLACE_ME $odir/$intermediate

expect "Enter password for $certdir/media key>"
send -- "28689155\\r"
expect "Enter password for $certdir/platform key>"
send -- "28689155\\r"
expect "Enter password for $certdir/releasekey key>"
send -- "28689155\\r"
expect "Enter password for $certdir/shared key>"
send -- "28689155\\r"

interact
SCRIPTEOL

    $script =~ s/REPLACE_ME/$REPLACE_FILE/;
    #print $script;

    my $ofile = $exp_script;
    open my $ofh, "> $ofile" or die;
    print $ofh $script;
    close $ofh;
}

sub sign_second()
{
    my $cmd = "./build/tools/releasetools/img_from_target_files $odir/$intermediate $odir/signed-img.zip";
	print $cmd,"\n";
    system $cmd;
}

sub main()
{
    sign_first();
    print "run expect...";
    system "expect $exp_script";
    unlink $exp_script;
    sign_second();
	unlink "$odir/$intermediate";
}

main;

=pod
./build/tools/releasetools/img_from_target_files signed-target-files.zip signed-img.zip
=cut

