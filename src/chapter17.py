
import numpy as np

def my_lin_interp(x, y, X):
    Y = []
    for x_val in X:
        for j in range(len(x) - 1):
            if x[j] <= x_val < x[j + 1]:
                y_val = y[j] + (y[j + 1] - y[j]) * (x_val - x[j]) / (x[j + 1] - x[j])
                Y.append(y_val)
                break
        else:
            if x_val == x[-1]:
                Y.append(y[-1])
    return Y


def my_cubic_spline(x, y, X):
    n = len(x)
    h = np.diff(x)
    delta = np.diff(y) / h
    A = np.zeros((n, n))
    b = np.zeros(n)
    A[0, 0] = 1
    A[-1, -1] = 1

    for i in range(1, n-1):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        b[i] = 3 * (delta[i] - delta[i-1])
    c = np.linalg.solve(A, b)
    a = y[:-1]
    b = delta - h * (2*c[:-1] + c[1:]) / 3
    d = (c[1:] - c[:-1]) / (3 * h)
    
    Y = np.zeros_like(X)
    for i, xi in enumerate(X):
        j = np.searchsorted(x, xi) - 1
        j = max(0, min(j, n-2))
        
        dx = xi - x[j]
        Y[i] = a[j] + b[j]*dx + c[j]*dx**2 + d[j]*dx**3
    
    return Y


