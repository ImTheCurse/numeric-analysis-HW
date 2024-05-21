import math
import unittest

def factorial(n):
    return math.factorial(n)

def leapYear(year):
    div_by_4 = year / 4
    div_by_100 = year / 100
    div_by_400 = year / 400
   
    if div_by_4.is_integer() and not div_by_100.is_integer():
        return True

    if div_by_4.is_integer() and div_by_100.is_integer() and div_by_400.is_integer():
        return True

    return False


def estimate_pi(N):
    p = 2 * math.sqrt(2) / 9801
    t = 0
    i = 0

    while N > 0:
        t += factorial(i * 4) * (1103 + 26390 * i) / pow(factorial(i),4) * pow(396,4 * i)
        N -= 1
    return p * t


def computeSin87():
    print(math.sin(87))

#Question 19: when p is false

def xor(p,q):
    return not p and q or p and not q



class TestTrig(unittest.TestCase):


    def test_trig(self):
        self.assertEqual(round(pow(math.sin(math.pi),2) + pow(math.cos(math.pi),2)),1)
        n = 2
        while n != 6:
            x = math.pi / n
            first = pow(math.sin(x),2) + pow(math.cos(x),2)
            self.assertEqual(round(first), 1)
            n += 2

unittest.main()
