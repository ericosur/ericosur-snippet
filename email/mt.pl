#!/usr/bin/perl
use MIME::Types;

my $mimetypes = MIME::Types->new;
my MIME::Type $plaintext = $mimetypes->type('text/plain');
my MIME::Type $imagegif  = $mimetypes->mimeTypeOf('gif');

print $plaintext,"\n";

print $imagegif,"\n";

if ($ARGV[0])  {
print $mimetypes->mimeTypeOf($ARGV[0]), "\n";
}
