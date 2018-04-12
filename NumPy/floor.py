'''Task 
You are given a 1-D array, A. Your task is to print the floor, 
ceil and rint of all the elements of A.''' 

import numpy as np

np.set_printoptions(sign=' ')

a =np.array([input().split()],np.float32)

print(np.floor(a)[0])
print(np.ceil(a)[0])
print(np.rint(a)[0])
