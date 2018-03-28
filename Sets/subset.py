#You are given two sets, A and B. 
#Your job is to find whether set A is a subset of set B.
#If set A is subset of set B, print True.
#If set A is not a subset of set B, print False.

if __name__=='__main__':
    n=int(input()) # number of tests
    for i in range(n):
        m=input() # number of elements in set A
        list1= list(map(int,input().split()))
        set1=set()
        set1.update(list1) # creating a set A
        
        k = input() # number of elements in set B
        list2= list(map(int,input().split()))
        set2=set()
        set2.update(list2) # creating a set B
        
        print(set1.issubset(set2))
        
