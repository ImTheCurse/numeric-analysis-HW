import numpy as np


def my_nth_root(x, n, tol):
    r = 4 #this number is inital guess which dosent matter.
    while True:
        r_ = r**n - x
        r_prime = n * r**(n - 1)
        r_new = r - r_ / r_prime
        if abs(r_new - r) < tol:
            break
        r = r_new

    return r



