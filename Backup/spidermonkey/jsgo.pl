#!/usr/bin/perl
# to execute an embedded js

use JavaScript;

print "js version: ", JavaScript::get_engine_version(),"\n";

my $rt = JavaScript::Runtime->new();
my $cx = $rt->create_context();
$cx->bind_function(write => sub { print @_; });
$cx->eval(q[

// js starts here

	function my99(n) {
	    // javascript: try to show a stupid 9x9 multiple table
	    for (i=1; i<=9; i++)  {
	        for (j=1; j<=9; j++)  {
	        	var mm = i*j;
	        	//write(Math.sqrt(mm));
	            write(i + "*" + j + "=" + (i*j) + "\t");
	        }
	        write("\n");
	    }
	}

	my99(1);

// js ends here

]);
