'''Task

You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

Input Format

A single line of input containing 9 space separated integers.'''

import numpy as np
list_=list(raw_input().split())
arr=np.array(list_,int)
print(np.reshape(arr,(3,3)))
