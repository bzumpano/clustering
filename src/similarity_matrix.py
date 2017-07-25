from math import sqrt
from sympy import Matrix

# Mede a distancia de 2 pontos a(xa, ya) e b(xb, yb)
def distance(a, b):
  xa = a[0]
  xb = b[0]

  ya = a[1]
  yb = b[1]

  dist = sqrt((xa-xb)**2) + ((ya-yb)**2)
  # print('d(%s, %s)=%f' % (str(a), str(b), dist))
  return dist


#
# Determina valor de similaridade entre pontos
#
# Returns:
#   1, se distance(a, b) < epsilon
#   0, c.c
#
def similarity_value(a, b):
  epsilon = 1.1
  dist = distance(a, b)

  return 1 if dist < epsilon else 0



def run(points):
  dimen = len(points)

  return  Matrix(dimen, dimen, lambda i, j: similarity_value(points[i], points[j]))


