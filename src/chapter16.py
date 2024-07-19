

import numpy as np

def my_ls_params(f, x, y):
    m = len(f)
    n = len(x)
    
    A = np.zeros((n, m))
    for j in range(m):
        A[:, j] = f[j](x)
    
    ATA = np.dot(A.T, A)
    ATy = np.dot(A.T, y)
    
    beta = np.linalg.solve(ATA, ATy)
    
    return beta



