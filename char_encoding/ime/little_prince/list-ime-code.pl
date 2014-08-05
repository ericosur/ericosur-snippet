#!/usr/bin/perl

=pod

This script comes from count-cin.pl to count some numbers from cin files.
I extended it to:
1. load all IME code combination from cin file
2. load file content
3. list with IME code

=cut

use strict;
use v5.10;
use Storable;
use Encode qw(from_to);
use Data::Dump qw(dump);
use utf8;

my $storage_file = "hashvalue.dat";

sub sep()
{
	say '-' x 50;
}

sub parse_cin($)
{
	my $local_debug = 0;
    my $arg = shift;
    my $flag;
    my $cnt;
    # %left is ime combination
    # %right is character
    # in IME, we input ime combination, eg 'HG', IME will output '麵'
    my (%left, %right) = ();
    my @files = ($arg);

    foreach my $ff (@files)  {
    	next if not -e $ff;
    	print "read from $ff\n";
    	open my $ifh, $ff or die "$!";
    	binmode($ifh, ":utf8");	# read it as utf8 encoding
    	$flag = 0;
    	$cnt = 0;
    	%left = ();
    	%right = ();
    	while (<$ifh>)  {
    		next if m/^#/;
    		my $line = $_;
=pod
    		if ( $line =~ m/%cname\s+(.*)/ )  {
    			print "ime name: $1\t";
    		}
=cut
    		if ( $line =~ m/%chardef\s+begin/ )  {
    			$flag = 1;
    			print "begin\n" if ($local_debug);
    			next;
    		}
    		if ($flag == 1)  {
    			++ $cnt;
    			$line =~ m/^(\w+)\s+(.*)/;
    			if ($1) {
    			    $left{$1} ++;
    			}
    			if ($2) {
    				my $cp = ord($2);	# change it to codepoint number
    				printf("cp:%x ", $cp) if ($local_debug);
if (1) {
					# every chinese char has one or more key combination
					# store it as array
    			    if ($right{$cp}) {
    			        my $ref_rights = $right{$cp};
    			        push @$ref_rights, $1;
    			    } else {
    			        my @rights = ($1);
    			        $right{$cp} = \@rights;
    			    }
}
    		    }
    			next;
    		}
    		if ( $line =~ m/%chardef\s+end/ )  {
    			$flag = 0;
    			print "end\n" if ($local_debug);
    			next;
    		}
    	}	# loop to next file
    	close $ifh;
    	print "char def: $cnt\n";
    	print "unique in: ", scalar keys %left, "\t";
    	print "unique out: ", scalar keys %right, "\n";
    	sep();
		if ($local_debug) {
	    	mydump(\%left);
	    	sep();
	    	mydump(\%right);
	    	sep();
    	}
    }

    store(\%right, $storage_file);
    return \%right;
}

sub mydump($)
{
    my $rh = shift;
    my $total = 0;
    my @freq = ();

    for my $kk (keys(%$rh)) {
        ++$total;
        if ( ref $rh->{$kk} eq 'ARRAY' ) {
            $freq[0] ++;
            my $rarr = $rh->{$kk};
            my $code = scalar(@$rarr);
            $freq[$code] ++;
            if ($code > 12) {	# list char has more than 12 combination
                from_to($kk, "UTF8", "BIG5");
                print $kk," ";
                foreach (@$rarr) {
                    print $_," ";
                }
                print "\n";
            }
        } else { # scalar
            $freq[0] ++;
            # print keydef > 1
            my $len = length($kk);
        }
    }

    if ($freq[0] > 0) {
        for (my $i=0; $i<scalar(@freq); $i++)  {
            printf("freq[%d]: %d\n", $i, $freq[$i]);
        }
    }
}

# in: ref of word hash
# in: input file name
# in: output file name
sub process_file($$$)
{
	my $debug_pf = 0;
	my ($rrh, $ifile, $ofile) = @_;
	my $linecnt = 0;
	my $chrcnt = 0;
    my @longseq = ();

	open my $fh, $ifile or die;
	open my $ofh, "> $ofile" or die;
	binmode( $fh, ':utf8' );
	binmode( $ofh, ':utf8' );

	while ( <$fh> ) {
		++$linecnt;
		s/[\r\n]//;
		my $len = length($_);
		say "len: $len, $_" if $debug_pf;

        # print original text
		#print $ofh $_,"\n";

		my @liner = unpack("U*", $_);

        # print original text with spacing
		foreach my $uu (@liner)  {
			printf $ofh "%3s", chr($uu);
		}
        print $ofh "\n";

        # lookup cin table and print codes
		foreach my $ww (@liner) {
			my $res = lookup_table($rrh, $ww);
			if ($res) {
				printf $ofh "%4s", $res;
                if (length($res) >= 4)  {
                    push(@longseq, $res);
                }
			} else {
				printf $ofh "%3s", chr($ww);
			}
		}
		$chrcnt += $len;

		if ($debug_pf) {
			last if $linecnt > 0;
		}
		print $ofh "\n\n";
	}
	close($fh);
	close($ofh);

    sep();
    print "In this article, there 4-code characters:\n";
    foreach my $ss (@longseq) {
        printf "%5s", $ss;
    }
    print "\n";
}

# in: ref of word hash
# in: look char in codepage (integer)
sub lookup_table($$)
{
	my $debug_lt = 0;
	my ($rrh, $word) = @_;
	my $res = "";

	if ($rrh->{$word}) {
		if (ref $rrh->{$word} eq 'ARRAY') {
			#dump($rrh->{$word});
			$res = find_shortest($rrh->{$word});
			say "res: $res" if $debug_lt;
		} else {
			say "not array?";
		}
	} else {
		printf("%x not found?\n", $word) if ($debug_lt);
	}
	return $res;
}

# in: ref of array
sub find_shortest($)
{
	my $rar = shift;
	my $len = 0;
	my $i;
	my ($minlen, $minchr) = (999,"");	# set $minlen as a large number
	foreach (@$rar) {
		$len = length($_);
		if ($len < $minlen) {
			$minlen = $len;
			$minchr = $_;
		}
	}
	return $minchr;
}

sub main()
{
	my $rrh;

	my $ifile = $ARGV[0] // 'littleprince.txt';
	my $ofile = 'output.txt';
	my $cin = 'boshiamy_t.cin';

    if (-e $storage_file) {
		$rrh = retrieve($storage_file);
    } else {
        $rrh = parse_cin($cin);
    }

=pod
if (1) {
    lookup_table($rrh, 0x9eb5);
}
=cut
	say "read: $ifile";
	say "out: $ofile";
    process_file($rrh, $ifile, $ofile);

}

main();
