#Task
#You have a non-empty set s, and you have to execute N
#commands given in N lines.
#The commands will be pop, remove and discard. 

if __name__=='__main__':
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input()) # number of commands
    for i in range(m):
        list1 = input().split()
        if list1[0]=="remove":
            s.remove(int(list1[1]))
        if list1[0]=="pop":
            s.pop()
        if list1[0]=="discard":
            s.discard(int(list1[1]))
    print(sum(s))
