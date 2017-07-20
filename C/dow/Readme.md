# readme

refer to: [determination of the day of the week from wikimedia](https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week)

try to implement:
```c
        (d+=m<3?y--:y-2,23*m/9+d+4+y/4-y/100+y/400)%7
```
