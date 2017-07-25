
def run(adjacency_matrix):
  matrix = []

  for i in range(0, len(adjacency_matrix)):
    row = adjacency_matrix[i]
    matrix.append(adjacency_row(i, sum(row), len(row)))

  return matrix



def adjacency_row(position, value, column_size):
  row = []

  for i in range(column_size):
    row.append(value if i == position else 0)

  return row
