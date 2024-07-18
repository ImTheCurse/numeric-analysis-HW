import math
import numpy as np

def my_sinh(x):
    return (pow(math.e,x) - pow(math.e,-x))/2


def my_checker_board(n):
    if n == 1:
        return 1
    
    arr = np.zeros((n,n))
    
    for i in range(0,n):
        for j in range(0,n):
            if (i+j)%2 != 0:
                continue
            arr[i][j] = 1


    return arr

def my_triangle(b,h):
    return 0.5 * b * h

def my_split_matrix(m):
    res1 = []
    res2 = []
    for arr in m:
        l1 = []
        l2 = []
        length = len(arr)
        for i in range(0,length):
            if i < length / 2:
               l1.append(arr[i])
               continue
            l2.append(arr[i])
        res1.append(l1)
        res2.append(l2)

    return res1,res2

def my_n_odds(a):
    count = 0
    for x in a:
        if x % 2 ==1:
            count += 1
    return count

def my_twos(m,n):
    return np.full((m,n),2)


x = lambda x,y: x - y

def add_string(s1,s2)->str:
    return s1 + s2




