import numpy as np
from scipy import optimize

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

    



def my_bisection(f, a,b, tol):

    max_iter = 1000 
    for _ in range(max_iter):
        m = (a + b) / 2
        if abs(f(m)) < tol:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    
    return []

def f(x,y=5):
    return (x**3+7)

print(my_bisection(f,5,-5,1e-1))
print(optimize.bisect(f,5,-5,1e-1))

#Q3: Bisection method fail for 1/x because it dosen't converge - 1/x goes to infinity, and we don't have a right bound / left bound(not continuous.).

def my_newton(func,df,x0,tol):
    itmax = 10
    i = 2
    x = x0
    h = func(x) / df(x)
    points = []
    while abs(h)> tol and i < itmax:
        points.append(x)
        h = func(x)/df(x)
        x = x-h
        i = i+1
    return points

fx = lambda x:np.sin(x)-np.cos(x)
df = lambda x:np.cos(x)+np.sin(x)

print(fx(1))
print(my_newton(fx,df,1,1e-5))
print(optimize.newton(fx,1))













