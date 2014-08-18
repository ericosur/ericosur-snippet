#!/usr/bin/perl

# what does /\p{IsUpper}{5,}/ mean???
#
# 2006/12/27 by ericosur

use strict;
use warnings;

use charnames ":full"; # use named chars with Unicode full names

sub main()
{
	my $count = 0;
	my $matched = 0;
	my $fh;
	my $file = $ARGV[0] || "pdf.txt";

	open $fh, $file or die "Please specify a file name: $!\n";

	while (<$fh>)
	{
		$count ++;
		if ( /\p{IsUpper}{3,}/i )	# search three more upper case characters
		{
			$matched ++;
			print "$count: $_" ;
		}
	}

	close $fh;

	print "$matched matched\n"
}

main();

__END__

# refer to "perlunicode"

    use charnames ":full"; # use named chars with Unicode full names
    $x = "BOB";
    $x =~ /^\p{IsUpper}/;   # matches, uppercase char class
    $x =~ /^\P{IsUpper}/;   # doesn't match, char class sans uppercase
    $x =~ /^\p{IsLower}/;   # doesn't match, lowercase char class
    $x =~ /^\P{IsLower}/;   # matches, char class sans lowercase

Here is the association between some Perl named classes and the traditional Unicode classes:

    Perl class name  Unicode class name or regular expression

    IsAlpha          /^[LM]/
    IsAlnum          /^[LMN]/
    IsASCII          $code <= 127
    IsCntrl          /^C/
    IsBlank          $code =~ /^(0020|0009)$/ || /^Z[^lp]/
    IsDigit          Nd
    IsGraph          /^([LMNPS]|Co)/
    IsLower          Ll
    IsPrint          /^([LMNPS]|Co|Zs)/
    IsPunct          /^P/
    IsSpace          /^Z/ || ($code =~ /^(0009|000A|000B|000C|000D)$/
    IsSpacePerl      /^Z/ || ($code =~ /^(0009|000A|000C|000D|0085|2028|2029)$/
    IsUpper          /^L[ut]/
    IsWord           /^[LMN]/ || $code eq "005F"
    IsXDigit         $code =~ /^00(3[0-9]|[46][1-6])$/

