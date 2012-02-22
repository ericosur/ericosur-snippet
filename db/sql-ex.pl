#!/usr/bin/perl

use DBI;

$dbh = DBI->connect( "dbi:SQLite:dbname=aaa.dbl" ) || die "Cannot connect: $DBI::errstr";

$sql = "select id,name,pass from table01";
$sth = $dbh->prepare($sql) or die '123';
$sth->execute() or die '456';

while( $href = $sth->fetchrow_hashref )
{
	#print $href->{'id'},"\n";
	while ( ($debug_key, $debug_value) = each %{$href} )
	{
		print pack('A2 A13 A3','', $debug_key,'=>') . $debug_value,"\n";
	}
}

$dbh->disconnect;

__END__

D:\test>sqlite3.exe aaa.dbl ".dump"


BEGIN TRANSACTION;
CREATE TABLE table01 (id , name , pass );
INSERT INTO "table01" VALUES('1','ddd','ddd');
INSERT INTO "table01" VALUES('2','perl','cpan');
INSERT INTO "table01" VALUES('3','aaa','bbb');
INSERT INTO "table01" VALUES('5','sss','ggg');
INSERT INTO "table01" VALUES('6','sss',NULL);
COMMIT;
