#!/usr/bin/perl

use strict;
use warnings;
use DBI;

sub main()  {
	my $dbh;

	$dbh = DBI->connect( "dbi:SQLite:data.dbl" ) || die "Cannot connect: $DBI::errstr";

	$dbh->do( "CREATE TABLE authors ( lastname, firstname )" );
	$dbh->do( "INSERT INTO authors VALUES ( 'Conway', 'Damian' ) " );
	$dbh->do( "INSERT INTO authors VALUES ( 'Booch', 'Grady' ) " );

	$dbh->do( "CREATE TABLE books ( title, author )" );
	$dbh->do( "INSERT INTO books VALUES ( 'Object Oriented Perl',
											  'Conway' ) " );
	$dbh->do( "INSERT INTO books VALUES ( 'Object-Oriented Analysis and Design',
											  'Booch' ) ");
	$dbh->do( "INSERT INTO books VALUES ( 'Object Solutions', 'Booch' ) " );

	my $res = $dbh->selectall_arrayref( q( SELECT a.lastname, a.firstname, b.title
						FROM books b, authors a
						WHERE b.title like '%Orient%'
						AND a.lastname = b.author ) );
	foreach( @$res ) {
		print "$_->[0], $_->[1]:\t$_->[2]\n";
	}

	$dbh->disconnect;
}

main;
