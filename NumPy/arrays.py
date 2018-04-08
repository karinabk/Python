'''Task

You are given a space separated list of numbers. 
Your task is to print a reversed NumPy array with the element type float.

Input Format

A single line of input containing space separated numbers.

Output Format

Print the reverse NumPy array with type float.'''


import numpy as np

def arrays(arr):
    # complete this function
    # use numpy.array 
    return np.array(list(reversed(arr)),float)
    
    
    
arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
