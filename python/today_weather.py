#!/usr/bin/python
# -*- coding: utf-8 -*-

# copy from:
# http://ez2learn.com/index.php/python-tutorials/python-examples/178-yahoo

import urllib

# 抓取Yahoo!奇摩天氣的網頁內容放到WebContent
weatherWeb = urllib.urlopen("http://tw.weather.yahoo.com/today.html")
webContent = weatherWeb.read().decode('utf_8')
weatherWeb.close()

import HTMLParser

# 用來解析台中地區天氣資訊的解析器，繼承自HTMLParser
class WeaterHTMLParser(HTMLParser.HTMLParser):

    def handle_data(self, data):
        """處理標籤以外的資料，也就是網頁中的文字"""

        data = data.strip()

        # 如果台中地區已出現過，就記錄天氣資訊
        if hasattr(self, 'found') and data:
            # 到了彰化地區，中止解析
            if data == u'彰化地區':
                self.stop = True
                return
            self.weather.append(data)

        # 出現台中地區
        # 設定旗標以通知後面幾次呼叫記下資訊
        if data == u'台中地區':
            self.found = True
            self.weather = []
            self.weather.append(data)

    def unknown_decl(self, data):
        """Override unknown handle method to avoid exception"""
        pass

Parser = WeaterHTMLParser()

try:
    # 將網頁內容拆成一行一行餵給Parser
    for line in webContent.splitlines():
        # 如果出現停止旗標，停止餵食資料，並且跳出迴圈
        if hasattr(Parser, 'stop') and Parser.stop:
            break
        Parser.feed(line)
except HTMLParser.HTMLParseError, data:
    print "# Parser error : " + data.msg

Parser.close()

print u"%s 的今天氣是 %s，氣溫是 %s度%s，降雨機率是 %s" % tuple(Parser.weather)
#print "Press enter to continue."
#raw_input()
