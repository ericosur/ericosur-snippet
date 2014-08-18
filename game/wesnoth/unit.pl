#!/usr/bin/perl

use strict;
use v5.10;
use strict;
use Data::Dump qw(dump);

my $noname_count = 0;
my $unit_count = 0;
my $error_count = 0;
my $output_count = 0;

my @token = ("name", "type", "experience", "side",
    "hitpoints", "max_experience", "max_hitpoints", "moves", "max_moves");

sub list_unit($)
{
    my $f = shift;
    my $level = 0;
    my $line_no = 0;
    my $line_text;
    my $tag;
    my $flag = -1;
    my %val;

    open my $fh, $f or die;
    while (<$fh>) {
        ++ $line_no;
        s/[\r\n\s]//g;
        $line_text = $_;

        if ( m/\[(\w+)\]/ ) {
            $level ++;
                if ($1 eq "unit") {
                $flag = $level;
                %val = ();
                #print "$line_no ($level): $line_text\n";
            }
        } elsif ( m/\[\/(\w+)\]/ ) {
            $level --;
            if ($1 eq "unit") {
                $flag = -1;

			    if ( $val{"name"}->[0] eq "\"\"" ) {
			    	$noname_count ++;
			    } elsif ( $val{"side"}->[0] eq "1" ) {
					say '-' x 40;
			        dump_value(\%val);
			        $output_count ++;
					#say '-' x 40;
			    }

	            #print "$line_no ($level): $line_text\n";
	            %val = ();
	            $unit_count ++;
	            next;
            }
        }

        if ($flag == $level) {
            #say "# $line_text";
            my $ret = get_value($line_text, $line_no, \%val);
            if ($ret) {
                #print "$line_no: match $ret\n";
            }
        }
    }
    close $fh;
    say '-' x 40;
}

sub suggest_value($)
{
	my $val = shift;
	while ($val < 10) {
		$val += 5;
	}
	return $val;
}

sub dump_value($) {
    my $rr = shift;
	if ( scalar(keys(%$rr)) != scalar(@token) ) {
		$error_count ++;
		dump(%$rr);
	} else {
		say "name: ",$rr->{"name"}->[0];
		say "type: ",$rr->{"type"}->[0];
		#say "side: ",$rr->{"side"}->[0];
		print "exp: ", $rr->{"experience"}->[0], " / ", $rr->{"max_experience"}->[0], "\t\tline: ", $rr->{"max_experience"}->[1];
		printf "\tfrom %s to %s\n", $rr->{"max_experience"}->[0], 8;
		print "hp: ", $rr->{"hitpoints"}->[0], " / ", $rr->{"max_hitpoints"}->[0], "\t\tline: ", $rr->{"hitpoints"}->[1];
		printf "\tfrom %s to %s\n", $rr->{"hitpoints"}->[0], $rr->{"max_hitpoints"}->[0];
		print "mp: ", $rr->{"moves"}->[0], " / ", $rr->{"max_moves"}->[0], "\t\tline: ", $rr->{"max_moves"}->[1];
		printf "\tfrom %s to %s\n", $rr->{"max_moves"}->[0], suggest_value($rr->{"max_moves"}->[0]);
	}
}

sub get_value($$$) {
    my $text = shift;
    my $lineno = shift;
    my $rr = shift;
    my $found = "";

    #print "gv: [$ln] => ";
    foreach my $tt (@token) {
        #my $pat = qr($tt);
        if ($text =~ m/^$tt=(.*)$/) {
            $found = $tt;
            my @tmp = ($1, $lineno);
            $rr->{$tt} = \@tmp;
            #$rr->{$lineno} = $text;
            #say "match: $tt => $1";
            last;
        }
    }
    return $found;
}

sub main()
{
	my $inf = "fuck";

    my $file = $ARGV[0] // $inf;
    list_unit($file);

    say "total unit count: $unit_count";
    say "no name count: $noname_count";
    say "error (not complete) count: $error_count";
    say "output count: $output_count";
}

main;
