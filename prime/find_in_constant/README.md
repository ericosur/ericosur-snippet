# README

- [Finding the First 10-digit Prime in (a Billion) Digits of e](https://www.hanshq.net/eprime.html)

```bash
curl -s https://apod.nasa.gov/htmltest/gifcity/e.2mil | tr -d '[:space:]' | \
          perl -MMath::Prime::Util=is_prime -MList::Util=first -nle \
          'print first { is_prime($_) } /(?=([1-9]\d{9}))/g'
```
