import numpy as np



matrix=np.array([[0,2,1],

        [1,-2,-3],

        [-1,1,2]],dtype = np.float)



matrix2 = [[ 1,  1, -2,  1, 3, -1],

           [ 2, -1,  1,  2, 1, -3],

           [ 1,  3, -3, -1, 2,  1],

           [ 5,  2, -1, -1, 2,  1],

           [-3, -1,  2,  3, 1,  3],

           [ 4,  3,  1, -6, -3, -2]]



def change_rows(matrix, I): 

    for j in range(len(matrix)):

        if matrix[j][0] != 0:
            matrix[0]=matrix[0]+matrix[j]
            I[0]=I[0]+I[j]
            break

    return matrix, I

    

def make_one(list1,list_):

    i=0

    while list1[i]==0:

        i+=1

    temp=list1[i]

    for k in range(i,len(list1)):        

        list1[k]=list1[k]/temp

    list_=list_/temp

    return list1,list_



def make_zero(matrix,I,line):

    i=0    

    while matrix[line][i]==0:

        i+=1

    list2=[]

    I[line]=I[i]*(-1)*matrix[line][i]+I[line]

    for k in range(len(matrix[0])):

        list2.append(matrix[i][k]*matrix[line][i]*(-1))

    for j in range(len(matrix[i])):

        matrix[line][j]=matrix[line][j]+list2[j]

    

    return matrix,I



def make_zero2(matrix,I,line,place):

    

    list2=[]

    I[line]=I[place]*(-1)*matrix[line][place]+I[line]

    for k in range(len(matrix[0])):

        list2.append(matrix[place][k]*matrix[line][place]*(-1))

    for j in range(len(matrix[0])):

        matrix[line][j]=matrix[line][j]+list2[j]

    return matrix,I

    

def elimination(matrix):
    I=np.eye(len(matrix),dtype=float)

    if matrix[0][0] == 0:

        matrix, I = change_rows(matrix, I)
      

    for i in range(len(matrix)):

        matrix[i], I[i] = make_one(matrix[i], I[i])

        if i == len(matrix) - 1 : break

        for j in range(i+1, len(matrix)):

            if matrix[j][i] != 0:

                matrix, I = make_zero(matrix, I, j)

    for k in range(len(matrix) - 2 , -1, -1):

        for l in range(len(matrix) - 1, k, -1):

            matrix, I = make_zero2(matrix, I,k, l)       

            

    return matrix, I



matrix2,inverse = elimination(matrix2)
print(matrix2)
print(inverse)
