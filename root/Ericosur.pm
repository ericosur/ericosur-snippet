package Ericosur;
use strict;
our (@ISA, @EXPORT, @EXPORT_OK, %EXPORT_TAGS, $VERSION);

use Exporter;
$VERSION = 1.00;              # Or higher
@ISA = qw(Exporter);

# Symbols to autoexport (:DEFAULT tag)
@EXPORT      = qw(sep show hexdump);

# Symbols to export on request
@EXPORT_OK   = qw(gcd gcd2 get_si);

# Define names for sets of symbols
#%EXPORT_TAGS = (
#    TAG1 => [...],
#    TAG2 => [...],
#    ...
#);

########################
# your code goes here
########################

#
# sep() to print a seperate line
#
sub sep()
{
	print '-' x 60, "\n";
}

#
# show() to print argument with newline
#
sub show(@)
{
	my @arg = @_;
	my $line = join(', ', @arg);

	print $line, "\n";
}

#
# gcd: greatest common divisor
#
sub gcd($$)
{
	my $a = shift;
	my $b = shift;
	my $t = 0;

	return 1 if (0 >= $a || 0 >= $b);

	while ($a != 0)  {
		$t = $b % $a;
		$b = $a;
		$a = $t;
	}

	return $b;
}

#
# gcd2: recursive method
#
sub gcd2($$)
{
	my $a = shift;
	my $b = shift;

	if ( $b eq 0 )  {
		return $a;
	}
	else {
		return gcd2($b, $a % $b);
	}
}

#
# hexdump()
#
sub hexdump($)
{
	my $foo = shift;
	my $len = length($foo);

	print "hexdump(): len=", $len, "\n";
	for my $ii (0..$len-1)
	{
		printf "%02x ", ord(substr($foo, $ii, 1));
	}
	print "\n";
}


#
# get_si()
# [in] 20480
# [out] 20k
#
sub get_si($)
{
	my $num = shift;
	my @unit = qw(B KB MB GB TB invalid error what nocanbe);
	my ($idx, $qu) = (0, 0);
	my $result;

	do  {
		$qu =  $num / 1024;
		$idx++ if ($qu >= 1);
		goto OUT if ($qu <= 1);
		$num = $qu;
	} while ( $num >= 1 );
OUT:

#	print "idx = $idx\n";
	$result = $num . ' ' . $unit[$idx];
	#print $result;
	return $result;
}


#
# this should be the last line
#
1;

__END__

=pod

=head1 NAME

Ericosur.pm

=head1 SYNOPSIS

C<sep>	print a seperate line

C<show>	show a list of argument

C<hexdump>	hexdump the argument

C<gcd>	calculate the gcd value of two integers

C<gcd2>	calculate the gcd value of two integers (recursive version)

=cut


