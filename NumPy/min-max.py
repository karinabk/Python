'''Task 
You are given a 2-D array with dimensions N X M. 
Your task is to perform the min function over axis 1
and then find the max of that.'''


import numpy as np 
N,M = map(int,input().split())
A = np.array([list(map(int,input().split())) for i in range(N)])
minArr=np.min(A,axis=1)
print(np.max(minList))
