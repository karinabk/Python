#5.5.2 Challenge

#Create a function called norms which meets the following requirements:
#It must take a list of numbers as array (eg: [[1,1,4],[3,0,-1],[1,1,2]])
#Calculate the matrix norms with p = 1,2 and ∞, Store them in a dictionary object as follows
# {'p1':p1 norm value,'p2':p2 norm value,'pinf':pinf norm value}
#Finally, return this dictionary object


import numpy as np
list_=[[1,1,4],[3,0,-1],[1,1,2]]

def norms(arr):
    array=np.array(arr)
    print(array)
    dictionary={}
    dictionary['p1']=np.linalg.norm(array,1)
    dictionary['p2']=np.linalg.norm(array,2)
    dictionary['pinf']=np.linalg.norm(array,np.inf)
    print(dictionary)
norms(list_)
