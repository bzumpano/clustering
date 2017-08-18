import unittest
import sys

sys.path.append('../src')

from sympy import Matrix, pretty
from matrix_functions import *

class TestMatrixFunctions(unittest.TestCase):

  def test_similarity_matrix(self):
    points = [
      [0, 0, 0],
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1],
      [1, 1, 0],
      [1, 0, 1],
      [1, 1, 1],
      [0, 1, 1]
    ]
    expected = Matrix([
      [1, 1, 1, 1, 0, 0, 0, 0],
      [1, 1, 0, 0, 1, 1, 0, 0],
      [1, 0, 1, 0, 1, 0, 0, 1],
      [1, 0, 0, 1, 0, 1, 0, 1],
      [0, 1, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 1, 0],
      [0, 0, 0, 0, 1, 1, 1, 1],
      [0, 0, 1, 1, 0, 0, 1, 1]
    ])

    result = similarity_matrix(points)
    self.assertEqual(result, expected)



  def test_diagonal_matrix(self):
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
      [4, 0, 0, 0, 0, 0, 0, 0],
      [0, 4, 0, 0, 0, 0, 0, 0],
      [0, 0, 4, 0, 0, 0, 0, 0],
      [0, 0, 0, 4, 0, 0, 0, 0],
      [0, 0, 0, 0, 4, 0, 0, 0],
      [0, 0, 0, 0, 0, 4, 0, 0],
      [0, 0, 0, 0, 0, 0, 4, 0],
      [0, 0, 0, 0, 0, 0, 0, 4]
    ])

    result = diagonal_matrix(adjacency_matrix)
    self.assertEqual(result, expected)





  def test_laplacian_matrix(self):
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

    result = laplacian_matrix(diagonal_matrix, adjacency_matrix)
    self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
