#!/usr/bin/perl
#rec = {	'name': {'first': 'Brown', 'last': 'Smith'},
#		'job': ['dev', 'mgr'],
#		'age': 40.5}

use Data::Dump qw(dump);
use Data::Dumper;

sub sep
{
	print '-' x 40,"\n";
}

sep;
# hash
%a = (a=>1,b=>2,c=>3);
dump %a;
print $a{b},"\n";
sep;

# hash
%c = (d,4,e,5,f,6);
dump %c;
print $c{e},"\n";
sep;

# array of hash ref
@b = {aa=>5,bb=>6,cc=>7};
dump @b;
print $b[0],"\n";
print $b[0]->{aa},"\n";
sep;

# array
@d = (mm=>17,nn=>19,oo=>23);
dump @d;
sep;

# ???
%e = {mm=>17,nn=>19,oo=>23};
dump %e;
print Dumper(%e);
print keys %e;
sep;
print values %e;
sep;

# ???
@zz = (1)[1,0];
dump @zz;
sep;
