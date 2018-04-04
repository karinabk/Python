#Task
#You are given a two lists A and B. Your task is to compute their cartesian product A X B.

from itertools import product

A= list(map(int,input().split()))
B=list(map(int,input().split()))

C = list(product(A,B))
sorted(C)
C = list(map(str, C))
print(" ".join(C))
