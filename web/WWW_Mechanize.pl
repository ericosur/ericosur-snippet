#!/usr/bin/perl
#
# 回答 帳號/密碼
#

use WWW::Mechanize;

@info = (
  'foo.domain.com:port',
  'realm-name',
  'user id' => 'password');

my $agent = WWW::Mechanize->new();
$agent->credentials(@info) if @info == 4 or die("information is not enough");

$response = $agent->get(
  'http://foo.domain.com:port/misc.html'
);

print $response->content;
