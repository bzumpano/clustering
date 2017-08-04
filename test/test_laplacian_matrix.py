import unittest

import sys
sys.path.append('../src')

from sympy import Matrix
from laplacian_matrix import run

# L = D - W
class TestLaplacianMatrix(unittest.TestCase):

  def test_diagonal_matrix(self):

    diagonal_matrix = Matrix([
      [4, 0, 0, 0, 0, 0, 0, 0],
      [0, 4, 0, 0, 0, 0, 0, 0],
      [0, 0, 4, 0, 0, 0, 0, 0],
      [0, 0, 0, 4, 0, 0, 0, 0],
      [0, 0, 0, 0, 4, 0, 0, 0],
      [0, 0, 0, 0, 0, 4, 0, 0],
      [0, 0, 0, 0, 0, 0, 4, 0],
      [0, 0, 0, 0, 0, 0, 0, 4]
    ])

    adjacency_matrix = Matrix([
      [1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 0, 0, 1, 1, 0, 0],
      [1, 0, 1, 0, 1, 0, 0, 1],
      [1, 0, 0, 1, 0, 1, 0, 1],
      [0, 1, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 1, 0],
      [0, 0, 0, 0, 1, 1, 1, 1],
      [0, 0, 1, 1, 0, 0, 1, 1]
    ])

    expected = Matrix([
      [ 3, -1, -1, -1,  0,  0,  0,  0],
      [-1,  3,  0,  0, -1, -1,  0,  0],
      [-1,  0,  3,  0, -1,  0,  0, -1],
      [-1,  0,  0,  3,  0, -1,  0, -1],
      [ 0, -1, -1,  0,  3,  0, -1,  0],
      [ 0, -1,  0, -1,  0,  3, -1,  0],
      [ 0,  0,  0,  0, -1, -1,  3, -1],
      [ 0,  0, -1, -1,  0,  0, -1,  3]
    ])

    result = run(diagonal_matrix, adjacency_matrix)
    self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
