import unittest

import sys
sys.path.append('../src')

from similarity_matrix import distance, similarity_value, run

class TestSimilarityMatrix(unittest.TestCase):

  def test_distance(self):
    a = [0, 0]
    b = [1, 0]

    self.assertEquals(distance(a, a), 0)
    self.assertEquals(distance(a, b), 1)


  def test_similarity_value(self):
    epsilon = 1.1

    self.assertEquals(similarity_value(epsilon-1), 1)
    self.assertEquals(similarity_value(epsilon), 0)
    self.assertEquals(similarity_value(epsilon+1), 0)


  def test_similarity_matrix(self):
    points = [[0, 0], [1, 0], [1, 1], [0, 1]]
    expected = [
      [1, 1, 0, 1],
      [1, 1, 1, 0],
      [0, 1, 1, 1],
      [1, 0, 1, 1]
    ]

    self.assertEquals(run(points), expected)



if __name__ == '__main__':
    unittest.main()
