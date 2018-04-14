'''Task
You are given two arrays A and B. Both have dimensions of N X N. 
Your task is to compute their matrix product.'''


import numpy as np 
N = int(input())
A=np.array([list(map(int,input().split())) for _ in range(N)])
B=np.array([list(map(int,input().split())) for _ in range(N)])
print(np.dot(A,B))
