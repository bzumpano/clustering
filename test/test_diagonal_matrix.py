import unittest

import sys
sys.path.append('../src')

from diagonal_matrix import diagonal_matrix

class TestDiagonalMatrix(unittest.TestCase):

  def test_diagonal_matrix(self):

    adjacency_matrix = [
      [1, 2, 0, 3],
      [2, 1, 3, 0],
      [0, 3, 1, 2],
      [3, 0, 2, 1]
    ]

    expected = [
      [6, 0, 0, 0],
      [0, 6, 0, 0],
      [0, 0, 6, 0],
      [0, 0, 0, 6]
    ]

    self.assertEquals(diagonal_matrix(adjacency_matrix), expected)



if __name__ == '__main__':
    unittest.main()
