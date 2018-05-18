import numpy as np

matrix=np.array([[0,2,1],
        [1,-2,-3],
        [-1,1,2]],dtype = np.float)

def transpose(matrix):

    new_matrix=[]

    for i in range(len(matrix[0])):

        new_matrix.append([])

    for x in range(len(matrix[0])):

        for k in range(len(matrix)):

            new_matrix[x].append(matrix[k][x])

    return new_matrix


def inverse(A):
    B = np.array(A,dtype = np.float)
    
    B[0][0]=A[1][1]*A[2][2]-A[1][2]*A[2][1]
    B[0][1]=-(A[1][0]*A[2][2]-A[1][2]*A[2][0])
    B[0][2]=A[1][0]*A[2][1]-A[1][1]*A[2][0]
    B[1][0]=-(A[0][1]*A[2][2]-A[0][2]*A[2][1])
    B[1][1]=A[0][0]*A[2][2]-A[0][2]*A[2][0]
    B[1][2]=-(A[0][0]*A[2][1]-A[0][2]*A[2][0])
    B[2][0]=A[0][1]*A[1][2]-A[0][2]*A[1][1]
    B[2][1]=-(A[0][0]*A[1][2]-A[0][2]*A[1][0])
    B[2][2]=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    print(B)
    B=np.array(transpose(B))
    
    print((1/np.linalg.det(A))*B)
    
inverse(matrix)
