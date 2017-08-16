from sympy import Matrix, pretty
import numpy as np
from sklearn.cluster import KMeans

from functions import *

from datetime import datetime

import similarity_matrix
import diagonal_matrix
import laplacian_matrix
import v_matrix

import read_files

print 'Starting at ', str(datetime.now())


# Le arquivos e transforma em matriz
path = '../data/areas'
files = read_files.all_files(path)

points = read_files.read_csv(files)


# ---
similarity_matrix = similarity_matrix.run(points)

# ---
# Ainda nao foram definidos os pesos, usar matriz similaridade ate definicao
adjacency_matrix = similarity_matrix

# ---
diagonal_matrix = diagonal_matrix.run(adjacency_matrix)


print 'Starting laplacian_matrix at', str(datetime.now())
# ---
#
print 'diagonal_matrix shape:', diagonal_matrix.shape
print 'adjacency_matrix shape:', adjacency_matrix.shape

laplacian_matrix = laplacian_matrix.run(diagonal_matrix, adjacency_matrix)

print 'Ending laplacian_matrix at', str(datetime.now())



# #######################################
# print 'Starting eigenvals at', str(datetime.now())
# # ---
# eigenvals = laplacian_matrix.eigenvals()

# print 'Ending eigenvals at', str(datetime.now())


# print 'Starting eigenvects at', str(datetime.now())
# # ---
# eigenvects = laplacian_matrix.eigenvects()

# print 'Ending eigenvects at', str(datetime.now())
# #######################################




#######################################
print 'Starting eigenvects and eigenvals at ', str(datetime.now())
# ---
P, D = laplacian_matrix.diagonalize()
eigenvects = P
eigenvals = extract_diagonal(D)

print 'Ending eigenvects and eigenvals at ', str(datetime.now())
#######################################




# ---
# k = int(find_min_diff(eigenvals))
k = 2


print 'Starting v_matrix at ', str(datetime.now())

# ---
v_matrix = v_matrix.run(k, eigenvects)

np_v_matrix = np.array(v_matrix).astype(np.float64)
np.savetxt('test.txt', np_v_matrix)

print v_matrix

print 'Ending at ', str(datetime.now())

# ---
# Calcula k-means
# data = np.array(v_matrix.tolist())

# kmeans = KMeans(n_clusters=k).fit(data)


# bench_k_means(KMeans(init='k-means++', n_clusters=k, n_init=10), name="k-means++", data=data)


# print "Done!"
