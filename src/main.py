import numpy as np

from datetime import datetime
from sympy import Matrix, pretty
from sklearn.cluster import KMeans


import read_files
from functions import *
from matrix_functions import *


starts_at = datetime.now()

# Le arquivos e transforma em matriz
path = '../data/areas'
points = read_files.run()


# ---
similarity_matrix = similarity_matrix(points)

# ---
# Ainda nao foram definidos os pesos, usar matriz similaridade ate definicao
adjacency_matrix = similarity_matrix

# ---
diagonal_matrix = diagonal_matrix(adjacency_matrix)

# ---
laplacian_matrix = laplacian_matrix(diagonal_matrix, adjacency_matrix)

np_laplacian_matrix = np.array(laplacian_matrix).astype(np.float64)
np.savetxt('laplacian_matrix.txt', np_laplacian_matrix)


# # ---
# #######################################
# P, D = laplacian_matrix.diagonalize()
# eigenvects = P
# eigenvals = extract_diagonal(D)
# #######################################
# np_laplacian_matrix = np.array(laplacian_matrix).astype(np.float64)
# eigenvals, eigenvects = np.linalg.eig(np_laplacian_matrix)
# #######################################


# ---
# k = 2


# print 'Starting v_matrix at ', str(datetime.now())

# # ---
# v_matrix = v_matrix(k, eigenvects)

# np_v_matrix = np.array(v_matrix).astype(np.float64)
# np.savetxt('v_matrix.txt', np_v_matrix)

ends_at = datetime.now()
process_time_in_seconds = (ends_at - starts_at).total_seconds()
print 'It takes', process_time_in_seconds, 'seconds to process', len(points), 'points'

# ---
# Calcula k-means
# data = np.array(v_matrix.tolist())

# kmeans = KMeans(n_clusters=k).fit(data)


# bench_k_means(KMeans(init='k-means++', n_clusters=k, n_init=10), name="k-means++", data=data)


# print "Done!"
