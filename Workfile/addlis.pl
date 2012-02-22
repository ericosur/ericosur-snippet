#!/usr/bin/perl

my $ifh;
my $ofh;

my $lis_file = "a.txt";
my $out_file = "total.txt";

system "cmd /c dir /s /b *.lis > $lis_file";

open my $lis_fh, $lis_file or die;
open $ofh, "> $out_file" or die;

while (<$lis_fh>)  {
	s/\r//;
	s/\n//;
	next if m/^$/;
	my $ifile = $_;
	open $ifh, $ifile or die;
	print $ofh "\n===> $ifile\n";
	while (<$ifh>)  {
		print $ofh $_;
	}
	close $ifh;
}

close $lis_file;
close $ofh;

unlink $lis_file;

__DATA__
h:\INDIGO25_07B_GPRS_W08.16_MMI\make\plutommi\conn_app\conn_app.lis
h:\INDIGO25_07B_GPRS_W08.16_MMI\make\plutommi\inet_app\inet_app.lis
h:\INDIGO25_07B_GPRS_W08.16_MMI\make\plutommi\media_app\media_app.lis
h:\INDIGO25_07B_GPRS_W08.16_MMI\make\plutommi\mmi_app\mmi_app.lis
h:\INDIGO25_07B_GPRS_W08.16_MMI\make\plutommi\mmi_framework\mmi_framework.lis
