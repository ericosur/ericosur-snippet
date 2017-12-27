#!/usr/bin/env python

output_file = 'weather.json'

import urllib2, urllib, json
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid=90717580"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)

#print data['query']['results']

import json
with open(output_file, 'w') as outfile:
    json.dump(data, outfile)

# yql_url you may paste it at browser and get the json result
print("yql:\n{0}".format(yql_url))

print("output json result to {0}".format(output_file))
