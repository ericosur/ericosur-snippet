#!/usr/bin/env python
#!/Users/ericosur/anaconda/bin/python

from plotly.offline import plot
import plotly.graph_objs as go

#import numpy as np

#y0 = np.random.randn(40)-1.5
y0 = [0.22,-0.87,-2.39,-1.79,0.37,-1.54,1.28,-0.31,-0.74,1.72,0.38,-0.17,-0.62,-1.10,0.30,0.15,2.30,0.19,-0.50,-0.09]
#y1 = np.random.randn(40)+3.1415926535897932
y1= [-5.13,-2.19,-2.43,-3.83,0.50,-3.25,4.32,1.63,5.18,-0.43,7.11,4.87,-3.10,-5.81,3.76,6.31,2.58,0.07,5.76,3.50]
trace0 = go.Box(
    y=y0
)
trace1 = go.Box(
    y=y1
)

output_file = 'box.html'
data = [trace0, trace1]
plot(data, filename=output_file)
print("output to: {0}".format(output_file))
