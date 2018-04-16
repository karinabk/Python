
'''There is an array of n integers. There are also 2 disjoint sets, 
A and B, each containing m integers. You like all the integers in set A
and dislike all the integers in set B. Your initial happiness is 0. For each 
i integer in the array, if i is in set A, you add 1 to your happiness. If 
i is in set B, you substruct 1 from your happiness. 
Otherwise, your happiness does not change. Output your final happiness at the end. '''



N,M = map(int,input().split())
arr=list(map(int,input().split()))
setA=set(map(int,input().split()))
setB=set(map(int,input().split()))
happ=0
for i in arr:
    if i in setA:
        happ+=1
    elif i in setB:
        happ-=1
print(happ)



#solution in one line 
print(sum([(i in setA)-(i in setB) for i in arr]))
