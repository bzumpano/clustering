import unittest

import sys
sys.path.append('../src')

from sympy import Matrix, pretty
from similarity_matrix import run

class TestSimilarityMatrix(unittest.TestCase):

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

    self.assertEquals(run(points), expected)



if __name__ == '__main__':
    unittest.main()
