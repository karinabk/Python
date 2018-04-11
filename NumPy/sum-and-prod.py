'''Task 
You are given a 2-D array with dimensions N X M. 
Your task is to perform the sum tool over axis 0
and then find the product of that result.'''


import numpy as np

num=list(input().split())
list1=[]
for i in range(int(num[0])):
    list1.append(list(map(int,input().split())))
arr=np.array(list1)
arr = np.sum(arr, axis=0)
arr = np.prod(arr, axis=None)
print(arr)
