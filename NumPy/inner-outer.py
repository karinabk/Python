'''Task 
You are given two arrays: A and B. 
Your task is to compute their inner and outer product.'''

import numpy as np
A = np.array(list(map(int,input().split())))
B=np.array(list(map(int,input().split())))

print(np.inner(A,B))
print(np.outer(A,B))
