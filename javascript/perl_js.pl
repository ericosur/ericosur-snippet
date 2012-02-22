use JavaScript;

print JavaScript::get_engine_version(),"\n";

my $rt = JavaScript::Runtime->new();
my $cx = $rt->create_context();
$cx->bind_function(write => sub { print @_; });
$cx->eval(q[
    // javascript: try a stupid 9x9 multiple table
    for (i=1; i<=9; i++)  {
        for (j=1; j<=9; j++)  {
            write(i + "*" + j + "=" + (i*j) + "\t");
        }
        write("\n");
    }
]);
