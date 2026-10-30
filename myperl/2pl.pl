#!/usr/bin/perl
# restore the wrapped batch file to original perl script
# -- Jul 23 1998 by Eric
# init version

use strict;

@ARGV = ('-') unless @ARGV;

process(@ARGV);

sub process {
  LOOP:
    foreach my $file_name ( @_ ) {
        my $fh = \*STDIN;
        if ( $file_name ne '-' ) {
            open($fh, '<', $file_name) or die "Can't open $file_name: $!";
        }
        my @real_script;
        my $b_script = 0;
      READLINE:
        while (my $line = <$fh>) {
            $b_script = 1 if ( $b_script == 0 && $line =~ /^#!.*perl/ );
            if ( $b_script == 1 ) {
                next READLINE if $line =~ /^#line/;
                last READLINE if $line =~ /^__END__/;
                push @real_script, $line;
            }
        }
        close($fh) unless $file_name eq '-';
        # change ext name
        my $out_name = $file_name;
        $out_name =~ s/\.bat$//;
        $out_name .= '.pl' unless $out_name =~ /\.pl$/ or $out_name eq '-';
        if (-e $out_name) {
            warn "File $out_name already exists, skipped\n";
            next LOOP;
        }
        print STDERR "output to $out_name\n";
        print STDOUT @real_script;
    }
}
