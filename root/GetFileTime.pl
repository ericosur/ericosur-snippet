#!/usr/bin/perl
#
# use GetFileTime() to get the atime, mtime, and ctime from file
# 2007/11/06 by ericosur
# 2007/12/16 by ericosur: add POD, add more fancy print out and store in hash
#
#

use strict;
no strict "refs";	# I want to use %hash->{'level 1'}->{'level 2'}
use warnings;
use if $^O eq 'MSWin32', 'Win32API::File::Time qw{:win}';
#use Win32API::File::Time qw{:win};

sub sep
{
	print '-' x 40, "\n";
}

sub main()
{
	if ($^O ne 'MSWin32')  {
		die "only run in win32";
	}

	my $in_file = $ARGV[0] || $0;	# if no argument specified, use itself
	my $out_file = $ARGV[1];

	die "File not found" if (not -e $in_file);

# the scalar version I comment out
# my ($atime, $mtime, $ctime) = GetFileTime ($in_file);

# put data into hash
	my %tdata = ();

	($tdata{'access'}, $tdata{'modify'}, $tdata{'create'}) = GetFileTime ($in_file);

	printf "file: %s\n", $in_file;
	sep;
	for my $kk (keys %tdata)  {
		# put stringify version into $tdata{'access'}{'string'}
		$tdata{$kk}{'string'} = localtime($tdata{$kk});
		printf "(%s): %s\n", $kk, $tdata{$kk}{'string'};
	}
	sep;
}

main;


=pod

B<uncomment the following version if you want to copy file time to another>

if (-e $out_file)
{
	#SetFileTime ($out_file, $atime, $mtime, $ctime);
	SetFileTime ($out_file, $tdata{access}, $tdata{modify}, $tdata{create});
	printf "file time was set for: %s\n", $out_file;
}
else
{
	print "No file specified, no harm done\n";
}
=cut

__END__

=pod

=head1 NAME

GetFileTime.pl - read access/modify/create time from file and copy to
the other

=head1 SYNOPSIS

B<GetFileTime> I<from_file> [I<to_file>]

=over 2

=item from_file

The input file to get the file time.

=item to_file

I<optional>. The output file. The file time would copy from
I<from_file>.

=back

=head1 REQUIREMENTS

B<use> C<Win32API::File::Time>;

=head1 DESCRIPTION

This script would take C<atime/mtime/ctime> from I<from_file> with
C<GetFileTime()>. If I<to_file> is specified, the script would copy
the file time from I<from_file> to I<to_file>.

Here I have some comment for
B<Can't use string  as a HASH ref while "strict refs">

=cut
