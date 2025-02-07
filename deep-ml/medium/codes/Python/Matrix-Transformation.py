import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    A = np.array(A)
    T = np.array(T)
    S = np.array(S)

    if T.shape[0] != T.shape[1] or S.shape[0] != S.shape[1]:
        return -1
    
    det_T = np.linalg.det(T)
    det_S = np.linalg.det(S)
    
    if det_T == 0 or det_S == 0:
        return -1
    
    T_inv = np.linalg.inv(T)
    
    result = np.dot(T_inv, np.dot(A, S))
    
    return result.tolist()