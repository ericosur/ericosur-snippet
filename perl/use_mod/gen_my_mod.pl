#!/usr/bin/perl
#
# take output of ''pl-use.pl''
# and output like
#
# 	use XXXX;	# 2
#	use YYYY;   # 1
#

my @pragmas = qw(attributes attrs autouse base bigint bignum bigrat
				blib bytes charnames constant diagnostics encoding
				fields filetest if integer less lib locale open
				ops overload ne sigtrap sort strict subs threads
				threads::shared utf8 vars vmsish warnings
				warnings::register 5.008008);

my $file = $ARGV[0] || "my_use.txt";
my %hash = ();
my %prags = ();

for (@pragmas)  {
	$prags{$_} = 1;
}

open $fh, $file or die;

LINE:
while ( <$fh> )
{
	if ( m/<<.*>>/ )  {
		next LINE;
	}
	if ( m/(.*)/ )  {
		$hash{$1} ++;
	}
}

close $fh;

for my $kk (sort keys %hash)  {
	if ( $prags{$kk} ne 1 )  {
		print "use $kk; \t# ", $hash{$kk}, "\n";
	}
}
