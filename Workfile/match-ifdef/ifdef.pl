#!/usr/bin/perl

use strict;

#
# count #if and #endif
# and filter the #if/#endif lines out
# you might use ''match-ifdef.pl'' for further process
#

# regexp for my search
my $left = qr(^\s*\#if\s?);
my $right = qr(^\s*\#endif\s?);

my $file = $ARGV[0] or die "please speicifed a source file\n";
open my $fh, $file or die;

my $lcnt = 0;
my $rcnt = 0;
my $level = 0;	# the level of nested #if .. #endif
my $line = 0;	# line number

LINE:
while (<$fh>)  {
	++ $line;
	if (m/$left/)  {
		$lcnt ++;
		$level ++;
		print "+$line($level): $_";	# first char for left bracket is ''+''
	} elsif (m/$right/)  {
		$rcnt ++;
		$level --;
		print "-$line($level): $_";	# first char for right bracket is ''-''
		next LINE;
	}
}

close $fh;

print STDERR "#if's: $lcnt\n#endif: $rcnt\n";

__END__;

=pod

=head1 NOTE
<pre>
The output would like:
+162(1): #ifndef MMI_EMAILAPPACCOUNT_C
+165(2): #ifdef __MMI_EMAIL__
+193(3): #ifdef __MMI_EMAIL_DRM_SUPPORT__
-195(2): #endif
+196(3): #ifdef __MMI_TOUCH_SCREEN__
-198(2): #endif
+199(3): #ifdef __USB_IN_NORMAL_MODE__
-201(2): #endif
+216(3): #ifdef __SSL_SUPPORT__
-218(2): #endif /* __SSL_SUPPORT__ */
+220(3): #ifdef __MMI_EMAIL_DRM_SUPPORT__
</pre>

=cut
