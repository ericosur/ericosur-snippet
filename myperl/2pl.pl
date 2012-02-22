#!/usr/bin/perl
# restore the wrapped batch file to original perl script
# -- Jul 23 1998 by Eric
# init version

use strict;

@ARGV = ('-') unless @ARGV;

process(@ARGV);

sub process {
  LOOP:
    foreach ( @_ ) {
        my $file_name = $_;
        open(FILE, $file_name) or die "Can't open $file_name: $!";
        my @real_script;
        my $b_script = 0;
      READLINE:
        while (<FILE>) {
            $b_script = 1 if ( $b_script == 0 && /^#!.*perl/ );
            if ( $b_script == 1 ) {
                next READLINE if /^#line/;
                last READLINE if /^__END__/;
                push @real_script, $_;
            }
        }
        # change ext name
        $_ = $file_name;
        s/\.bat$//;
        $_ .= '.pl' unless /\.pl$/ or /^-$/;
        if (-e $_) {
            warn "File $_ already exists, skipped\n";
            next LOOP;
        }
        print STDERR "output to $_\n";
        print STDOUT @real_script;
    }
}
