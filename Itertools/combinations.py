'''Task

You are given a string S. 
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
Input Format

A single line containing the string S and integer value k separated by a space.'''

from itertools import combinations

s,k = raw_input().split()

for i in range(1,int(k)+1):
    for j in combinations(sorted(s),i):
        print("".join(j))
