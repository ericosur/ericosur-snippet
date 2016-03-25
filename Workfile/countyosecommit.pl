#!/usr/bin/env perl

use strict;

# run git-log and output to $f
my $f = 'y.txt';
chdir "/src/gmui_git/yosemite/YOSE_GUI/";
system "git log --format='%an' --no-merges > $f";

# read commit author names
my $cnt = 0;
open my $fh, $f or die;
my %val = ();
while (<$fh>) {
    ++ $cnt;
    # dirty hacks for some weird names
	s/[\r\n\"“”]//g;
    s/ernest/Ernest_Liao/;
    s/unknown/Cid Huang/;
    s/ericosur/Rasmus_Lai/;
	if ( m/^(.*)$/ ) {
		$val{$1} ++;
	}
}
close $fh;
print STDERR "cnt: $cnt\n";
unlink $f;

# $result would be json style data array
my $sum = 0;
my $result;
foreach my $k (sort { $val{$b} <=> $val{$a} }keys %val) {
	my $oneline = sprintf("          ['%s (%d)', %d],\n", $k, $val{$k}, $val{$k});
    #print $oneline;
    $result = $result . $oneline;
    $sum = $sum + $val{$k};
}
print STDERR "sum: $sum\n";

# output to the result HTML
my $of = "output.html";
my $date = `/bin/date`;
$date =~ s/[\r\n]//g;
my $title = "Yosemite UI Commits " . $date;
open my $ofh, "> $of" or die;
while (<DATA>) {
    if ( m/REALDATAINSERTHERE/ ) {
        print $ofh $result;
    } elsif ( m/PIECHARTTITLE/ ) {
        print $ofh "          title: '$title'\n";
    } else {
        print $ofh $_;
    }
}
close $ofh;
print "output to $of\n";

__DATA__
<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Name', 'Commit Number'],
          REALDATAINSERTHERE
        ]);

        var options = {
          PIECHARTTITLE
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="piechart" style="width: 900px; height: 500px;"></div>
  </body>
</html>
