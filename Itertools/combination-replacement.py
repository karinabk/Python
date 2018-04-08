'''Task
You are given a string S and number k. 
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
Input Format
A single line containing the string and integer value separated by a space.
Output Format
Print the combinations with their replacements of string 
on separate lines.
'''

from itertools import combinations_with_replacement



list1 = list(map(str,input().split()))                          #store input as a list of strings
num = int(list1[1])                                             # takes number of letters in one group
result = list(combinations_with_replacement(list1[0],num))      #creates list of combination with replacement of type tuples
result = list(map(list,result))                                 #converts tuples to list
l=[]                                                            #list for storing one permutation 
for i in result:
    i.sort()                                                    #sorting inside the combination
    i="".join(i)                                                #converts from list to string
    l.append(i)
l.sort()                                                        #sorting in order 

print("\n".join(l))                                             #printing on new line
