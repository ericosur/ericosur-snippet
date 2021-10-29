#!/usr/bin/python3.6
# coding: utf-8

'''
凱基下載的未實現損益的 xls 其實是個不太完整的 html table,
這個 script 會轉換 encoding (big5 to utf8), parse html, 輸出成
  - CSV (預設模組)
  - XLS (excel 2010), 需要 xlsxwriter 模組
    > 以 excel 格式輸出的話, 會自動填入公式以及作格式設定
'''

import csv
from datetime import date
from decimal import Decimal
import locale
import os
import sys
from typing import List

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('use pip install beautifulsoup4')
    print('use pip install lxml')
    sys.exit(1)

XLSWRITER_OK = False
try:
    import xlsxwriter
    XLSWRITER_OK = True
except ImportError:
    print('cannot import module xlsxwriter')
    sys.exit(1)


def conv_big5_to_utf8(fn: str) -> str:
    ''' convert input file encoding from big5 to utf8,
        output content as str
    # iconv -f BIG-5 -t UTF-8 un0304.xls > u.html
    # or *_*uconv*_*
    cmd = 'iconv -f BIG-5 -t UTF-8 {} > {}'.format(in_fn, out_fn)
    os.system(cmd)
    '''
    c = None
    with open(fn, 'rb') as f:
        c = f.read()
    #print(c)
    d = c.decode('big5').encode('utf-8')
    utf8 = d.decode('utf-8')    # str in utf-8 encoding
    return utf8

def make_soup(content: str) -> List:
    ''' make soup from content '''
    def remove_some_col(data: List) -> List:
        ''' remove col#2, col#-1, col#-2 '''
        t = []
        t.extend(data[0:2])
        t.extend(data[3:-2])
        return t
    data = []
    soup = BeautifulSoup(content, 'lxml')
    t = soup.find('table', attrs={'class':'tablesorter'})
    header = t.find('tr', attrs={'class':'tablebg0'})
    ths = header.find_all('th')
    header_line = [tt.text for tt in ths]
    #print(header_line)
    data.append(remove_some_col(header_line))

    rows = t.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cells = [ele.text.strip() for ele in cols]
        if cells:
            #data.append([ele for ele in cells if ele])
            #print(type(cells))
            data.append(remove_some_col(cells))
    return data

def get_datetag() -> str:
    ''' string in UYYMMDD '''
    today = date.today()
    yy = today.year - 2000
    s = f'U{yy:02d}{today.month:02d}{today.day:02d}'
    return s

def output_csv(data: List) -> None:
    ''' output data as csv format in UMMDD.csv '''
    fn = get_datetag() + '.csv'
    print('[INFO] output to:', fn)
    with open(fn, 'wt', encoding='utf8') as csvfile:
        sw = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
        for dd in data:
            sw.writerow(dd)

class XlsFormat():
    ''' formats of workbook '''
    def __init__(self, wb):
        # 1,234 if negative, show (2,468) in red
        self.currency_format = wb.add_format({'num_format': '#,##0_);[Red](#,##0)'})
        # 1234.56 if negative, show -1234.56 in red
        self.rate_format = wb.add_format({'num_format': '0.00;[Red]-0.00'})
        # 2.46%
        self.percent_format = wb.add_format({'num_format': '0.00%'})
        # 1,234.56
        self.decimal_format = wb.add_format({'num_format': '#,##0.00'})
        # normal text, center align
        self.item_format = wb.add_format({'num_format': '@', 'align': 'center'})
        # normal text, align default (left align?)
        self.text_format = wb.add_format({'num_format': '@'})
        # bold, and hcenter, vcenter
        self.head_format = wb.add_format({'bold': True, 'align': 'center',
                                          'valign': 'vcenter'})

def to_currency(v: str) -> Decimal:
    ''' convert str to Decimal according to locale, return "" if empty
        eg: "1,234,567.89" to 1234567.89
    '''
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    r = ""
    try:
        r = Decimal(locale.atof(v))
    except ValueError:
        #print('Value Error on:', v)
        pass
    return r

def to_float(v: str) -> float:
    ''' convert str to float, return "" if empty '''
    r = ""
    try:
        r = float(v)
    except ValueError:
        #print('Value Error on:', v)
        pass
    return r

# pylint: disable=consider-using-f-string
def output_xls(data: List) -> None:
    ''' using xlsxwriter to output '''
    fn = get_datetag() + '.xls'
    print('[INFO] output to:', fn)
    wb = xlsxwriter.Workbook(fn)
    x = XlsFormat(wb)
    ws = wb.add_worksheet(get_datetag())

    i = 0
    for i, d in enumerate(data):
        if i == 0:
            ws.write_row(i, 0, d, x.head_format)
        else:
            ws.write(i, 0, d[0], x.item_format)
            ws.write(i, 1, d[1], x.text_format)
            ws.write(i, 2, to_currency(d[2]), x.currency_format)
            ws.write(i, 3, to_float(d[3]), x.decimal_format)
            ws.write(i, 4, to_currency(d[4]), x.currency_format)
            ws.write(i, 5, to_currency(d[5]), x.currency_format)
            ws.write(i, 6, to_currency(d[6]), x.currency_format)
            ws.write(i, 7, to_float(d[7]), x.rate_format)
            ws.write(i, 8, to_float(d[8]), x.decimal_format)

    # insert formula into table, will update in Excel and google spreadsheet
    # will not re-calculate in libre-office
    ws.write_formula(i, 2, "=SUM(C2:C{})".format(i), x.currency_format)
    ws.write_formula(i, 3, "=E{0}/C{0}".format(i+1), x.decimal_format)
    ws.write_formula(i, 4, "=SUM(E2:E{})".format(i), x.currency_format)
    ws.write_formula(i, 5, "=SUM(F2:F{})".format(i), x.currency_format)
    ws.write_formula(i, 6, "=F{0}-E{0}".format(i+1), x.currency_format)
    ws.write_formula(i, 7, "=G{0}/E{0}".format(i+1), x.percent_format)

    # it's ARRAYFORMULA in excel format
    f = "{=SUM(ROUNDDOWN(C2:" + "C{}".format(i) + "/1000))}"
    ws.write_formula(i+1, 2, f, x.currency_format)
    ws.write_formula(i+1, 4, "=E{0}/C{0}".format(i+1), x.decimal_format)
    ws.write_formula(i+1, 5, "=F{0}/C{0}".format(i+1), x.decimal_format)
    ws.write_formula(i+1, 6, "=G{0}/C{0}".format(i+1), x.decimal_format)

    ws.set_column('B:B', 14) # width of column
    ws.set_column('E:G', 10) # width of column

    wb.close()


def main(argv: List) -> None:
    ''' main '''
    in_fn = None
    if argv == []:
        in_fn = '證券_未實現損益.xls'
    else:
        in_fn = argv[0]
    if not os.path.exists(in_fn):
        print('[ERROR] input file not found:', in_fn)
        sys.exit(1)

    #print('[INFO] input from:', in_fn)
    # html download from KGI is encoded as BIG-5, need transcoding to UTF-8
    utf8 = conv_big5_to_utf8(in_fn)
    # parsing html and store into list()
    data = make_soup(utf8)
    #output_csv(data)
    if XLSWRITER_OK:
        output_xls(data)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main([])
