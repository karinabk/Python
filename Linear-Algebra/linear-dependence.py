

#Consider a 2-by-2 identity matrix, I. We see that this is a basis of ℜ2 spanned by vectors [1,0] and [0,1]. 
#Solve the unique solution for b = [3,4] - call this sol1.
#Given matix A, compute the determinant - call this det1. Find the inverse of this matrix - call this mat1.
#We see that this is a basis of ℜdim. This is spanned by two vectors, one being [0,1]. What is the other one - call this bas1
#Solve the unique solution for b = [3,4] - call this sol2. 
#Given matix B, compute the determinant - call this det2.
#We see that matrix is noninvertible and the rows are linearly dependent. 
#Infact we see this matrix is reducible if we perform the following operation on row 2: alpha x row 1 - row 2. 
#What is the value of alpha? alpha equals 2

import numpy as np

A=[[1,1],[0,1]]
B =[[1,2],[3,6]]
I=[[1,0],[0,1]]
b=[3,4]
bas1=[1,1]
sol1= np.linalg.solve(I,b)
det1=np.linalg.det(A)
mat1=np.linalg.inv(A)
sol2=np.linalg.solve(A,b)
det2=np.linalg.det(B)
