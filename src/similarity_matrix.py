from math import sqrt

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
# Regra:
#
# Returns:
#   1, se distance(a, b) < epsilon
#   0, c.c
#
def similarity_value(dist):
  epsilon = 1.1

  return 1 if dist < epsilon else 0



def run(points):
  matrix = []

  for i in range(0, len(points)):
    row = []

    for j in range(0, len(points)):
      dist = distance(points[i], points[j])
      row.append(similarity_value(dist))

    matrix.append(row)

  return matrix

