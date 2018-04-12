'''Task 
You are given a 2-D array of size N X M. 
Your task is to find:
The mean along axis 1
The var along axis 0
The std along axis None'''





import numpy as np

np.set_printoptions(sign=' ')
N,M = map(int,input().split())

A=np.array([list(map(int,input().split())) for i in range(N)])
print(np.mean(A,axis=1))
print(np.var(A,axis=0))
print(round(np.std(A),12))
