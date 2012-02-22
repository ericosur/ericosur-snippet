#!/usr/bin/perl
#
# List all installed perl modules in the current system
# and its own path.
#

use ActiveState::ModInfo qw(list_modules find_module);

#$path = find_module('Image::Magick');
#print $path,"\n" if $path;

# it would be a long list
%mod = list_modules();
# yeah, I sort the keys
for (sort keys %mod)  {
	print "$_ => $mod{$_}\n";
}
