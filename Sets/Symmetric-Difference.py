#Task 
#Given 2 sets of integers, M and N,
#print their symmetric difference in ascending order. 
#The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
#Output the symmetric difference integers in ascending order, one per line.

if __name__ == '__main__':
    n = int(input())
    list1=list(map(int,input().split()))
    mySet=set()
    mySet.update(list1)
    m = int(input())
    mySet2=set()
    list2 = list(map(int,input().split()))
    mySet2.update(list2)
    
    setResult=set()
    setResult = mySet.difference(mySet2).union(mySet2.difference(mySet))
    setResult=sorted(setResult)
    for i in setResult:
        print(i)
        
