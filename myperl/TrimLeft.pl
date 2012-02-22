#!/usr/bin/perl

# trim spaces at left of line
# -- Aug 9 1998 by Eric
# init version

while ( <> ) {
#    print ":$_";
    s/^\s+//;
    print STDOUT $_;
};
