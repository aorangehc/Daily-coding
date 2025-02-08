import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    size = len(A)
    
    x = np.zeros(size)
    
    for _ in range(n):
        x_old = x.copy()
        
        for i in range(size):
            sigma = 0
            for j in range(size):
                if j != i:
                    sigma += A[i][j] * x_old[j]
            x[i] = (b[i] - sigma) / A[i][i]
        
        x = np.round(x, 4)
    
    return x.tolist()