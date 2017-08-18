import numpy as np
import sklearn

from time import time
from sklearn import metrics

def extract_diagonal(sympy_matrix):
  return np.array(sympy_matrix.tolist()).diagonal()
