#!/usr/bin/perl
#
# myglob.pl
#
# July 17 2002 by ericosur
# test on File::Glob
#

use File::DosGlob 'glob';
@files = glob "*.cpp *.h";
foreach $fname (@files)  {
    print "$fname\n";
}

@morefiles = glob "./larry/*.cpp ./larry/*.h ./macro/*.cpp ./macro/*.h ./md5/*.cpp ./md5/*.h";
foreach $fname (@morefiles)  {
    print "$fname\n";
}

__END__;

    require 5.004;
    # override CORE::glob in current package
    use File::DosGlob 'glob';
    # override CORE::glob in ALL packages (use with extreme caution!)
    use File::DosGlob 'GLOBAL_glob';
    @perlfiles = glob  "..\\pe?l/*.p?";
    print <..\\pe?l/*.p?>;
    # from the command line (overrides only in main::)
    > perl -MFile::DosGlob=glob -e "print <../pe*/*p?>"
