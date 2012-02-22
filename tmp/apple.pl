$a =<<EOF;
an apple a day,
keeps a doctor away
EOF

print $a;

$a =~ s/\n//g;

print $a;
