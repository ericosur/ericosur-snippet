#!/usr/bin/perl

use strict;

my %applist = ();

sub is_device_ok()
{
	my $cmd = q(adb devices);
	my $res = `$cmd`;
#    print $res;
	if ($res =~ m/[0-9a-v]{10}/g) {
		return 1;
	} else {
		return 0;
	}
}

sub parse_full_list()
{
	my ($fullpath,$path,$package,$apk) = ();

    open my $fh, "ful.txt" or die;
	while (<$fh>) {
		s/[\r\n]//;
		s/^package://;
		if (m/^([^=]+)=(.*)$/) {
            $fullpath = $1;
			$package = $2;
            $apk = $fullpath;
			if ( $fullpath =~ m/(\/.*\/)/ ) {
				$path = $1;
			}
			$apk =~ s/\/.*\///g;
#            printf("==> %s,%s,%s,%s\n", $fullpath, $package, $apk, $path);
			my %data = ();
			$data{"full"} = $fullpath;
            $data{"path"} = $path;
			$data{"apk"} = $apk;

			$applist{$package} = \%data;
		}
	}
    close $fh;
}

sub parse_attr_list($)
{
    my $type = shift;
	my $fn = $type . '.txt';

	my ($apk) = ();
	open my $fh, $fn or die;
	while (<$fh>) {
		s/[\r\n]//;
		s/^package://;
		if (m/(^(.*)$)/) {
			$apk = $1;
			my $hh = $applist{$apk};
			if (ref $hh eq 'HASH') {
				$hh->{$type} = $type;
#				print STDERR "$apk - $type\n";
			} else {
				print "$hh nok?\n";
			}
		}
	}
	close $fh;
}


sub get_full_apk_list()
{
#	my $f = shift;
	my $cmd;

#	if (is_device_ok()) {
	if (1) {
		$cmd = q(adb shell pm list package -f > ful.txt);
		system($cmd);
        $cmd = q(adb shell pm list package -s > sys.txt);
		system($cmd);
        $cmd = q(adb shell pm list package -d > dis.txt);
		system($cmd);
        $cmd = q(adb shell pm list package -3 > 3rd.txt);
		system($cmd);
	} else {
		print "did not call adb to get list\n";
	}
    parse_full_list();
	parse_attr_list('sys');
	parse_attr_list('dis');
	parse_attr_list('3rd');
}


sub show($)
{
	my $fn = shift;
	open my $ofh, ">$fn" or die;

    my $cnt = 0;
#    print "show()\n";
	foreach my $kk ( sort keys %applist) {
        $cnt ++;
        my $fp = $applist{$kk};
#		print $kk,"\n";
#		print $fp,"\n";
        print $ofh "$kk,$fp->{'full'},$fp->{'path'},$fp->{'apk'}";
		if ( $fp->{'sys'} ) {
			print $ofh ",SYS";
		} 
		if ( $fp->{'dis'} ) {
			print $ofh ",DIS";
		}
		if ( $fp->{'3rd'} ) {
			print $ofh ",3RD";
		}
		print $ofh "\n";
	}

	close $ofh;
}

sub main()
{
	my $ofile = 'result.csv';
	get_full_apk_list();

	show($ofile);
}

main;

