from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd

data_files = "./data"

def movingAv(interval, window_size):
  window = np.ones(int(window_size))/float(window_size)
  return np.convolve(interval, window, 'same')

fig,ax = plt.subplots()
for subdir, dirs, files in os.walk(data_files):
  for fname in files:
    if fname.endswith(('.csv')):
      x,y = np.loadtxt("data/%s" % fname, unpack = True, delimiter = ',', skiprows = 1)
      y_av = movingAv(y, 200)
      ax.plot(x,y_av)
      ax.plot(x,y)
plt.show()

