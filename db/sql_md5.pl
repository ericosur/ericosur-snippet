#!/usr/bin/perl

use strict;
use File::Glob ':glob';
use DBI;
use Digest::MD5;

my $dbh;
my $res;

my @filelist = glob("*.*");
my $sql_cmd;
my $sql_fmt = "INSERT INTO files VALUES ('%s', '%s')";
my $md5sum;

$dbh = DBI->connect( "dbi:SQLite:d:\\md5.db" ) || die "Cannot connect: $DBI::errstr";
$dbh->do( "CREATE TABLE files ( filename, md5sum )" );

for (@filelist)
{
	$sql_cmd = sprintf $sql_fmt, $_, calc_md5($_);
	#print $sql_cmd,"\n";
	$dbh->do($sql_cmd);
}

#
#$res = $dbh->selectall_arrayref( q( SELECT a.lastname, a.firstname, b.title
#				    FROM books b, authors a
#				    WHERE b.title like '%Orient%'
#				    AND a.lastname = b.author ) );
#
#foreach( @$res ) {
#  print "$_->[0], $_->[1]:\t$_->[2]\n";
#}

$dbh->disconnect;


sub calc_md5()
{
	my $md5;
	my $fh;
	my $file = shift;
	my $digest = Digest::MD5->new();

	# md5 hash
	open $fh, $file or die;
	binmode($fh);
	$md5 = $digest->addfile(\$fh)->hexdigest;
	close $fh;

	undef $digest;
	return $md5;
}
