#Initialize your list and read in the value of n
#followed by n lines of commands where each command will be of the 
# 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    list_=[]
    N = int(input())
    for _ in range(N):
        ins = list(input().split())
        if ins[0] == "insert":
            list_.insert(int(ins[1]), int(ins[2]))
        if ins[0]== "print":
            print(list_)
        if ins[0]== "remove":
            list_.remove(int(ins[1]))
        if ins[0]== "append":
            list_.append(int(ins[1]))
        if ins[0]== "sort":
            list_.sort()
        if ins[0]== "pop":
            list_.pop()
        if ins[0]== "reverse":
            list_.reverse()
