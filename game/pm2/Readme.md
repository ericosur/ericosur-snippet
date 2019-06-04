# readme

script to read property data from save file of PM2

## input file

re of file name:
```
F\d{3}.GNX
```

for example
> F101.GNX

## output file

a.json


## extra address

still not verified

| position | description |
|------|---|-------------|
| 0x8C | father's name   |
| 0x74 | daughter's name |
| 0x00 | year |
| 0x02 | month |
| 0x06 | date |

## scripts

- show_gnx.py
- go_cmd.py
