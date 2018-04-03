
#Challenge

#Find the norm of the vector [3, 9, 5, 4] using the actual formula above.
#You should write a function find_norm(v1) that returns this value as a float and then call it on the provided variable n1.
#You should not use scipy, but you may use the math module.

import numpy as np
import math
v=np.array([3,9,5,4])
def find_norm(v1):
    sum=0.0
    for i in v1:
        sum+=pow(i,2)
    result=sum**(1/2)
    return result


n1=find_norm(v)
