from math import sqrt
from sympy import Matrix

from sklearn.neighbors import NearestNeighbors

import numpy as np

# Mede a distancia de 2 pontos a(xa, ya) e b(xb, yb)
def distance(a, b):
  dist = np.linalg.norm(np.array(a) - np.array(b))
  return dist


#
# Determina valor de similaridade entre pontos
#
# Returns:
#   1, se distance(a, b) < epsilon
#   0, c.c
#
def epsilon_neighborhood(a, b):
  epsilon = 1.1
  dist = distance(a, b)

  return 1 if dist < epsilon else 0



def run(points):
  X = np.array(points)

  k = len(points) / 2

  print ' K-nearest value:', k
  nbrs = NearestNeighbors(n_neighbors=k).fit(X)

  # print distances
  return Matrix(nbrs.kneighbors_graph(X).toarray())
  # dimen = len(points)

  # return  Matrix(dimen, dimen, lambda i, j: epsilon_neighborhood(points[i], points[j]))
