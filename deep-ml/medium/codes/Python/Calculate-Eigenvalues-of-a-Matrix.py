import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a, b = matrix[0]
    c, d = matrix[1]
    
    trace = a + d
    determinant = a*d - b*c
    
    discriminant = trace**2 - 4*determinant
    
    eigenvalue1 = (trace + np.sqrt(discriminant)) / 2
    eigenvalue2 = (trace - np.sqrt(discriminant)) / 2

    return sorted([eigenvalue1, eigenvalue2], reverse=True)