#Transpose function for square matrices on pure python

matrix=[[0,2,1],
        [1,-2,-3],
        [-1,1,2]]

def transpose(matrix):
    for i in range(len(matrix)):
        for k in range(i,len(matrix[0])):
            
            temp = matrix[i][k]
            print(temp)
            matrix[i][k]=matrix[k][i]
            matrix[k][i]=temp
    print(matrix)
    
transpose(matrix)
