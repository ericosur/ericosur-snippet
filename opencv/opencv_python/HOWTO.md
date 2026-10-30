# HOWTO


## read image from URL in python

https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url-in-python


```python
import urllib.request

import cv2
import numpy as np

url = 'https://example.com/image.png'
with urllib.request.urlopen(url) as resp:
    img = cv2.imdecode(np.frombuffer(resp.read(), np.uint8), cv2.IMREAD_COLOR)
```
