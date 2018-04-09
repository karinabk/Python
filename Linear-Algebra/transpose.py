#Transpose function for square matrices on pure python
#now it works for non square matrices


matrix=[[0,2,1,3,5],
        [1,-2,-3,4,5],
        [-1,1,2,5,3],
        [4,5,6,7,6]]

def transpose(matrix):
    new_matrix=[]
    for i in range(len(matrix[0])):
        new_matrix.append([])
    for x in range(len(matrix[0])):
        for k in range(len(matrix)):
            new_matrix[x].append(matrix[k][x])
    return new_matrix
    
print(transpose(matrix))
