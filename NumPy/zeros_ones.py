'''Task 
You are given the shape of the array in the form of space-separated integers,
each integer representing the size of different dimensions,
your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.'''


import numpy as np 

N,M,P = map(int,input().split())
arr=[]
for _ in range(P):
    arr.append(np.zeros((N,M),dtype= np.int))
arr=np.array(arr)
print(arr)
arr=[]
for _ in range(P):
    arr.append(np.ones((N,M),dtype= np.int))
arr=np.array(arr)
print(arr)

