# weather api provider

If I don't want to pay...

* Yahoo weather
  * https://www.yahoo.com/news/weather/
    * hourly forecast
    * yahoo portal links
  * https://developer.yahoo.com/weather/documentation.html
    * no hour-level forecast
    * limited translations
  * public query without api key

* OpenWeatherMap
  * https://openweathermap.org/
  * need input location here
    * mapview weather (cannot get location automatically)
  * https://openweathermap.org/api
    * next 3 hour forecast
    * 33 translations

* AccuWeather
  * https://www.accuweather.com/
    * CM links
    * map view
  * https://developer.accuweather.com/
    * next 12/24/72/120 hour per hour forecast
    * translation api

* weather channel
  * https://www.wunderground.com/weather/api/?ref=twc

## compare

* all supports latitude/longitude to POI/location


| name | commercial usage | free usage |
|------|-------------|---------|
| yahoo weather | need request | Per IP limits: /v1/public/*: 2,000 calls per hour; /v1/yql/*: 20,000 calls per hour |
| open weather | 40-2000 USD/mo, 600-200K calls | 60 calls/min |
| accuweather | 25-500 USD/mo, extra fee if more calls | 50 calls/day |
