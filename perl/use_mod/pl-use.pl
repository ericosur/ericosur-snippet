#!/usr/bin/perl
#
# to find the "use <???>;" from *.pl files
# the duplicated items would be ignored
#

#
# may use gen_my_mod.pl for further generation
#

use strict;
use warnings;

use File::Glob ':glob';

#
# todo: to ignore those are pragma not modules like "strict", "warnings"
# updated: it was done in "gen_my_mod.pl" to screen the perl pragmas
#

sub main()
{
	my @files = glob("*/*.pl");	# buggy!!!
	print join("\n", @files), "\n";
	map foo(), @files;
}

sub foo($)
{
	my $file = $_;
	my $found = 0;
	my $fh;
	my $line = 0;
	my @result = ();
	my $tok;

	$file =~ s/\r?\n?//;
	return if $file =~ /^$/;

	open $fh, $file or warn;

	#print "<$file>\n";
	#push @result, sprintf "<<%s>>", $file;
	while (<$fh>)  {
		++ $line;
		if ( m/^use ([\S^]+)\s?.*;$/ )  {
			push @result, $1;
			$found = 1;
		}
	}
	close $fh;

	#$tok = join "\n", @result;
	#print $tok if $found eq 1;
	if ($found eq 1)  {
		print "<<$file>>\n";
		my $uniq = unique_elem_from_array_unsort(\@result);
		print join("\n", @$uniq), "\n";
	}
	return $found;
}

sub unique_elem_from_array_unsort(\@)
{
	# eliminate duplicate values from a array
	# and don't care about the order of @array's elements.
	my $array = shift;
	my %hash = ();
	@hash{@$array} = ();
	$array = [keys %hash];
	return $array;
}

main();

__END__

# the output would be like:
<<check_rotate.pl>>
Image::ExifTool
Image::Magick
<<chg_relative.pl>>
strict
<<chn-1.pl>>
Ericosur
Encode
<<chn-2.pl>>
Ericosur
Encode
<<chn-3.pl>>
open
Ericosur
encoding
<<clipboard_demo.pl>>
Win32::Clipboard
