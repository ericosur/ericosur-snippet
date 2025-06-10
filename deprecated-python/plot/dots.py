#!/usr/bin/env python
#!/Users/ericosur/anaconda/bin/python

# Get this figure: fig = py.get_figure("https://plot.ly/~foo12345/6/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~foo12345/6/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="plot from API (6)", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~foo12345/6/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.offline as offplot
#import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np

#py.sign_in('username', 'api_key')
#
y1 = np.random.randn(100)*10+22
y2 = np.random.randn(100)*33

trace1 = {
  "y": y1,
  "boxpoints": "all",
  "jitter": 0.3,
  "name": 'blue',
  "type": "box"
}
trace2 = {
  "y": y2,
  "boxpoints": "all",
  "jitter": 0.3,
  "name": 'orange',
  "type": "box"
}
data = Data([trace1, trace2])
layout = {
  "plot_bgcolor": "rgb(233,233,233)",
  "showlegend": False,
  "xaxis": {
    "showgrid": False,
    "title": "two series",
    "zeroline": False
  },
  "yaxis": {
    "gridcolor": "white",
    "title": "Age",
    "zeroline": False
  }
}

output_file = 'dots.html'
fig = Figure(data=data, layout=layout)
plot_url = offplot.plot(fig, filename=output_file)
print("output to: {0}".format(output_file))
