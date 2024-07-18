import numpy as np

def my_bin_2_dec(b):
    degree = 0;
    sum = 0;

    for bit in b:
        sum += 2**degree * bit
        degree += 1

    return sum


def my_dec_2_bin(num):
    if num == 0: 
        return [0]
    bin = []
    while num > 0:
        bin.append(num%2)
        num = num // 2
    bin.reverse()

    return bin


def my_ieee_2_dec(s):
    sign_bit = int(s[0])
    exp_bits = s[1:12]
    after_bits = s[12:]

    sign = (-1) * sign_bit
    exp = int(exp_bits,2) - 1023
    after_point = 1
    for i,bit in enumerate(after_bits):
        after_point += int(bit) * 2 **(-(i+1))

    dec = sign * after_point * 2**exp

    return dec


        
