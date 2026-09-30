# HOWTO


## read image from URL in python

https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url-in-python


```python
from PIL import Image
import requests

im = Image.open(requests.get(url, stream=True).raw)
```
