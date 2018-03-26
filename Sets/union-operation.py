#You are given two sets of student roll numbers.
#One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper.
#The same student could be in both sets. 
#Your task is to find the total number of students who have subscribed to at least one newspaper.

if __name__ == '__main__':
    n = int(input())
    list1=list(map(int,input().split()))
    mySet=set()
    mySet.update(list1)
    m = int(input())
    mySet2=set()
    list2 = list(map(int,input().split()))
    mySet2.update(list2)
    
    setResult =()
    setResult = mySet.union(mySet2)
    print(len(setResult))
