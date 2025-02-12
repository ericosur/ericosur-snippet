# README

crypto demo scripts

Use ```passutil.py``` to generate cipher/json for exchange.
Use ```decpu.py``` to decrypt/retrieve the plain text.

## passutil.py

- require "pycryptodome"
- encrypt
- decrypt

- key, ciphertext,
- cn is cipher.nonce
- tag is
```json
{
    "key": "5BuB39jVhjqG+dikT7I6ED2iY6CdA5hmDoHKZyuEi80=",
    "cn": "cqc2MtpGaBIl4XN7m0vO2Q==",
    "tg": "DA0ObO7PQ8J61WBT0O+Ecg==",
    "ciphertext": "XYMOuxx08RRIIGY="
}
```

## scrypt

- it is single way, not for symantric encrypt/decrypt
- use this for encrypting plain text password
- store password, salt, cipher text
