#!/usr/bin/env perl

while (<DATA>) {
    s/[\r\n]//;
    if ( m/([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)/ ) {
        print "test: ", $_, "\n";
        printf("[%s]  [%s]\n", $1, $2);
    }
}

__DATA__
12,23
49,-100
-89,121
-78,-45
25.3452,121.3582
99.3418,-18.3829
-79.328281,110.182945
-34.2121,-48.2981
25.3452,121.
99,-18.3829
+38,-45
a382,b382.3
