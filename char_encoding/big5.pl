#!/usr/bin/perl
#
# three handy regular expressions for ascii/big5/big5 plus
#

# 2006/12/27 by ericosur
# 2008/02/19 add warning and reviewed

use strict;
use warnings;
use Data::Dump qw(dump);

my $ascii = qr([a-zA-Z0-9]+);
my $big5 = qr{
    [\xA1-\xF9][\x40-\x7E\xA1-\xFE]
};
my $big5plus = qr{
    [\x81-\xFE][\x40-\x7E\x80-\xFE]
};

my $data=<<EOL;
處理一個process的步驟如下
EOL

my @chars = $data =~ m/$big5|$ascii+/gox;
my @charsplus = $data =~ m/$big5plus|$ascii+/gox;
my @big5 = $data =~ m/$big5+/gox;

dump @chars;
dump @charsplus;
dump @big5;
