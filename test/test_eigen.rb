import unittest

import sys
import scipy
sys.path.append('../src')

from sympy import Matrix
import numpy as np


class TestEigen(unittest.TestCase):

  def test_eigen(self):

    input = Matrix([
      [ 5, -2,  0, -3],
      [-2,  5, -3,  0],
      [ 0, -3,  5, -2],
      [-3,  0, -2,  5]
    ])

    expected_eigenval = [0, 4, 6, 10]
    expected_eigenvect = [
      [ 1,  1,  1, 1],
      [ 1, -1, -1, 1],
      [-1, -1,  1, 1],
      [-1,  1, -1, 1]
    ]

    np_input = np.array(input).astype(np.float64)
    # w, v = np.linalg.eig(np_input)
    # w = np.linalg.eigvals(np_input)
    # v = np.linalg.eigvals(np_input)

    w, v = scipy.linalg.eigh(np_input)

    print input.tolist() == np_input.tolist()
    print w
    print v

    self.assertEqual(np.sort(w.astype(np.int64)).tolist(), expected_eigenval)
    self.assertEqual(v.astype(np.int64).tolist(), expected_eigenvect)



if __name__ == '__main__':
    unittest.main()
