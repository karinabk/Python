
#Challenge

#Write a function matrix_inverse(matrix_A) that outputs the inverse matrix.



import numpy as np
A=np.matrix([[1,2,3],
             [4,5,6],
             [7,8,9]
             ])

def matrix_inverse(matrix_A):
    if (matrix_A.shape[0]==matrix_A.shape[1] and np.linalg.det(matrix_A)!=0):
        id= np.eye(matrix_A.shape[0])
        inv = np.linalg.solve(A,id)
        return inv

print(matrix_inverse(A))
