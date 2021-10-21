#!/usr/bin/perl
# Copyright GPL (c) 2004 Mike Chirico mchirico@users.sourceforge.net mchirico@comcast.net


# You will need the following to work with
# SQLite3
#
#  $ perl -MCPAN -e shell
#  cpan> install DBI
#  cpan> install DBD::SQLite


# Reference
#  http://www.perl.com/pub/a/2004/09/12/embedded.html


use DBI;

$dbh = DBI->connect( "dbi:SQLite:dataperl.db" ) || die "Cannot connect: $DBI::errstr";

$dbh->do( "CREATE TABLE exam (ekey      INTEGER PRIMARY KEY,
                   fn        VARCHAR(15),
                   ln        VARCHAR(30),
                   exam      INTEGER,
                   score     DOUBLE,
                   timeEnter DATE)");

$dbh->do("CREATE TRIGGER insert_exam_timeEnter AFTER  INSERT ON exam
          BEGIN
            UPDATE exam SET timeEnter = DATETIME('NOW')
              WHERE rowid = new.rowid;
          END");


$dbh->do( "INSERT INTO exam (ln,fn,exam,score)
                        values ('Anderson','Bob',1,75)");
$dbh->do( "INSERT INTO exam (ln,fn,exam,score)
                        values ('Anderson','Bob',2,80)");


print "LAST insert id: ",$dbh->func('last_insert_rowid'),"\n\n\n";

$res = $dbh->selectall_arrayref( q( SELECT ln,fn,exam,score
                                        FROM exam
				    ));

foreach( @$res ) {
# We could do this, but it only works for 4 elements
#    print "$_->[0], $_->[1] $_->[2] $_->[3]\n";
# Therefore, use the more general form.
    foreach $i (0..$#$_) {
       print "$_->[$i] "
       }
    print "\n";
#  Note $_->[0] is the same as $$_[0]


}


# this will create a test function
# Also see http://search.cpan.org/~msergeant/DBD-SQLite-1.06/lib/DBD/SQLite.pm
$dbh->func( 'now', 0, sub { return time }, 'create_function' );
# Our Perl sign function signp. You could name this just sign, but I
# did not want to confuse it with a build in sign that I created.
$dbh->func( 'signp', 1, sub { return $_[0] > 0 ? 1 : $_[0] < 0 ? -1 : 0; }, 'create_function' );

$dbh->do( "CREATE TABLE t (a INTEGER)");
$dbh->do( "INSERT INTO t VALUES ( now() ) " );



$dbh->do( "INSERT INTO t VALUES ( signp(0) ) " );
$dbh->do( "INSERT INTO t VALUES ( signp(-34) ) " );
$dbh->do( "INSERT INTO t VALUES ( signp(100) ) " );

print "TABLES \n";

$res= $dbh->selectall_arrayref( "PRAGMA table_info(exam)");
foreach( @$res ) {
    foreach $i (0..$#$_) {
       print "$_->[$i] "
       }
    print "\n";

}

$dbh->disconnect;
