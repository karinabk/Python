#TASK
#You are given a set A and N 
#number of other sets. These N number of sets have to perform some specific mutation operations on set A.
#Your task is to execute those operations and print the sum of elements from set A.
#Input Format
#The first line contains the number of elements in set A.
#The second line contains the space separated list of elements in set A.
#The third line contains integer N, the number of other sets.
#The next 2*N lines are divided into N parts containing two lines each.
#The first line of each part contains the space separated entries of the operation name and the length of the other set.
#The second line of each part contains space separated list of elements in the other set.

if __name__=='__main__':
    n = int(input()) # number of elements in A
    list1 = list(map(int,input().split())) # list A
    set1=set() # set A
    set1.update(list1) # place values from list A  in set A
    m = int(input()) # number of sets
    
    for i in range(m):
        operation =list(input().split())
        list2 = list(map(int,input().split()))
        set2=set()
        set2.update(list2)
        if operation[0]=="intersection_update":
            set1.intersection_update(set2)
        if operation[0]=="update":
            set1.update(set2)
        if operation[0]=="symmetric_difference_update":
            set1.symmetric_difference_update(set2)
        if operation[0]=="difference_update":
            set1.difference_update(set2)
    print(sum(set1))
