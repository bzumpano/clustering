import unittest

import sys
sys.path.append('../src')

from sympy import Matrix
from diagonal_matrix import run

class TestDiagonalMatrix(unittest.TestCase):

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

    self.assertEquals(run(adjacency_matrix), expected)



if __name__ == '__main__':
    unittest.main()
