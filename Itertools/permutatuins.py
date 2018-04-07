#Task 
#You are given a string S. and number k
#Your task is to print all possible permutations of size k of the string in lexicographic sorted order.


from itertools import permutations

list1 = list(map(str,input().split()))         #store input as a list of strings
num = int(list1[1])                            # takes number of letters in one group
result = list(permutations(list1[0],num))      #creates list of permutations of type tuples
result = list(map(list,result))                # converts tuples to list
l=[]                                           # list for storing one permutation 
for i in result:
    i="".join(i)                               #converts from list to string
    l.append(i)
l.sort()                                       #sorting in order 
print("\n".join(l))                            #printing on new line
