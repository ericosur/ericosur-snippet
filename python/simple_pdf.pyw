from matplotlib.mlab import normpdf
import matplotlib.numerix as nx
import pylab as p

x = nx.arange(-4, 4, 0.01)
y = normpdf(x, 0, 1) # unit normal
p.plot(x,y, color='red', lw=2)
p.show()
