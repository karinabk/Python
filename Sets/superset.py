#You are given a set A and n other sets. 
#Your job is to find whether set A is a strict superset of each of the 
#N sets. Print True, if A is a strict superset of each of the 
#N sets. Otherwise, print False. 
#A strict superset has at least one element that does not exist in its subset. 

if __name__=='__main__':
    set1=set(map(int,input().split())) #set A
    n = int(input()) # number of other sets
    boolean = True
    for i in range(n):
        set2=set(map(int,input().split())) # Set for checking
        if not set1.issuperset(set2):
            boolean = False
    print(boolean)
