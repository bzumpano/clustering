import unittest

import sys
sys.path.append('../src')

from sympy import Matrix
from diagonal_matrix import run

class TestDiagonalMatrix(unittest.TestCase):

  def test_diagonal_matrix(self):

    adjacency_matrix = Matrix([
      [1, 2, 0, 3],
      [2, 1, 3, 0],
      [0, 3, 1, 2],
      [3, 0, 2, 1]
    ])

    expected = Matrix([
      [6, 0, 0, 0],
      [0, 6, 0, 0],
      [0, 0, 6, 0],
      [0, 0, 0, 6]
    ])

    self.assertEquals(run(adjacency_matrix), expected)



if __name__ == '__main__':
    unittest.main()
