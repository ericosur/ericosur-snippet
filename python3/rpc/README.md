# README

## python json rpc

* data generation:
  Calling json-rpc API from <https://random.org> by module *requests*.
* [google sheet to draw chart](https://www.benlcollins.com/spreadsheets/histogram-in-google-sheets/)
* [data sheet and chart](https://docs.google.com/spreadsheets/d/1yi2goF-OSH_rKFlH2_A7yfTvG3HU46xLPHsHz1wlOj4/edit#gid=1453399585)

## scripts and data files

* [concat.py](./concat.py)
  read *resp?.json* and output result into *data.txt*

* [dogapi.py](./dogapi.py)
  call dog api and download image from [dog api](https://dog.ceo/api/breeds/image/random)

* [fetch_pi.py](./fetch_pi.py)
  fetch pi digits from [pi delivery](https://api.pi.delivery/v1/pi)

* [req_guassian.py](./req_guassian.py)
  call [random.org](https://www.random.org/) API *generateGaussians* with parameter
  mean = 100, stdev = 15, 1000 numbers

* [req_random_int.py](./req_random_int.py)
  call [random.org](https://www.random.org/) API to simulate rolling a dice (1 to 6)

* [validate_gaussian.py](./validate_gaussian.py)
  read *data.txt* and calculate mean, median, stdev
  and try-and-error to test how many numbers to figure out it is a normal distribution

* [getapikey.py](./getapikey.py)
  common function to fetch API key of [random.org](https://www.random.org/)

* [getimgur.py](./getimgur.py)
  download image from imgur

## web api

* <https://aa.usno.navy.mil/data/docs/api.php#phase>
* <https://opendata.cwb.gov.tw/index>
