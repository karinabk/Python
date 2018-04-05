
#Challenge
#Write a function matrix_det(matrix_A) that calculates the determinant (an integer) of matrix A if it is a 1x1 or 2x2 matrix.
#If the input matrix is not square, print this error message "Cannot calculate determinant of a non-square matrix."
#If the input matrix is square but has a higher dimension, 
#print the error message "Cannot calculate determinant of a n-by-n matrix", 
#where you substitute n with the dimension of the input matrix.





import numpy as np
A=np.matrix([[1,4,4],
             [4,3,2],
             [4,3,3]])


def matrix_det(matrix_A):
    if matrix_A.shape[0]!=matrix_A.shape[1]:
        print("Cannot calculate determinant of a non-square matrix.")
    elif(matrix_A.shape[0]>2):
        print( "Cannot calculate determinant of a {0}-by-{1} matrix".format(matrix_A.shape[0],matrix_A.shape[1]))            
    elif(matrix_A.shape[0]==matrix_A.shape[1] and matrix_A.shape[0]<3):
        
       
        if matrix_A.shape[0]==1:
            return matrix_A.item(0)
        result= matrix_A.item(0,0)*matrix_A.item(1,1)-matrix_A.item(0,1)*matrix_A.item(1,0)
        return result
print(matrix_det(A)) 
