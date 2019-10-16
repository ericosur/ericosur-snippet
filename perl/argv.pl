#!/usr/bin/perl
#@ argv.pl
#@ simple test for list all 'argv' strings
#
# argv demo
# also demo the while and shift
#
# 2006/12/27 by ericosur

@ARGV = ('-') unless @ARGV;
my $cnt = @ARGV;
print "There are $cnt items in arguments\n";

foreach my $i (@ARGV) {
    print "foreach: $i\n";
}

# note: use ``$ARGV[...]'' to access elem of array
for ($i=0; $ARGV[$i]; $i++) {
    print "\$ARGV[$i] = $ARGV[$i]\n";
}

while (@ARGV) {
    print "ARGV[0] = $ARGV[0]\n";
    print '@ARGV' . " = @ARGV\n";
    shift @ARGV;		# it will shrink @ARGV
}

if (@ARGV) {
    print "hell\n";
}
else {
    print "argv is null\n";
}
