'''Task

Your task is to print an array of size N X M
with its main diagonal elements as 1's and 0's everywhere else.'''

import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))
