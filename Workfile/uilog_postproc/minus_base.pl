#!/usr/bin/env perl
#
# take the first line epoch as base,
# replace it as +diff
# take from stdin and output to stdout
#

=pod

# input:
[75611.141] D: Using the 'ivi-shell' shell integration
[75611.143] D: Loading main state...
[75611.147] D: Loading settings state...
[75611.148] D: Brightness changed to  50
[75611.152] D: BSA_DmSetConfig failed: 105
[75611.157] D: Loading settings state:  text_current_lang_code = en
# output:
[0.002] D: Loading main state...
[0.006] D: Loading settings state...
[0.007] D: Brightness changed to  50
[0.011] D: BSA_DmSetConfig failed: 105
[0.016] D: Loading settings state:  text_current_lang_code = en

=cut

use strict;

# the first line...
my $first = <STDIN>;
$first =~ m/^\[(\d+\.\d+)\]/;
my $base = $1;
my $sec = $1;
#print STDERR "base: ", $base, "\n";
printf("[%.3f]%s", $sec-$base, $');

my $sec;
while (<STDIN>) {
    s/[\r\n]//;
    if ( m/^\[
        (\d+\.\d+)
        \]/x
        ) {
        $sec = $1;
        printf("[%.3f]%s\n", $sec-$base, $');
    }
}
