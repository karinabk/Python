'''Task 
You are given two integer arrays of size N X P and M X P
(N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.
Input Format
The first line contains space separated integers N, M and P. 
The next N lines contains the space separated elements of the P columns. 
After that, the next M lines contains the space separated elements of the P columns.
Output Format
Print the concatenated array of size (N+M)X P.'''



import numpy as np 
num=list(input().split())
list1=[]
for i in range(int(num[0])):
    list1.append(list(map(int,input().split())))
arr=np.array(list1)
list2=[]
for k in range(int(num[1])):
    list2.append(list(map(int,input().split())))
arr2=np.array(list2)
print(np.concatenate((arr,arr2),axis=0))
