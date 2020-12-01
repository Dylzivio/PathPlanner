
# Просто строим карту
from megamap import A
import matplotlib.pyplot as plt
import numpy as np
from searcher import expand_matrix
np.random.seed(19680801)
data = np.random.randn(100, 100)
B = expand_matrix(A)
C = expand_matrix(B)
M = np.array(C)
plt.imshow(M, cmap='cividis', aspect='auto', interpolation='none')
plt.show()



# =========================================================================
# #Строим отработавший алгоритм поиска
# from searcher import expand_matrix, where_unknown, where_your_know
#
# B = [1, 1, 1, 2, 4]
# alfa, error = 90, 0.5
# # f = where_your_know(A, B, alfa, error)
# f = where_unknown(A, B, error)
# B = expand_matrix(A)
# M = np.array(B)
# plt.imshow(f, cmap='viridis', aspect='auto', interpolation='none')
# # plt.imshow(Z, origin='lower', interpolation='none')
# plt.show()
