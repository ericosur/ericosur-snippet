#!/usr/bin/perl

=pod

=head1 NOTE

 Recipe from perl cookbook 11.13. Storing Data Structures to Disk
 via Storable module.

=cut

use strict;
use Storable;

sub gen_data_file($)
{
	my $file = shift;
	my %hash = ('b', 'ball', 'z', 'zebra', 'g', 'goat',
		'a', 'apple', 'c', 'cat');

	store(\%hash, $file);
	undef %hash;
}

sub main()
{
	my $dfile = 'storable.dat';
	gen_data_file($dfile);

	# later on...
	my $href = retrieve($dfile);        # by ref
	#my %hash = %{ retrieve($dfile) };   # direct to hash

	# sort hash by key or by value
	#foreach ( sort { $href->{$a} <=> $href->{$b} } (keys %{$href}) )  {
	foreach ( sort { $a cmp $b } (keys %{$href}) )  {
		print $_," => ",$href->{$_},"\n";
	}

	# delete the data file
	unlink $dfile;
}

main;
