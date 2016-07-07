Record Temperature
==================

Hardware
--------

raspberry pi 2B + DHT11 module attached at pin #2(+5V), #6(GND), #12(GPIO#18)

DHT11 module will measure temperature and Humidity.


Software
--------

### Prepare ###

Needed packages:
```
sudo apt-get install build-essential python-dev
```

Fetch [Adafruit Python DHT][1] from github.

Fetch [Dropbox uploader][4] from github, need configure for your own dropbox account/permission.

### Usage ###

Crontab of root will run [callDHT11.sh][2] periodically, which calls [AdafruitDHT.py][3] and write results into __data.log__.

And calls [upload-log.sh][5] to upload __data.log__ to preset Dropbox account/folder.

Perl script [convLogCsv.pl][6] will re-organize __data.log__ into a CSV format file.

------------------------------------------------------------------

[1]: https://github.com/adafruit/Adafruit_Python_DHT
[2]: ./callDHT11.sh
[3]: https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py
[4]: https://github.com/andreafabrizi/Dropbox-Uploader
[5]: ./upload-log.sh
[6]: ./convLogCsv.pl
