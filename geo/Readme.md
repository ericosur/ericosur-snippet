# Readme

## api key

to request API key:
https://github.com/google/open-location-code/wiki/Plus-codes-API#api-keys


## migrate to python3

old geo.py
  - python2
  - urllib2

new geo.py
  - python3
  - **requests**

## for plus.codes, encrypt geo api key request

```
curl https://plus.codes/api?encryptkey=abcdefkey
```
returns
```
{
  "encryption_message": "Provide the key in the key= parameter in your requests",
  "key": "8Kr54rKYBj8l8DcTxRj7NkvG%2Fe%2FlwvEU%2F4M41bPX3Zmm%2FZX7XoZlsg%3D%3D",
  "status": "OK"
}
```
