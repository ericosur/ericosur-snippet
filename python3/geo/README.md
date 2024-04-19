# Readme

## api key

to request [API key](https://github.com/google/open-location-code/wiki/Plus-codes-API#api-keys)

## geo.py

- check [geo.py](./geo.py)

### denied

At Dec 16 2019, current status:

```json
r.text: {
  "error_message": "You must enable Billing on the Google Cloud Project at https://console.cloud.google.com/project/_/billing/enable Learn more at https://developers.google.com/maps/gmp-get-started",
  "status": "REQUEST_DENIED"
}
```

### for plus.codes, encrypt geo api key request

```bash
curl https://plus.codes/api?encryptkey=abcdefkey
```

returns

```json
{
  "encryption_message": "Provide the key in the key= parameter in your requests",
  "key": "8Kr54rKYBj8l8DcTxRj7NkvG%2Fe%2FlwvEU%2F4M41bPX3Zmm%2FZX7XoZlsg%3D%3D",
  "status": "OK"
}
```
