
def diagonal_matrix(adjacency_matrix):
  matrix = []

  for i in range(0, len(adjacency_matrix)):
    row = adjacency_matrix[i]
    column_size = len(row)
    row_sum = 0

    for j in range(0, column_size):
      row_sum += row[j]

    matrix.append(adjacency_row(i, row_sum, column_size))

  return matrix



def adjacency_row(position, value, column_size):
  row = []

  for i in range(0, column_size):
    row.append(value if i == position else 0)

  return row
