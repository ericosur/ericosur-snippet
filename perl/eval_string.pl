#!/usr/bin/perl

=pod

=head1
to demo a stupid way to hide its own source code

=head1
to generate the ascii code from source:


my $str=<<EOL;
sub hello()
{
	print "hello kitty!";
}
EOL

foreach (split //,$str)  {
	print ord($_),',';
}

=cut


my $data=q(115,117,98,32,104,101,108,108,111,40,41,10,123,10,9,112,114,105,110,116,32,34,104,101,108,108,111,32,107,105,116,116,121,33,34,59,10,125,10);

my $cmd;

foreach ( split(/,/,$data))
{
	$cmd = $cmd . chr($_);
}

#print $cmd;
eval $cmd;

hello();
