import numpy as np

def my_bin_2_dec(b):
    degree = 0;
    sum = 0;

    for bit in b:
        sum += 2**degree * bit
        degree += 1

    return sum

print(my_bin_2_dec([1,0,1,0,1,0,1]))




