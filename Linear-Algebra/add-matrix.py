
#Challenge

#Write a function matrix_add(matrix_A, matrix_B) that performs matrix addition if the dimensionality is valid. 
#Note that the dimensionality is only valid if input matrix A and input matrix B are of the same
# dimension in both their row and column lengths.

#For example, you can add a 3x5 matrix with a 3x5 matrix, but you cannot add a 3x5 matrix with a 3x1 matrix. 
#If the dimensionality is not valid, print this error message
#"Cannot perform matrix addition between a-by-b matrix and c-by-d matrix",
#where you substitute a, b with the dimension of the input matrix A, and c,d with the dimension of the input matrix B.


import numpy as np
A=np.matrix([[1,2,3],
             [4,5,6],
             [7,8,9]
             ])
B=np.matrix([[3,1],
              [2,-2],
              [1,2]
              ])

def matrix_add(matrix_A,matrix_B):
    if (matrix_A.shape[0]==matrix_B.shape[0] and matrix_A.shape[1]==matrix_B.shape[1]):               
        X=np.empty(shape=[matrix_A.shape[0],matrix_A.shape[1]])
        for x in range(matrix_A.shape[0]):
            for y in range(matrix_A.shape[1]):
                X[x][y]=matrix_A.item((x, y))+matrix_B.item((x,y))         
        return X
    print("Cannot perform matrix addition between {0}-by-{1} matrix and {2}-by-{3} matrix".format(matrix_A.shape[0],matrix_A.shape[1],matrix_B.shape[0],matrix_B.shape[1]))                  

print(matrix_add(A,B))
