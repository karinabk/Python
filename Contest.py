# https://www.hackerrank.com/contests/hourrank-27/challenges/impressing-the-boss 
# the task and conditions

#!/bin/python3

import os
import sys

#
# Complete the canModify function below.
#
def canModify(a):
    #
    # Write your code here.
    #
    count = 0
    for i in range(len(a)):
        var1=a[i]
        var2=a[i+1]
        if a[i+1]-a[i]<0:
            count +=1
        if i+1==len(a)-1:
            break
    if count <=1:
        return "YES"
    if count>1:
        return "NO"





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        

        a = list(map(int, input().rstrip().split()))

        result = canModify(a)

        fptr.write(result + '\n')

    fptr.close()
