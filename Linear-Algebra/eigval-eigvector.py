#Given the matrix below, find the eigenvalues (name these variable eig1 and eig2). 
#For each eigenvalue find its eigenvector (call these variables eigenvector1 and eigenvector2).

#    1    4
#    3    5

#Don't forget to create the matrix above.
#Consider the rotation matrix for two dimensions.
#(for example - we see that for zero degrees this matrix is just a 2-by-2 identity matrix.) 
#Find the eigenvalues for a 45 degree rotation (call these variables eig_rot1 and eig_rot2).
#For each eigenvalue find its eigenvalue (call these variables eigenvector_rot1 and eigenvector_rot2).


import numpy as np
import math
A=np.matrix([[1,4],
          [3,5]
          ])

eig1,eig2=np.linalg.eigvals(A)
print(eig1,eig2)
B= np.matrix([[math.cos(math.pi/4),-math.sin(math.pi/4)],
              [math.sin(math.pi/4),math.cos(math.pi/4)]])
C = B*A
eig_rot1,eigenvector1=np.linalg.eig(C)
eig_rot2,eigenvector2=np.linalg.eig(C)
print(eigenvector1)
