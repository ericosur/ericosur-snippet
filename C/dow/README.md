# readme

## description

refer to: [determination of the day of the week from wikimedia](https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week)

try to implement:
```c
        (d+=m<3?y--:y-2,23*m/9+d+4+y/4-y/100+y/400)%7
```

## note

This equation is only valid for the date later than (1752, 9, 14).

```LC_ALL=en_US.UTF-8 cal -d 1752-9```
```
   September 1752
Su Mo Tu We Th Fr Sa
       1  2 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
```
