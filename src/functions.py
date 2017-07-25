import numpy as np
import sklearn

from time import time
from sklearn import metrics

def extract_diagonal(sympy_matrix):
  return np.array(sympy_matrix.tolist()).diagonal()


# Retorna a menor diferenca entre dois valores consecutivos
#
# Parametros:
#   val_array: Vetor com os valores
#
def find_min_diff(val_array):
  return min(np.diff(val_array))

#
# @see <a href="http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html" />
#
def bench_k_means(estimator, name, data):
    t0 = time()
    estimator.fit(data)
    print('% 9s   %.2fs    %i   %.3f   %.3f   %.3f   %.3f   %.3f    %.3f'
          % (name, (time() - t0), estimator.inertia_,
             metrics.homogeneity_score(estimator.labels_, estimator.labels_),
             metrics.completeness_score(estimator.labels_, estimator.labels_),
             metrics.v_measure_score(estimator.labels_, estimator.labels_),
             metrics.adjusted_rand_score(estimator.labels_, estimator.labels_),
             metrics.adjusted_mutual_info_score(estimator.labels_,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean',
                                      sample_size=300)))
