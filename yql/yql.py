#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from: http://57life.blogspot.tw/2012/12/msn-yahoo.html
# 20070568   台北 (台北市內湖區)

import urllib2, urllib, json

woeid = '20070568'

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select wind from weather.forecast where woeid=" + woeid
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
print data['query']['results']
