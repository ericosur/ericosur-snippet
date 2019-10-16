#!/usr/bin/perl
=pod

=head1 NOTE
This script would translate
TAB 0x10,0x20,0x30,0x40,0x50,0x60,0x70,0x80
into
TAB 0x20,0x10,0x40,0x30,0x60,0x50,0x80,0x70
=cut

LINE: while ( <> )
{
    chomp;

    if ( /^\t0/ )  {
        s/^\t//;
        my $string = $_;
        $string =~ s/(\w+),(\w+),(\w+),(\w+),(\w+),(\w+),(\w+),(\w+)/$2,$1,$4,$3,$6,$5,$8,$7/g;
        print "\t$string\n";
    }
    else  {
        print "$_\n";
    }
}

print "// Trlanslated by swp.pl from rasmus_lai\n";

__END__;

# the following wrote by maggie
my $string = ",,0x10,0x20,0x30,0x40,0x50,0x60,0x70,0x80";
$string =~ m/(\w+),(\w+),(\w+),(\w+),(\w+),(\w+),(\w+),(\w+)/;
my $newString = "$2,$1,$4,$3,$6,$5,$8,$7";
print "$newString";

# my own
    ($a, $b, $c, $d, $e, $f, $g, $h) = split /,/;
    print "\t$b,$a,$d,$c,$f,$e,$h,$g,\n";

    #join ',', $b,$a,$d,$c,$f,$e,$h,$g;
    #print "\t$_\n";
