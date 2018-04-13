'''Task
You are given a square matrix A with dimensions N X N.
Your task is to find the determinant.
Input Format
The first line contains the integer N. 
The next N lines contains the N space separated elements of array A.'''


import numpy as np
N = int(input())

A = np.matrix([list(map(float,input().split())) for _ in range(N)])
print(round(np.linalg.det(A),2))
