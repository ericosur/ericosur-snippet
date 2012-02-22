use Test::Without::Module qw( Data::Dumper );

# Now, loading of My::Module fails :
eval { require Data::Dumper; };
warn $@ if $@;

# Now it works again
eval q{ no Test::Without::Module qw( Data::Dumper ) };
eval { require Data::Dumper; };
print "Found My::Module" unless $@;
