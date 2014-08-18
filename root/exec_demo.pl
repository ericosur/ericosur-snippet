#!/usr/bin/perl
# call the other perl script
# system("perl aparture.pl");
#
# 2007/08/07 by ericosur

$script = q(aparture.pl);
#eval $script;

#
# It seems not a good idea to use ''exec'' because it would
# not return to this script. Suggest to use the system() or
# `script` (the qx(...))
#
$_ = exec $script;
print '-' x 40,"\n";	# never reach here
$_ = `aparture.pl`;
print;
exit 1;

__END__;

=pod

=head1 NAME

	bed.pl

=head1 DESCRIPTION

Demo how to call the other perl script by using:

	system("perl aparture.pl");

	or

	exec "aparture.pl"

=head1 AUTHOR

	2007/08/07 by ericosur

=cut
