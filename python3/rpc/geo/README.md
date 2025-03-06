# Readme

## api key

To request [API key](https://github.com/google/open-location-code/blob/main/Documentation/Reference/plus.codes_Website_API.md)

> updated on Mar 6 2025

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
  "key": "8Kr54rKYBj8l8DcTxRj7NkvGUF4M41bPX3ZmmFZX7XoZlsg",
  "status": "OK"
}
```
