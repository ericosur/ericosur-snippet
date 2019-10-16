#!/usr/bin/perl

use strict;
use warnings;

=pod

=head2

To practice how to pass arument to function

=cut

# 傳遞參數的練習
sub hello($$;);

sub hello($$;)
{
	my $one = shift;
	my $two = shift;

	print "$one, $two\n" if $one && $two;
}

sub main
{
	hello(100, 200);
	hello 37, 43;
	@_ = (53, 31);
	&hello;		# got warning
	&hello();	# got warning
}

main;
