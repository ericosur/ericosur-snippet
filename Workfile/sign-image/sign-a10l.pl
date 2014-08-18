#!/usr/bin/perl

use strict;
use 5.010;

my $exp_script = "sg.exp";
my $odir = "test-sign";
my $ofile = "signed-a10l-img-DATE.zip";
my $intermediate = "signed-target-files.zip";
my $certdir = "/home/rasmus/duke";
my $delete_intermediate = 0;

sub sign_first($)
{
	my $file = shift;
    my $REPLACE_FILE;

	if ( -e $file ) {
		say "=====> file found...";
		$REPLACE_FILE = $file;
	} else {
        $REPLACE_FILE = `find ./dist/ -name 'tostab12AL-target_files*zip'`;
        $REPLACE_FILE =~ s/[\r\n]//;
	}
    say "=====> from file: " . $REPLACE_FILE;

    my $script=<<SCRIPTEOL;
#!/usr/bin/expect

spawn ./build/tools/releasetools/sign_target_files_apks -d $certdir REPLACE_ME $odir/$intermediate

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
    my $cmd = "./build/tools/releasetools/img_from_target_files $odir/$intermediate $odir/$ofile";
	print $cmd,"\n";
    system $cmd;
}

sub main()
{
    my $date = `date +%y%m%d-%H%M`;
	$date =~ s/[\r\n]//;
#	say $date;
	$ofile =~ s/DATE/$date/;
#	say $ofile;

	unless ( -d $odir ) {
        mkdir $odir;
    }

	my $ifile = $ARGV[0] // "";
    sign_first($ifile);
    say "=====> run expect...";
    system "expect $exp_script";
	if ($delete_intermediate) {
        unlink $exp_script;
    }

    sign_second();
    if ($delete_intermediate) {
	    unlink "$odir/$intermediate";
    }

	say "=====> output file at: $odir/$ofile";
}

main;

=pod
./build/tools/releasetools/img_from_target_files signed-target-files.zip signed-img.zip
=cut

