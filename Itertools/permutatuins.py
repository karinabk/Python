#Task 
#You are given a string S. 
#Your task is to print all possible permutations of size k of the string in lexicographic sorted order.



from itertools import permutations

string = list(map(str,input().split()))
n = int(string[1])

result = list(permutations(string[0],2))
result = list(map(str,result))
out=[]
for i in result:
    i=list(map(str,i))
    out.append(i[2])
    out.append(i[7])
    print(out)
    
    #DOES NOT WORK YET
