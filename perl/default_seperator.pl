#!/usr/bin/perl
#
# a small script to demo $/ usage
#

my $data = undef;

open(FH, "input.txt");
{
   local $/ = undef;
   $data = <FH>;
	print "==>$data<==\n";
}
close(FH);

#print $data,"\n";
__END__
foreach(sort split/\s+/, $data) {
   print $_,$/;
}
