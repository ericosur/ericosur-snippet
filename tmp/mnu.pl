use strict;
use warnings;

sub do_help
{
	print "ActiveState::Menu demo\n";
}

sub do_bar
{
	print "do_bar()\n";
}

use ActiveState::Menu qw(menu prompt yes);

my $sel = menu([qw(Foo Bar Baz)]);

menu(intro  => "M E N U",
  menu   => [["&Foo", \&do_foo],
             ["S&ub", {
                 intro      => "S U B  M E N U",
                 menu       => [qw(Apples Oranges Exit)],
                 loop_until => 2,
             }],
             ["Ba&r", \&do_bar],
             "-----",
             ["&h", \&do_help],
             ["(Ba&z)", \&do_baz]],
  prompt => "What (type 'h' for help)?",
  force  => 1,
 );

my $ans = (prompt("What is your favourite colour?", "blue"));

if (yes("Do you really want to quit?")) {
  print "Bye\n";
  exit;
}
