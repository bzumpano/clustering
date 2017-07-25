from sympy import Matrix, zeros

def run(k, eigenvectors_matrix):
  return eigenvectors_matrix[:, :k]
