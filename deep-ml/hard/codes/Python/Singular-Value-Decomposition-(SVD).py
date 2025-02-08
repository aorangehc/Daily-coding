import numpy as np 
def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    if A.shape != (2, 2):
        raise ValueError("Matrix must be 2x2")

    ATA = A.T @ A
    
    J = np.eye(2)
    
    max_iter = 1000
    tol = 1e-10
    for _ in range(max_iter):
        theta = 0.5 * np.arctan2(2 * ATA[0, 1], ATA[0, 0] - ATA[1, 1])
        
        J = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
        
        ATA = J.T @ ATA @ J
        
        if abs(ATA[0, 1]) < tol:
            break
    
    sigma1 = np.sqrt(ATA[0, 0])
    sigma2 = np.sqrt(ATA[1, 1])
    
    Sigma = np.diag([sigma1, sigma2])
    
    V = J
    
    U = A @ V @ np.linalg.inv(Sigma)
    
    return U, (sigma1, sigma2), V.T
