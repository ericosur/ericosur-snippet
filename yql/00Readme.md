# yql samples

this sub directory contains several samples to query Yahoo weather:
  * bash
      * curl
      * output to all.json

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
