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
#no strict 'refs';

use File::Glob ':glob';

#
# todo: to ignore those are pragma not modules like "strict", "warnings"
# updated: it was done in "gen_my_mod.pl" to screen the perl pragmas
#

my $count = 0;
my $mod_count = -1;
my $dotfh;
my %hash = ();
my @pragmas = qw(attributes attrs autouse base bigint bignum bigrat
				blib bytes charnames constant diagnostics encoding
				fields filetest if integer less lib locale open
				ops overload ne sigtrap sort strict subs threads
				threads::shared utf8 vars vmsish warnings
				warnings::register 5.008008);
my %prags = ();
my ($dir, $graph) = ("->", "digraph");

for (@pragmas)  {
	$prags{$_} = 1;
}


sub main()
{
	my @files = glob("*/*.pl");	# buggy!!!
#	print join("\n", @files), "\n";

	open $dotfh, "> use.dot" or die;

	#output the header
	print $dotfh <<EOL;
$graph g {
	rankdir = LR;
	overlap = false;
	node [ fontsize=9 fontname=\"Lucida Console\"];

EOL

	map foo(), sort @files;

	#output the footer
	print $dotfh "}\n";
	close $dotfh;

	system "dot -Tpng -o use.png use.dot";
	print STDERR "output to use.png with use.dot\n";
}

sub foo($)
{
	my $file = $_;
	my $found = 0;
	my $fh;
	my $line = 0;
	my @result = ();
	my $tok;
	my $debug = 0;
	my $str;

	++ $count;

	$file =~ s/\r?\n?//;
	return if $file =~ /^$/;

	open $fh, $file or warn;

	print "=====> file: <$file>\n" if $debug;
	#push @result, sprintf "<<%s>>", $file;

	# open each perl file to find ''use'' statement
	while (<$fh>)  {
		++ $line;
		if ( m/^use ([\S^]+)\s?.*;$/ )  {
			print "found => $1\n" if $debug;
			if (not defined($prags{$1}))  {	# not pragma
				if (not defined($hash{$1}))  {	# first time in hash
					$mod_count ++;
					$hash{$1} = $mod_count;
					#$hash{$1}{"use"} ++;

					# output module name to dot file
					$str = sprintf "\tmod%03d [ label = \"$1\" ", $mod_count, $1;
					if (length($1) >= 8)  {
						$str = $str . "width = " . (length($1)/10*1.3) . " ";
					}
					$str = $str . " ];\n";
					print $dotfh $str;
					#printf "mod%03d [ label = \"$1\" ];\t", $mod_count, $1;
				}
				++ $found;
				push @result, $1;# and print "pushed\n";
			}
		}
	}
	close $fh;

	# to add a relationship about #mod -> file
	my $num = $#result + 1;
	#$str = sprintf "%d -> node%03d;\n", $num, $count;
	$str = sprintf "node%03d %s %d;\n", $count, $dir, $num ;
	if ($num != 0)  {
		print $dotfh $str;
	}

	#$tok = join "\n", @result;
	#print $tok if $found eq 1;

	if ($found > 0)  {

		# def file name as node
		$str = sprintf "node%03d [ label =\"%s\" shape = box ", $count, $file;
		if (length($file) >= 8)  {
			$str = $str . "width = " . (length($file)/10*1.2) . " ";
		}
		$str = $str . " ];\n";
		print $dotfh $str;

		# elimate the duplicated modules
		my $uniq = unique_elem_from_array_unsort(\@result);
		foreach my $kk (@$uniq)  {
			next if not defined($hash{$kk});
			printf $dotfh "mod%03d %s node%03d;\n", $hash{$kk}, $dir, $count ;
			#printf $dotfh "node%03d -> mod%03d;\n", $count, $hash{$kk};
		}
		#print join("\n", @$uniq), "\n";
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
