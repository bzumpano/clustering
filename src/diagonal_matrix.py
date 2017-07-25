from sympy import Matrix, diag

def run(adjacency_matrix):
  matrix = []
  results = []

  for row in adjacency_matrix.tolist():
    results.append(sum(row))

  return diag(*results)
