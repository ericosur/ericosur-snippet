#!/usr/bin/perl
=pod

=head1 NOTE
Use B<Cwd> or B<pwd> to get current working directory.

Notice the C</> or C<\> style

2007/01/10 by ericosur
=cut

use strict;
use warnings;

use Cwd;

my $cwd_str = cwd();
print $cwd_str,"\n";

$cwd_str =~ s[/][\\]g;
print $cwd_str,"\n";

# in win32 only
# print Win32::GetCwd(),"\n";