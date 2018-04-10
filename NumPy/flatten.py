'''Task 
You are given a N X M integer array matrix with space separated elements 
(N= rows and M= columns). 
Your task is to print the transpose and flatten results.'''


import numpy as np 
N,M=map(int,input().split())
list1=[]
for i in range(N):
    list1.append(list(map(int,input().split())))
arr=np.array(list1)
print(arr.transpose())
print(arr.flatten())
