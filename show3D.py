import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from megamap import A
import pylab
from mpl_toolkits.mplot3d import Axes3D
from searcher import expand_matrix
from matplotlib import cm


# mini
# x = np.arange(0, 30, 1)
# y = np.arange(0, 30, 1)
# X, Y = np.meshgrid(x, y)
# Z = np.array(A)
# Z = Z*(-1)

#max
x = np.arange(0, 120, 1)
y = np.arange(0, 120, 1)
Z = expand_matrix(A)
Z = expand_matrix(Z)
Z = np.array(Z)
Z = Z*(-1)
X, Y = np.meshgrid(x, y)
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1, projection='3d')
# ax.plot_surface(X, Y, Z)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()



