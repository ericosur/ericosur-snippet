#!/usr/bin/env perl

use strict;

# use ImageMagick or GraphicsMagic 'convert' to perfrom image resize 50%
sub process_one_file($$)
{
	my $file = shift;
	my $mode = shift;
	my $nfn = $file;
	my $outdir;

	$nfn =~ s/\.jpg/-%mode.jpg/;
	my $cmd ;
	if ($mode eq "im") {
		$outdir = 'im';
		$cmd = sprintf("convert -resize 50%% %s %s/%s", $file, $outdir, $nfn);
	} else {
		$outdir = 'gm';
		$cmd = sprintf("gm convert -reisze 50%% %s %s/%s", $file, $outdir, $nfn);
	}
	print $cmd,"\n";
	system $cmd;
}

sub main()
{
    my $mode;

	printf("main ==>\n");
	my $list = 'list.txt';
	my $cnt = scalar @ARGV;
	#print $ARGV[0],"...\n";
	#print $ARGV[1],"...x\n";
	print "cnt: $cnt\n";
	if ($cnt > 0) {
		$mode = $ARGV[0];
		printf("mode: %s\n", $mode);
		#return;
	} else {
		printf("specify 'im' or 'gm'\n");
		return;
	}
	open my $fh, $list or die;
	while (<$fh>) {
		s/[\r\n]//;
		process_one_file($_, $mode);
	}
	close($fh);
}

main();
