#!/usr/bin/perl

=pod

=head1 NOTE

 Recipe from perl cookbook 11.13. Storing Data Structures to Disk
 via Storable module.

=cut

use strict;
use Storable;

my $dfile = 'store.dat';

my %hash = ('a', 'apple', 'b', 'ball', 'c', 'cat');

store(\%hash, $dfile);

%hash = ();

# later on...
my $href = retrieve($dfile);        # by ref
#%hash = %{ retrieve($dfile) };   # direct to hash

foreach (keys %{$href})  {
	print $_," => ",$href->{$_},"\n";
}

# maybe you should delete the 'store.dat'
