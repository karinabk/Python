# Implementation of Gauss_Jordan elimination on pure python 


matrix=[[0,2,1],
        [1,-2,-3],
        [-1,1,2]]
list_=[-8,0,3]

matrix2 = [[ 1,  1, -2,  1, 3, -1],
           [ 2, -1,  1,  2, 1, -3],
           [ 1,  3, -3, -1, 2,  1],
           [ 5,  2, -1, -1, 2,  1],
           [-3, -1,  2,  3, 1,  3],
           [ 4,  3,  1, -6, -3, -2]]
vector = [4, 20, -15, -3 ,16, -27]

def change_rows(matrix, vector): 
    for j in range(len(matrix)):
        if matrix[j][0] != 0 and matrix[j][0] != 0:
            temp_lst = matrix[j]
            temp_lst2 = vector[j]
            matrix[j] = matrix[0]
            vector[j] = vector[0]
            matrix[0] = temp_lst
            vector[0] = temp_lst2
    return matrix, vector
    
def make_one(list1,list_):
    i=0
    while list1[i]==0:
        i+=1
    temp=list1[i]
    for k in range(i,len(list1)):        
        list1[k]=list1[k]/temp
    list_[i]=list_[i]/temp
    return list1,list_

def make_zero(matrix,list_,line):
    i=0    
    while matrix[line][i]==0:
        i+=1
    list2=[]
    list_[line]=list_[i]*(-1)*matrix[line][i]+list_[line]
    for k in range(len(matrix[0])):
        list2.append(matrix[i][k]*matrix[line][i]*(-1))
    for j in range(len(matrix[i])):
        matrix[line][j]=matrix[line][j]+list2[j]
    
    return matrix,list_

def make_zero2(matrix,list_,line,place):
    
    list2=[]
    list_[line]=list_[place]*(-1)*matrix[line][place]+list_[line]
    for k in range(len(matrix[0])):
        list2.append(matrix[place][k]*matrix[line][place]*(-1))
    for j in range(len(matrix[0])):
        matrix[line][j]=matrix[line][j]+list2[j]
    return matrix,list_
    
def elimination(matrix,list_):
    if matrix[0][0] == 0:
        matrix, list_ = change_rows(matrix, list_)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            
    if matrix[0][0]!=1:
        matrix[0],list_=make_one(matrix[0],list_)
    if matrix[1][0]!=0:
        matrix,list_=make_zero(matrix,list_,1)
    if matrix[2][0]!=0:
        matrix,list_=make_zero(matrix,list_,2)
    if matrix[1][1]!=1: 
        matrix[1],list_=make_one(matrix[1],list_)
    if matrix[2][1]!=0:
        matrix,list_=make_zero(matrix,list_,2)
    if matrix[2][2]!=1:
        matrix[2],list_=make_one(matrix[2],list_)
    if matrix[1][2]!=0:
        matrix,list_=make_zero2(matrix,list_,1,2)
    if matrix[0][2]!=0:
        matrix,list_=make_zero2(matrix,list_,0,2)
    if matrix[0][1]!=0:
        matrix,list_=make_zero2(matrix,list_,0,1)
    print(list_)
    print(matrix)
    
        
        

# elimination(matrix,list_)
print(elimination(matrix, list_))



