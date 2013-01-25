#!/usr/bin/perl

sub do_avg($)
{
    my $sum = 0;
    my $cnt = 0;
    my $file = shift;
    open my $fh, $file or die;
    while (<$fh>) {
    	if ( m/(\d+\.\d+)/ ) {
    		#print $1,"\n";
    		$cnt ++;
    		$sum += $1;
    	}
    }
    close $fh;
    printf("avg=%.3f\n",$sum/$cnt);
}

sub main()
{
    do_avg("s1.txt");
    do_avg("s2.txt");
	do_avg("s3.txt");
	do_avg("s4.txt");
}

main;

