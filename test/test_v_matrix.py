import unittest

import sys
sys.path.append('../src')

from sympy import Matrix
from v_matrix import run

class TestVMatrix(unittest.TestCase):

  def test_v_matrix(self):

    k = 2

    eigenvectors_matrix = Matrix([
      [1,  0, -1,  0,  0,  1,  0,  1],
      [1,  0,  0, -1,  0,  0,  1, -1],
      [1, -1,  0,  0,  1,  0,  0, -1],
      [1,  1, -1,  1, -1, -1, -1, -1],
      [1, -1,  1, -1, -1, -1, -1,  1],
      [1,  1,  0,  0,  1,  0,  0,  1],
      [1,  0,  1,  0,  0,  1,  0, -1],
      [1,  0,  0,  1,  0,  0,  1,  1]
    ])

    expected = Matrix([
      [1,  0],
      [1,  0],
      [1, -1],
      [1,  1],
      [1, -1],
      [1,  1],
      [1,  0],
      [1,  0]
    ])

    result = run(k, eigenvectors_matrix)
    self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
