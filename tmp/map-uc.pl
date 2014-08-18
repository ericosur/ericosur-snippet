$a = "a quick smart fox jumps over the lazy dog";

@phrases = split /\s/, $a;

@capital = map uc, split //, $a;
#show(@capital);

@first_word = map { m/.+(..)$/ } @phrases;
show(@first_word);

#show(@phrases);

$name = "a qUicK SMarT foX JumPS OveR tHe lAzY dOg";
$title = join ' ', map { ucfirst lc } split / /, $name;
print $title, "\n";
$title = join '),(', map { m/.(.).*/ m/.*(.)$/ } split / /, $name;
print $title, "\n";

sub show()
{
	my @in = @_;
	my $str = join ', ', @in;

	print $str, "\n";
}
