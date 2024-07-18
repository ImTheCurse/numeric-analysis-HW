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

def greeting(str1,num):
    return f'hello, my name is {str1}. i am {num} year old'


def my_donut_area(r1,r2):
    r2_area = np.pi * r2**2
    r1_area = np.pi * r1**2
    return  r2_area-r1_area


def my_withing_tolerence(A,a,tol):
    diff = np.array(A)
    diff = [x - a for x in diff]
    return np.where(np.array(diff) > tol,diff,diff)


print(my_withing_tolerence([0,1,2,3],1.5,0.75))














