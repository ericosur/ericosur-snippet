#!/usr/bin/env perl

# only for win32

use strict;

use Getopt::Std;
use Win32::TieRegistry;
use Data::Dump qw(dump);

my %ib_reg = (
	"1002019" => q(48C6296A-4F4C-4238-A9E1-60E9A544A863),	# ib v3.40 (build 1019)
	"1002106" => q(B2DD5486-4922-42CC-A68E-C9069FFC3205)	# ib v3.51 (build 1106)
);

sub toggle_service($)
{
	my $onoff = shift;
	my $cmd;

	# toggle the agent service
	$cmd = sprintf("net %s \"IncrediBuild Agent\"", ($onoff ? "start" : "stop"));
	print $cmd,"\n";
	system $cmd;
}


sub get_ib_ver()
{
	$Registry->Delimiter("\\");
	my $ver = $Registry->{"HKEY_LOCAL_MACHINE\\SOFTWARE\\Xoreax\\IncrediBuild\\Builder\\Version"};

	return $ver;
}



sub read_registry($)
{
	my $reg_path = shift;
	die "no registry key path" unless $reg_path;

	# for make sure and debugging
	$Registry->Delimiter("/");
	my $abc = $Registry->{"HKEY_CLASSES_ROOT/Interface/{${reg_path}}/ProxyStubClsid32/"};
	dump($abc);
}

sub modify_registry($)
{
	my $reg_path = shift;
	die "no registry key path" unless $reg_path;

	die "crackib.exe not found!" unless (-e "crackib.exe");
	system "crackib";

	my $file = "ibreg.txt";
	open my $fh, $file or die "cannot read ibreg.txt";
	my $ibreg = <$fh>;
	$ibreg =~ s/\000//g;	# remove all 0x00 char
	close $fh;

	#print "new value: ", $ibreg, "\n";

	$Registry->Delimiter("/");
	# write new value
	$Registry->{"HKEY_CLASSES_ROOT/Interface/{${reg_path}}/ProxyStubClsid32/"} = {
		"/" => "$ibreg"
	};
}

sub main()
{
	my $ver = get_ib_ver();
	if ($ver)  {

		my $regpath = $ib_reg{$ver};
		read_registry($regpath);

		toggle_service(0);
		sleep 2;

		modify_registry($regpath);

		toggle_service(1);

		read_registry($regpath);

	}
	else  {
		die "cannot determine the version of crazybuild";
	}


#	read_registry();
#	toggle_service(1);


}

main();
