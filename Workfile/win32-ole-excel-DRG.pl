#!/usr/bin/perl
#
# this script is to do copy/paste cells to another work sheet
# to deal with brain damage ¤¤¥¡°·«O§½ DRG excel table
#
# MUST:
# necessary module installed like Win32::*
# microsoft excel (OS need to be MS-Windows)
#

# reference: http://www.perlmonks.org/?node=153486

use strict;

use Win32::OLE qw(in with);
use Win32::OLE::Const 'Microsoft Excel';
use Win32::OLE::Variant;
use Win32::OLE::NLS qw(:LOCALE :DATE);

$Win32::OLE::Warn = 3; # Die on Errors.
# ::Warn = 2; throws the errors, but #
# expects that the programmer deals  #

my $excelfile = ".\\book.xls";

my $Excel = Win32::OLE->GetActiveObject('Excel.Application')
        || Win32::OLE->new('Excel.Application', 'Quit');

$Excel->{DisplayAlerts}=0;

#my $Book = $Excel->Workbooks->Add();
#$Book->SaveAs($excelfile); #Good habit when working with OLE, save often.

my $Book = $Excel->Workbooks->Open($excelfile);
my $sheet1 = $Book->Worksheets("from");
my $sheet2 = $Book->Worksheets("to");

$sheet2->Activate();
#$sheet2->{Name} = "sheet2"; # to rename the sheet
#$sheet2->Range("a1")->{Value} = "test value";

my $min = 1;
my $max = 29999;    # the last row to fetch
my $from_cell;
my $to_cell;
my $to_cnt = 1;

LOOP:
for (my $i=1; $i<=$max; ++$i)  {
    $from_cell = "A" . $i;  # from A1 to A29999
    my $drg_value = $sheet1->Range($from_cell)->{Value};

    if ($drg_value =~ /^DRG\d+-DRG\d+/)  {  # do not want it
        print "[DROP]: $drg_value\n";
        next LOOP;
    }
    elsif ($drg_value =~ /^DRG/)  {
        # DRG12345
        $to_cell = "A" . $to_cnt;
        $sheet2->Range($to_cell)->{Value} = $drg_value;
        #print $drg_value,"\n";

        # chinese name
        $from_cell = "B" . $i;
        my $ch_name = $sheet1->Range($from_cell)->{Value};
        $to_cell =~ s/A/B/;
        $sheet2->Range($to_cell)->{Value} = $ch_name;

        # english name
        $from_cell = sprintf("B%d", $i+1);
        my $en_name = $sheet1->Range($from_cell)->{Value};
        $to_cell =~ s/B/C/;
        $sheet2->Range($to_cell)->{Value} = $en_name;

        $to_cnt ++;
    }

}

print "item copied: ", ($to_cnt-1),"\n";
$Book->SaveAs($excelfile);
