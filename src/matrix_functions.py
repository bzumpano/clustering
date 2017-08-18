import numpy as np

from math import sqrt
from sympy import Matrix, diag
from sklearn.neighbors import NearestNeighbors


def similarity_matrix(points):
  X = np.array(points)
  k = len(points) / 2
  nbrs = NearestNeighbors(n_neighbors=k).fit(X)

  return Matrix(nbrs.kneighbors_graph(X).toarray())


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
