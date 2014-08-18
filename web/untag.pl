#!/usr/bin/perl

# same topic in perl cookbook 20.6
# http://docstore.mik.ua/orelly/perl/cookbook/ch20_07.htm

use WWW::Mechanize;

sub show_lunar()
{
	my $url = 'http://tw.news.yahoo.com/';
	my $mech = WWW::Mechanize->new();
	$mech->get($url);
	my $html = $mech->content();

	my $new_html = untag($html);
	open FH, "> o.txt" or die;
	$new_html =~ s/\s+\n//gm;
	$new_html =~ s/\n+/\n/gm;

	print FH $new_html;
	close FH;
}

# this function is copied from http://www.perlmonks.org/?node_id=161281
sub untag {
  local $_ = $_[0] || $_;
# ALGORITHM:
#   find < ,
#       comment <!-- ... -->,
#       or comment <? ... ?> ,
#       or one of the start tags which require correspond
#           end tag plus all to end tag
#       or if \s or ="
#           then skip to next "
#           else [^>]
#   >
  s{
    <               # open tag
    (?:             # open group (A)
      (!--) |       #   comment (1) or
      (\?) |        #   another comment (2) or
      (?i:          #   open group (B) for /i
        ( TITLE  |  #     one of start tags
          SCRIPT |  #     for which
          APPLET |  #     must be skipped
          OBJECT |  #     all content
          STYLE     #     to correspond
        )           #     end tag (3)
      ) |           #   close group (B), or
      ([!/A-Za-z])  #   one of these chars, remember in (4)
    )               # close group (A)
    (?(4)           # if previous case is (4)
      (?:           #   open group (C)
        (?!         #     and next is not : (D)
          [\s=]     #       \s or "="
          ["`']     #       with open quotes
        )           #     close (D)
        [^>] |      #     and not close tag or
        [\s=]       #     \s or "=" with
        `[^`]*` |   #     something in quotes ` or
        [\s=]       #     \s or "=" with
        '[^']*' |   #     something in quotes ' or
        [\s=]       #     \s or "=" with
        "[^"]*"     #     something in quotes "
      )*            #   repeat (C) 0 or more times
    |               # else (if previous case is not (4))
      .*?           #   minimum of any chars
    )               # end if previous char is (4)
    (?(1)           # if comment (1)
      (?<=--)       #   wait for "--"
    )               # end if comment (1)
    (?(2)           # if another comment (2)
      (?<=\?)       #   wait for "?"
    )               # end if another comment (2)
    (?(3)           # if one of tags-containers (3)
      </            #   wait for end
      (?i:\3)       #   of this tag
      (?:\s[^>]*)?  #   skip junk to ">"
    )               # end if (3)
    >               # tag closed
   }{}gsx;          # STRIP THIS TAG
  return $_ ? $_ : "";
}

sub main
{
	show_lunar();
}

main;
