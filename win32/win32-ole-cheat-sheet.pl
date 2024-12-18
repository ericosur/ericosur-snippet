#
# perl Win32::OLE cheat sheet
#
# from: http://www.tek-tips.com/faqs.cfm?fid=6715

use OLE;
use Win32::OLE::Const "Microsoft Excel";

###################################################################################################################################

#___ DEFINE EXCEL

$excel = CreateObject OLE "Excel.Application";

#___ MAKE EXCEL VISIBLE

$excel -> {Visible} = 1;

#___ ADD NEW WORKBOOK

$workbook = $excel    -> Workbooks -> Add;
$sheet    = $workbook -> Worksheets("Sheet1");
$sheet                -> Activate;

#___ OPEN EXISTING WORKBOOK

$workbook = $excel    -> Workbooks -> Open("$file_name");
$sheet    = $workbook -> Worksheets(1) -> {Name};
$sheet    = $workbook -> Worksheets($sheet);
$sheet                -> Activate;

#___ ACTIVATE EXISTING WORKBOOK

$excel -> Windows("Book1") -> Activate;
$workbook = $excel    -> Activewindow;
$sheet    = $workbook -> Activesheet;

#___ CLOSE WORKBOOK

$workbook -> Close;

#___ ADD NEW WORKSHEET

$workbook -> Worksheets -> Add({After => $workbook -> Worksheets($workbook -> Worksheets -> {Count})});

#___ CHANGE WORKSHEET NAME

$sheet -> {Name} = "Name of Worksheet";

#___ PRINT VALUE TO CELL

$sheet -> Range("A1") -> {Value} = 1234;

#___ SUM FORMULAS

$sheet -> Range("A3") -> {FormulaR1C1} = "=SUM(R[-2]C:R[-1]C)";                # Sum rows
$sheet -> Range("C1") -> {FormulaR1C1} = "=SUM(RC[-2]:RC[-1])";                # Sum columns

#___ RETRIEVE VALUE FROM CELL

$data = $sheet -> Range("G7") -> {Value};

#___ FORMAT TEXT

$sheet -> Range("G7:H7") -> Font -> {Bold}       = "True";
$sheet -> Range("G7:H7") -> Font -> {Italic}     = "True";
$sheet -> Range("G7:H7") -> Font -> {Underline}  = xlUnderlineStyleSingle;
$sheet -> Range("G7:H7") -> Font -> {Size}       = 8;
$sheet -> Range("G7:H7") -> Font -> {Name}       = "Arial";
$sheet -> Range("G7:H7") -> Font -> {ColorIndex} = 4;

$sheet -> Range("G7:H7") -> {NumberFormat} = "\@";                             # Text
$sheet -> Range("A1:H7") -> {NumberFormat} = "\$#,##0.00";                     # Currency
$sheet -> Range("G7:H7") -> {NumberFormat} = "\$#,##0.00_);[Red](\$#,##0.00)"; # Currency - red negatives
$sheet -> Range("G7:H7") -> {NumberFormat} = "0.00_);[Red](0.00)";             # Numbers with decimals
$sheet -> Range("G7:H7") -> {NumberFormat} = "#,##0";                          # Numbers with commas
$sheet -> Range("G7:H7") -> {NumberFormat} = "#,##0_);[Red](#,##0)";           # Numbers with commas - red negatives
$sheet -> Range("G7:H7") -> {NumberFormat} = "0.00%";                          # Percents
$sheet -> Range("G7:H7") -> {NumberFormat} = "m/d/yyyy"                        # Dates

#___ ALIGN TEXT

$sheet -> Range("G7:H7") -> {HorizontalAlignment} = xlHAlignCenter;            # Center text;
$sheet -> Range("A1:A2") -> {Orientation} = 90;                                # Rotate text

#___ SET COLUMN WIDTH/ROW HEIGHT

$sheet -> Range('A:A') -> {ColumnWidth} = 9.14;
$sheet -> Range("8:8") -> {RowHeight}   = 30;
$sheet -> Range("G:H") -> {Columns} -> Autofit;

#___ FIND LAST ROW/COLUMN WITH DATA

$last_row = $sheet -> UsedRange -> Find({What => "*", SearchDirection => xlPrevious, SearchOrder => xlByRows})    -> {Row};
$last_col = $sheet -> UsedRange -> Find({What => "*", SearchDirection => xlPrevious, SearchOrder => xlByColumns}) -> {Column};

#___ ADD BORDERS

$sheet -> Range("A3:I3") -> Borders(xlEdgeBottom)       -> {LineStyle}  = xlDouble;
$sheet -> Range("A3:I3") -> Borders(xlEdgeBottom)       -> {Weight}     = xlThick;
$sheet -> Range("A3:I3") -> Borders(xlEdgeBottom)       -> {ColorIndex} = 1;
$sheet -> Range("A3:I3") -> Borders(xlEdgeLeft)         -> {LineStyle}  = xlContinuous;
$sheet -> Range("A3:I3") -> Borders(xlEdgeLeft)         -> {Weight}     = xlThin;
$sheet -> Range("A3:I3") -> Borders(xlEdgeTop)          -> {LineStyle}  = xlContinuous;
$sheet -> Range("A3:I3") -> Borders(xlEdgeTop)          -> {Weight}     = xlThin;
$sheet -> Range("A3:I3") -> Borders(xlEdgeBottom)       -> {LineStyle}  = xlContinuous;
$sheet -> Range("A3:I3") -> Borders(xlEdgeBottom)       -> {Weight}     = xlThin;
$sheet -> Range("A3:I3") -> Borders(xlEdgeRight)        -> {LineStyle}  = xlContinuous;
$sheet -> Range("A3:I3") -> Borders(xlEdgeRight)        -> {Weight}     = xlThin;
$sheet -> Range("A3:I3") -> Borders(xlInsideVertical)   -> {LineStyle}  = xlContinuous;
$sheet -> Range("A3:I3") -> Borders(xlInsideVertical)   -> {Weight}     = xlThin;
$sheet -> Range("A3:I3") -> Borders(xlInsideHorizontal) -> {LineStyle}  = xlContinuous;
$sheet -> Range("A3:I3") -> Borders(xlInsideHorizontal) -> {Weight}     = xlThin;

#___ PRINT SETUP

$sheet -> PageSetup -> {Orientation}  = xlLandscape;
$sheet -> PageSetup -> {Order}        = xlOverThenDown;
$sheet -> PageSetup -> {LeftMargin}   = .25;
$sheet -> PageSetup -> {RightMargin}  = .25;
$sheet -> PageSetup -> {BottomMargin} = .5;
$sheet -> PageSetup -> {CenterFooter} = "Page &P of &N";
$sheet -> PageSetup -> {RightFooter}  = "Page &P of &N";
$sheet -> PageSetup -> {LeftFooter}   = "Left\nFooter";
$sheet -> PageSetup -> {Zoom}         = 75;
$sheet -> PageSetup -> FitToPagesWide = 1;
$sheet -> PageSetup -> FitToPagesTall = 1;

#___ ADD PAGE BREAK

$excel -> ActiveWindow -> SelectedSheets -> HPageBreaks -> Add({Before => $sheet -> Range("3:3")});

#___ HIDE COLUMNS

$sheet -> Range("G:H") -> EntireColumn -> {Hidden} = "True";

#___ MERGE CELLS

$sheet -> Range("H10:J10") -> Merge;

#___ INSERT PICTURE

$sheet -> Pictures -> Insert("picture_name");                # Insert in upper-left corner
$excel -> ActiveSheet -> Pictures -> Insert("picture_name"); # Insert in active cell

#___ GROUP ROWS

$sheet -> Range("7:8") -> Group;

#___ ACTIVATE CELL

$sheet -> Range("A2") -> Activate;

#___ FREEZE PANES

$excel -> ActiveWindow -> {FreezePanes} = "True";

#___ DELETE SHEET

$sheet -> Delete;

#___ SAVE AND QUIT

$excel    -> {DisplayAlerts} = 0; # This turns off the "This file already exists" message.
$workbook -> SaveAs ("C:\\file_name.xls");
$excel    -> Quit; 
 