#!/usr/bin/perl
use Net::HTTP;

sub main()
{
	$string = get("http://www.ptt.cc/bbs/Perl/M.1193183641.A.CFA.html");
	print $string;
}

sub get
{
        my $url = shift;
        my $retr;

        ($host, $addr) = $url =~ qq#http://(.*?)/(.*)#;
        my $s = Net::HTTP->new(Host => $host) || die $@;
        $s->write_request(GET => "/$addr", 'User-Agent' => "Mozilla/4.0");
        my($code, $mess, %h) = $s->read_response_headers;
        while (1) {
                my $buf;
                my $n = $s->read_entity_body($buf, 1024);
                die "read failed: $!" unless defined $n;
                last unless $n;
                $retr=$retr.$buf;
        }
        return $retr;
}

main();
