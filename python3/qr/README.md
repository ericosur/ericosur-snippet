# README

qrcode related

## issue

This character

```
han character: 輸
         utf8: e8 bc b8
```

generated by ```genqr.py```

- NG:
	- [zbarlight_test.py](file://./zbarlight_test.py) decode this qrcode image incorrectly.
	- pixel6a camera (android 14)
- OK:
	- iphone qrcode scanner (iOS 18.0.1)
	- ```zbarimg```

> zbarimg is not suitable to process qrcode image captured in real world. Usu. camera app will handle the physical captured image better.


## module that generate barcode/qrcode

```bash
pip install treepoem
```

## qrcode related

### generation

- qrcode
- segno

```python -m pip install segno```

```python
import segno
qrcode = segno.make_qr("hello world")
qrcode.save("qrcode.png", scale=5)
```

### view

ImageMagick view: ```magick display qrcode.png```

### decode

- zbar-tools

```
apt intall zbar-tools

zbarimg -q qrcode.png
QR-Code:hello world
```

### totp

- mintotp (https://github.com/susam/mintotp.git)

```
otpauth://totp/GitHub:LarryLuTW?secret=X5CTBOMEYE3TXIIS

zbarimg -q secret1.png | sed 's/.*secret=\([^&]*\).*/\1/' | ./mintotp.py
```
