#!/usr/bin/perl
#
# Program to build a regex to match an internet email address,
# from Chapter 7 of _Mastering Regular Expressions_ (Friedl / O'Reilly)
# (http://www.ora.com/catalog/regexp/)
#
# Unoptimized version.
#
# Copyright 1997 O'Reilly & Associates, Inc.
#


# Some things for avoiding backslashitis later on.
$esc        = '\\\\';               $Period      = '\.';
$space      = '\040';               $tab         = '\t';
$OpenBR     = '\[';                 $CloseBR     = '\]';
$OpenParen  = '\(';                 $CloseParen  = '\)';
$NonASCII   = '\x80-\xff';          $ctrl        = '\000-\037';
$CRlist     = '\n\015';  # note: this should really be only \015.



# Items 19, 20, 21
$qtext = qq/[^$esc$NonASCII$CRlist\"]/;               # for within "..."
$dtext = qq/[^$esc$NonASCII$CRlist$OpenBR$CloseBR]/;  # for within [...]
$quoted_pair = qq< $esc [^$NonASCII] >; # an escaped character

# Item 10: atom
$atom_char = qq/[^($space)<>\@,;:\".$esc$OpenBR$CloseBR$ctrl$NonASCII]/;
$atom = qq<
  $atom_char+    # some number of atom characters...
  (?!$atom_char) # ..not followed by something that could be part of an atom
>;


# Items 22 and 23, comment.
# Impossible to do properly with a regex, I make do by allowing at most one level of nesting.
$ctext   = qq< [^$esc$NonASCII$CRlist()] >;
$Cnested = qq< $OpenParen (?: $ctext | $quoted_pair )* $CloseParen >;
$comment = qq< $OpenParen
                     (?: $ctext | $quoted_pair | $Cnested )*
               $CloseParen >;

$X       = qq< (?: [$space$tab] | $comment )* >; # optional separator



# Item 11: doublequoted string, with escaped items allowed
$quoted_str = qq<
        \" (?:                      # opening quote...
              $qtext                #   Anything except backslash and quote
              |                     #    or
              $quoted_pair          #   Escaped something (something != CR)
                             )* \"  # closing quote
>;

# Item 7: word is an atom or quoted string
$word = qq< (?: $atom | $quoted_str ) >;

# Item 12: domain-ref is just an atom
$domain_ref = $atom;

# Item 13 domain-literal is like a quoted string, but [...] instead of "..."
$domain_lit = qq<  $OpenBR                         # [
                   (?: $dtext | $quoted_pair )*    #    stuff
                   $CloseBR                        #           ]
>;

# Item 9: sub-domain is a domain-ref or domain-literal
$sub_domain = qq< (?: $domain_ref | $domain_lit ) >;




# Item 6: domain is a list of subdomains separated by dots.
$domain = qq< $sub_domain                          # initial subdomain
              (?:                                  #
                 $X $Period                        # if led by a period...
                 $X $sub_domain                    #   ...further okay
              )*
>;

# Item 8: a route. A bunch of "@ $domain" separated by commas, followed by a colon
$route = qq< \@ $X $domain
             (?: $X , $X \@ $X $domain )* # further okay, if led by comma
         :                                # closing colon
>;


# Item 5: local-part is a bunch of $word separated by periods
$local_part = qq< $word                   # initial word
        (?: $X $Period $X $word )*        # further okay, if led by a period
>;

# Item 2: addr-spec is local@domain
$addr_spec  = qq< $local_part $X \@ $X $domain >;

# Item 4: route-addr is  <route? addr-spec>
$route_addr = qq[ < $X                    # leading <
                    (?: $route $X )?      #       optional route
                        $addr_spec        #       address spec
                                    $X >  #                  trailing >
];


# Item 3: phrase
$phrase_ctrl = '\000-\010\012-\037'; # like ctrl, but without tab

# Like atom-char, but without listing space, and uses phrase_ctrl.
# Since the class is negated, this matches the same as atom-char plus space and tab
$phrase_char =
   qq/[^()<>\@,;:\".$esc$OpenBR$CloseBR$NonASCII$phrase_ctrl]/;

$phrase = qq< $word            # one word, optionally followed by....
              (?:
                  $phrase_char  |  # atom and space parts, or...
                  $comment      |  # comments, or...
                  $quoted_str      # quoted strings
              )*
>;




# Item #1: mailbox is an addr_spec or a phrase/route_addr
$mailbox = qq< $X                         # optional leading comment
                (?: $addr_spec            # address
                    |                     #  or
                    $phrase  $route_addr  # name and address
                ) $X                      # optional trailing comment
>;




###########################################################################
# Here's a little snippet to test it.
# Addresses given on the commandline are described.
#

my $error = 0;
my $valid;
foreach $address (@ARGV) {
    $valid = $address =~ m/^$mailbox$/xo;
    printf "`$address' is syntactically %s.\n", $valid ? "valid" : "invalid";
    $error = 1 if not $valid;
}
exit $error;


