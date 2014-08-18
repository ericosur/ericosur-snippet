#!/usr/bin/perl

use strict;
use warnings;

my $from_nocard1 = qr(\"no_cert_file_found\" product=\"nosdcard\"[^>]*>([^<]+)<\/string>);
my $from1 = '';
my $dest_default1 = qr(\"no_cert_file_found\" product=\"default\"[^>]*>([^<]+)<\/string>);
my $dest1 = '';

my $file = 'list.txt';
my $fcnt = 0;
my $debug = 0;

sub process($)
{
	my $xmlfile = shift;
	my $xmlnew = $xmlfile . '.new';

	open my $fh, $xmlfile or die;
	open my $ofh, "> $xmlnew" or die;

	$fcnt ++;

	while (<$fh>) {
		my $line = $_;
		if ( m/$from_nocard1/ ) {
			$from1 = $1;
			print "from1: $1\n" if ($debug);
		} elsif ( $_ =~ $dest_default1 ) {
			print "before: $line" if ($debug);
			$line =~ s/$1/$from1/;
			#$line = $from1;
			print " after: $line" if ($debug);
		} else {
			# do nothing here
		}
		print $ofh $line;
	}

	close $ofh;
	close $fh;

	my $backup = $xmlfile . '.bak';
	rename $xmlfile, $backup;
	rename $xmlnew, $xmlfile;
}

sub main()
{
	open my $fh, $file or die;
	while (<$fh>) {
		s/[\r\n]//;
		print "open ", $_,"...\n";
		process($_);
	}
	close $fh;
	print "files processed: $fcnt\n";
}

main;

