#Rupal has a huge collection of country stamps. 
#She decided to count the total number of distinct country stamps in her collection.
#She asked for your help. You pick the stamps one by one from a stack of N country stamps.
#Find the total number of distinct country stamps.




if __name__=='__main__':
    n = int(input())
    mySet=set()
    for _ in range(n):
        mySet.add(input())
    print(len(mySet))
