#!/usr/bin/env python
# -*- coding: utf-8 -*-

# use yql to query yahoo weather
# to get pretty output:
# ./yql.py|python -m json.tool
#
# from: http://57life.blogspot.tw/2012/12/msn-yahoo.html
# 20070568   台北 (台北市內湖區)

import urllib2, urllib, json

def print_tips():
    print("you may use './yql.py | python -m json.tool' to get pretty format\n")

def query_weather():
    woeid = '20070568'
    city_name = 'Taipei'
    #condition = 'item.condition'
    condition = 'astronomy'
    baseurl = "https://query.yahooapis.com/v1/public/yql?"

    tmp = '''
        select {0} from weather.forecast where woeid in (select woeid
        from geo.places(1) where text =\'{1}\') and u=\'c\'
    '''.format(condition, city_name)
    yql_query = tmp.strip()

    yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
    result = urllib2.urlopen(yql_url).read()
    data = json.loads(result)

    # DO NOT use this
    # need more string processing for further json usage, not good output
    #print data['query']['results']

    # use this:
    print json.dumps(data['query']['results'])


if __name__ == '__main__':
    query_weather()
