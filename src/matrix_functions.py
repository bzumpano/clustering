import numpy as np

from math import sqrt
from sympy import Matrix, diag
from sklearn.neighbors import NearestNeighbors


def similarity_matrix(points):
  nbrs = kneighbors(points)

  return Matrix(nbrs)


def diagonal_matrix(adjacency_matrix):
  matrix = []
  results = []

  for row in adjacency_matrix.tolist():
    results.append(sum(row))

  return diag(*results)


def laplacian_matrix(diagonal_matrix, adjacency_matrix):
  return diagonal_matrix - adjacency_matrix


def v_matrix(k, eigenvectors_matrix):
  return eigenvectors_matrix[:, :k]



def is_symmetric(M):
  a = np.array(M).astype(np.float64)
  return np.allclose(a, a.T)


def kneighbors(points):
  X = np.array(points)
  length = len(points)
  k = length / 2
  nbrs = NearestNeighbors(n_neighbors=k).fit(X)
  nbrs_graph = nbrs.kneighbors_graph(X).toarray()

  for i in range(length):
      for j in range(i+1, length):
          if nbrs_graph[i][j] != nbrs_graph[j][i]:
              nbrs_graph[i][j] = 1
              nbrs_graph[j][i] = 1

  return nbrs_graph

