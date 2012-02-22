use Crypt::CBC;
use Crypt::OpenSSL::AES;

my $key = q(x3j5pnb2/PgDE1WEkKPCkgx1jtSnti0GOCxWSDYHSmDgeqGfhXqz1KqoVns1o9Fl
XCwyNDECgnZVC1swmYAKidaeE1rKTf5lWnukps7aEPh8HXj2idZ18Dv4fXk9ek6x);

my $file = "in.bin";
my $decrypt = 0;

sub main()
{
	$cipher = Crypt::CBC->new(
		-key    => $key,
		-cipher => "Crypt::OpenSSL::AES"
	);

	$encrypted = $cipher->encrypt($plaintext)
	#$decrypted = $cipher->decrypt($encrypted)

	$cipher->start($decrypt ? 'decrypt' : 'encrypt');

	my $in;
	my $fh;
    open $fh, $file || die "$file: $!";
    print $cipher->crypt($in) while read($fh, $in, 1024);
    close ARGV;

	print $cipher->finish;

}

main();
