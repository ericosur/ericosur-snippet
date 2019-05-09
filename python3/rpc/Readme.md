# python json rpc

* data generation:
  Calling json-rpc API from https://random.org by module *requests*.

* google sheet to draw chart
  https://www.benlcollins.com/spreadsheets/histogram-in-google-sheets/

* [data sheet and chart](https://docs.google.com/spreadsheets/d/1yi2goF-OSH_rKFlH2_A7yfTvG3HU46xLPHsHz1wlOj4/edit#gid=1453399585)


## existed files

* resp?.json (request and save) **NOT IN GIT**
  previously fetched results from *req-guassian.py*,
  responsed json rpc result

* data.txt (generated) **NOT IN GIT**
  one number one line text format

* req-guassian.py
  call random.org API *generateGaussians* with parameter
  mean = 100, stdev = 15, 1000 numbers

* req-random-int.py
  call random.org API to simulate rolling a dice (1 to 6)

* wtf.py
  read *data.txt* and calculate mean, median, stdev

* concat.py
  read *resp?.json* and output result into *data.txt*
