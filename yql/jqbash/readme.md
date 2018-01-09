# readme for jqbash

In this folder, scripts demo how to read values from json file and use yahoo weather API to query woeid and related weather forecast.

* [input.json](./input.json) which defines parameters and input/output files

* [Makefile](./Makefile) performs all demos

* [query.sh](./query.sh) reads 'input.json' for latitude and longitude, and then query woeid and weather. It outputs "file.woeid" and "file.weather".

* [tj.sh](./tj.sh) demos how to use 'jq' and bash functions and output to another file. It outputs "file.tjoutput".

## running

```
$ make
```
If make says "nothing to be done", touch input.json and then "make".

## clean intermediate files
```
$ make clean
```

## example content of 'input.json'
```json
{
    "input": {
        "latitude": 37.331932,
        "longtitude": -122.030146
    },
    "file": {
        "woeid": "woeid.json",
        "weather": "weather.json",
        "tjoutput": "tjout.json"
    }
}
```
