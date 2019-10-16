#!/usr/bin/perl
#
# hash demo
#
#

use strict;
use warnings;

sub build_a_hash();
sub foo();
sub bar();
sub dump_hash(\%);
sub sep();

# init/clear/empty a hash
my %hash = ();

# hash ref
my $hash_ref;
my $hash_ref2 = 0;

my $foo = "foo";

# add a key/value pair to a hash
$hash{'key'} = 'value';
$hash{$foo} = $foo;

# add key/value pair with hash ref
$hash_ref = \%hash;

$hash_ref->{'key'} = 'value';

# assign several key/value to hash
%hash = {'apple', 25, 'ball', 30, 'cat', 400};
printf "line %d: dump_hash():\n", __LINE__;
dump_hash(%hash);
sep();

# NOTE: init with ( aa => 11, bb => 22 )
# differ from  { .. .. .. .. }
%hash = ( 'duck' => 23,
		'egg' => 5,
		'fish' => 29
	);
printf "line %d: dump_hash():\n", __LINE__;
dump_hash(%hash);
sep();

# copy a hash
my %hash_copy = %hash;	# copy hash
my $hash_ref_copy = $hash_ref;	# copy hash ref

# delete a single key/value pair
delete $hash{$foo};
delete $hash_ref->{$foo};

#################################################

%hash = ();
%hash = build_a_hash();

# perform action to each pair
while ( my ($k, $v) = each(%hash) )  {
	print "$k => $v\n";
}
sep();
# notice ''%$hash_ref''
while ( my ($k, $v) = each(%$hash_ref) )  {
	print "$k => $v\n";
}
sep();
dump_hash(%hash);
sep();
printf "size of hash: %d\n", scalar keys(%hash);
sep();

my $foo_ref = foo();
printf "%s => %s\n", 'a', $foo_ref->{'a'};
sep();

my $bar_ref = bar();
for my $xx (keys %$bar_ref)  {
	#printf "%s\t%s\n", $xx, $bar_ref->{$xx};
	# notice the syntax
	for my $yy (keys %{$bar_ref->{$xx}} )  {
		printf "{%s}->{%s} = %s\n", $xx, $yy, $bar_ref->{$xx}->{$yy};
		# ''$bar_ref->{$xx}->{$yy}'' could be ''$bar_ref->{$xx}{$yy}''
	}
}
sep();

#printf "%s: %s, %s\n", $aa, $bar_ref->{$aa}->{'verb'}, $bar_ref->{$aa}->{'num'};

#################################################

#
# new a hash and return it
#
sub build_a_hash()
{
	my @lines = <DATA>;
	my %hh = ();

	for (@lines)  {
		my ($kk, $vv) = ( m/(.*):\s*(\d+)/ );
		$kk =~ s/\s+$//;
		$hh{$kk} = $vv;
	}
	return %hh;
}

#
# new a hash ref and return it
#
sub foo()
{
	my $rr;

	$rr->{'a'} = 'apple';
	$rr->{'b'} = 'ball';
	$rr->{'c'} = 'cat';

	return $rr;
}

#
# build a hash to hash
#
sub bar()
{
	my ($noun, $num, $verb);

	my %loh = ();
	my @data = qw(Dog:97:run Apple:31:eat Bird:59:fly  Egg:43:boil);

	for (@data)  {
		($noun, $num, $verb) = ( m/(.*):\s*(\d+):\s*(.*)/ );

#		printf "%s-%s-%s\n", $noun, $num, $verb;
		$loh{$noun}{'num'} = $num;
		$loh{$noun}{'verb'} = $verb;
	}

#	print scalar keys %loh, "\n";
	return \%loh;
}

#
# dump hash
#
sub dump_hash(\%)
{
	my $hh = shift;

	return if not defined $hh;

	#for my $k (sort { $a <=> $b } keys %$hh)  {
	for my $k (sort { $a cmp $b } keys %$hh)  {
		#print $k;
		printf "%s => %s\n", $k, $hh->{$k} if $k and $hh->{$k};
	}
}


#
# print seperate line
#
sub sep()
{
	print '-' x 40, "\n";
}

__DATA__
Dog: 97: run
Apple: 31: eat
Bird: 59: fly
Milk: 11: flow
Egg: 43: boil
