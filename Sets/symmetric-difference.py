#You are given two sets of student roll numbers. 
#One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper.
#Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.


if __name__=='__main__':
    n = int(input()) # number of elements in English
    list1 = list(map(int,input().split())) 
    set1=set()
    set1.update(list1) # replace values in set
    m = int(input()) # number of elements in French
    list2 = list(map(int,input().split()))
    set2=set()
    set2.update(list2)
    myRes=set()

    myRes= set1.symmetric_difference(set2)

    

    print(len(myRes))
