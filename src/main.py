from sympy import Matrix, pretty
import numpy as np
from sklearn.cluster import KMeans

from functions import *
import similarity_matrix
import diagonal_matrix
import laplacian_matrix
import v_matrix


# TODO Ler dados dos arquivos
points = [[0, 0], [1, 0], [1, 1], [0, 1]]

similarity_matrix = similarity_matrix.run(points)

# TODO Verificar como calcular
adjacency_matrix = Matrix([
  [1, 2, 0, 3],
  [2, 1, 3, 0],
  [0, 3, 1, 2],
  [3, 0, 2, 1]
])

diagonal_matrix = diagonal_matrix.run(adjacency_matrix)

laplacian_matrix = laplacian_matrix.run(diagonal_matrix, adjacency_matrix)

P, D = laplacian_matrix.diagonalize()
eigenvects = P
eigenvals = extract_diagonal(D)

k = int(find_min_diff(eigenvals))

v_matrix = v_matrix.run(k, eigenvects)

# Calcula k-means
data = np.array(v_matrix.tolist())

kmeans = KMeans(n_clusters=k).fit(data)


bench_k_means(KMeans(init='k-means++', n_clusters=k, n_init=10), name="k-means++", data=data)


print "Done!"
