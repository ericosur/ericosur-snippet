#!/usr/bin/perl

while (<DATA>) {
 if ( m/(http:\/\/10.193.95.212\/cts\/)(\w+)\/(\d{4}\.\d\d\.\d\d_\d\d\.\d\d\.\d\d)/ ) {
  my ($url, $prj, $dateid) = ($1, $2, $3);
  my $ofile = sprintf("%s-%s.zip", $prj, $dateid);
  my $cmd = sprintf("curl -o %s %s%s/%s/%s.zip", $ofile, $url, $prj, $dateid, $dateid);
  print $cmd,"\n";
  system $cmd;
  $cmd = sprintf("unzip %s -d %s-%s", $ofile, $prj, $dateid);
  system $cmd;
 }
}

__DATA__
http://10.193.95.212/cts/sphinx/2012.03.28_02.42.42/2012.03.28_02.42.42/2012.03.28_02.42.42
http://10.193.95.212/cts/sphinx/2012.03.28_11.01.57/2012.03.28_11.01.57/2012.03.28_11.01.57
http://10.193.95.212/cts/titan/2012.03.28_04.07.58/2012.03.28_04.07.58/2012.03.28_04.07.58
http://10.193.95.212/cts/titan/2012.03.28_11.46.03/2012.03.28_11.46.03/2012.03.28_11.46.03
http://10.193.95.212/cts/titan/2012.03.28_11.27.55/2012.03.28_11.27.55/2012.03.28_11.27.55