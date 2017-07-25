import unittest

import sys
sys.path.append('../src')

from sympy import Matrix
from laplacian_matrix import run

class TestLaplacianMatrix(unittest.TestCase):

  def test_diagonal_matrix(self):

    diagonal_matrix = Matrix([
      [6, 0, 0, 0],
      [0, 6, 0, 0],
      [0, 0, 6, 0],
      [0, 0, 0, 6]
    ])

    adjacency_matrix = Matrix([
      [1, 2, 0, 3],
      [2, 1, 3, 0],
      [0, 3, 1, 2],
      [3, 0, 2, 1]
    ])

    expected = Matrix([
      [5, -2, 0, -3],
      [-2, 5, -3, 0],
      [0, -3, 5, -2],
      [-3, 0, -2, 5]
    ])

    result = run(diagonal_matrix, adjacency_matrix)
    self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
