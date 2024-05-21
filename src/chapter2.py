import numpy as np

array = np.linspace(-10,10,num=100)

array_a = np.array([-1,0,1,2,0,3])

y = np.array([[3,5,3],[2,2,5],[3,8,9]])

print(y.transpose())

zero = np.zeros((2,4))
print(zero)

zero[:,1] = 1
print(zero)


s = '123'
n = float(s)

s2 = 'hello'
s1 = 'HELLO'

print(s1 == s2)
print(s1.lower() == s2)

def countString(s):
    print("The world " + s + " has " + len(s).__str__() + " letters")

countString('Engineering')
countString('book')

s = 'Python is great!'

print('Python' in s)

arr = s.split()
print(arr[2])

list_a = [1,8,9,15]

list_a.insert(1,2)
list_a.append(4)
list_a.sort()
print(list_a)
