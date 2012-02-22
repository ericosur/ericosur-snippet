#!/usr/bin/perl
#
# Program to build a regex to match an internet email address,
# from Chapter 7 of _Mastering Regular Expressions_ (Friedl / O'Reilly)
# (http://www.ora.com/catalog/regexp/)
#
# Optimized version.
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

##############################################################################
# Items 22 and 23, comment.
# Impossible to do properly with a regex, I make do by allowing at most one level of nesting.
$ctext   = qq< [^$esc$NonASCII$CRlist()] >;

# $Cnested matches one non-nested comment.
# It is unrolled, with normal of $ctext, special of $quoted_pair.
$Cnested = qq<
   $OpenParen                            #  (
      $ctext*                            #     normal*
      (?: $quoted_pair $ctext* )*        #     (special normal*)*
   $CloseParen                           #                       )
>;

# $comment allows one level of nested parentheses
# It is unrolled, with normal of $ctext, special of ($quoted_pair|$Cnested)
$comment = qq<
   $OpenParen                              #  (
       $ctext*                             #     normal*
       (?:                                 #       (
          (?: $quoted_pair | $Cnested )    #         special
           $ctext*                         #         normal*
       )*                                  #            )*
   $CloseParen                             #                )
>;

##############################################################################

# $X is optional whitespace/comments.
$X = qq<
   [$space$tab]*                    # Nab whitespace.
   (?: $comment [$space$tab]* )*    # If comment found, allow more spaces.
>;



# Item 10: atom
$atom_char   = qq/[^($space)<>\@,;:\".$esc$OpenBR$CloseBR$ctrl$NonASCII]/;
$atom = qq<
  $atom_char+    # some number of atom characters...
  (?!$atom_char) # ..not followed by something that could be part of an atom
>;

# Item 11: doublequoted string, unrolled.
$quoted_str = qq<
    \"                                     # "
       $qtext *                            #   normal
       (?: $quoted_pair $qtext * )*        #   ( special normal* )*
    \"                                     #        "
>;

# Item 7: word is an atom or quoted string
$word = qq<
    (?:
       $atom                 # Atom
       |                       #  or
       $quoted_str           # Quoted string
     )
>;

# Item 12: domain-ref is just an atom
$domain_ref  = $atom;

# Item 13: domain-literal is like a quoted string, but [...] instead of  "..."
$domain_lit  = qq<
    $OpenBR                            # [
    (?: $dtext | $quoted_pair )*     #    stuff
    $CloseBR                           #           ]
>;

# Item 9: sub-domain is a domain-ref or domain-literal
$sub_domain  = qq<
  (?:
    $domain_ref
    |
    $domain_lit
   )
   $X # optional trailing comments
>;

# Item 6: domain is a list of subdomains separated by dots.
$domain = qq<
     $sub_domain
     (?:
        $Period $X $sub_domain
     )*
>;

# Item 8: a route. A bunch of "@ $domain" separated by commas, followed by a colon.
$route = qq<
    \@ $X $domain
    (?: , $X \@ $X $domain )*  # additional domains
    :
    $X # optional trailing comments
>;

# Item 6: local-part is a bunch of $word separated by periods
$local_part = qq<
    $word $X
    (?:
        $Period $X $word $X # additional words
    )*
>;

# Item 2: addr-spec is local@domain
$addr_spec  = qq<
  $local_part \@ $X $domain
>;

# Item 4: route-addr is <route? addr-spec>
$route_addr = qq[
    < $X                 # <
       (?: $route )?     #       optional route
       $addr_spec        #       address spec
    >                    #                 >
];


# Item 3: phrase........
$phrase_ctrl = '\000-\010\012-\037'; # like ctrl, but without tab

# Like atom-char, but without listing space, and uses phrase_ctrl.
# Since the class is negated, this matches the same as atom-char plus space and tab
$phrase_char =
   qq/[^()<>\@,;:\".$esc$OpenBR$CloseBR$NonASCII$phrase_ctrl]/;

# We've worked it so that $word, $comment, and $quoted_str to not consume trailing $X
# because we take care of it manually.
$phrase = qq<
   $word                        # leading word
   $phrase_char *               # "normal" atoms and/or spaces
   (?:
      (?: $comment | $quoted_str ) # "special" comment or quoted string
      $phrase_char *            #  more "normal"
   )*
>;

## Item #1: mailbox is an addr_spec or a phrase/route_addr
$mailbox = qq<
    $X                                  # optional leading comment
    (?:
            $addr_spec                  # address
            |                             #  or
            $phrase  $route_addr      # name and address
     )
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


