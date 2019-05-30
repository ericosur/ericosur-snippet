# yql samples

## NOTE

Important EOL Notice: As of Thursday, Jan. 3, 2019, the weather.yahooapis.com and query.yahooapis.com for Yahoo Weather API will be retired.
To continue using our free Yahoo Weather APIs, use https://weather-ydn-yql.media.yahoo.com/forecastrss. Follow below instructions to get credentials and onboard to this free Yahoo Weather API service.

## description

this sub directory contains several samples to query Yahoo weather:
  * bash
      * curl
      * jq
      * query woeid, weather

  * python
      * urllib, urllib2, json
      * [yql.py](./yql.py) just query one field
      * [woeid.py](./woeid.py) predefined some latitude/longitude locations, demo:
        * how to query woeid by latitude/longitude
        * basic query weather by using woeid
        * use sub select statement, query woeid by lat/long also query weather

  * javascript
      * yql
      * showing forecasts
