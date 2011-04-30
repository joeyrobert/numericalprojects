# lorenz_visual.py - Graphing the Lorenz equation
# Author: Joey Robert <joey@joeyrobert.org>

import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = []; y = []; z = []
reader = csv.reader(open('result.txt'))

for row in reader:
    x.append(float(row[0]))
    y.append(float(row[1]))
    z.append(float(row[2]))

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x, y, z)
fig.suptitle('Lorenz Attractor')
Axes3D.set_xlabel(ax, 'x')
Axes3D.set_ylabel(ax, 'y')
Axes3D.set_zlabel(ax, 'z')
fig.savefig('result.png')
