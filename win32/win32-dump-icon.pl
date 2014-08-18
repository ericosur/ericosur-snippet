#!/usr/bin/perl
use Win32::Exe;
use Data::Dump qw(dump);
use Data::Dumper;
use Dumpvalue;

my $ifile = q(c:/windows/system32/cmd.exe);
my $exe = Win32::Exe->new($ifile);
my $write_out = 0;	# 0: would not write out icons, 1: will output icons

printf STDERR "read icons from: %s\nSimulation: %s\n",
	$ifile, (! $write_out ? "Yes" : "No");

my $cnt = 0;
# Dump icons in an executable
my $icon;
foreach $icon ($exe->icons) {
	++ $cnt;
	printf "Icon: %s x %s (%s colors) ==>\t",
			$icon->Width, $icon->Height, 2 ** $icon->BitCount;

	dump_icon($icon->Data, $cnt);
#	dumper_icon($icon, $cnt);
#	last;
}

sub dump_icon($$)
{
	my ($data, $cnt) = @_;
	# 2008/02/25 not a real win32 icon format???
	# it cannot be recognized as a window ico file :-<
	my $file = sprintf("foo_%04d.ico", $cnt);

	printf "[%s] output to $file\n", ($write_out ? "Actually" : "Simulating");

	if ($write_out)  {
		open my $fh, "> $file" or die;
		binmode($fh);

#	my $content = dump($data);
#	$content =~ s/\s+(.*\n)/ $1/g;
#	print $fh $content;

		print $fh $data;
		close $fh;
	}
}

sub dumper_icon($$)
{
	my ($icon, $cnt) = @_;
	#my $file = sprintf("dumper_02d.pl", $cnt);

	my $dumper = new Dumpvalue;

	$dumper->set(globPrint => 1);

	#print "output to $file\n";
	#open my $fh, "> $file" or die;

	#print $fh Data::Dumper->Dump($icon);
	#print $fh $dumper->dumpvars($icon);
	$dumper->dumpValue($icon);
	#$dumper->stringify($icon);

	#close $fh;
}
