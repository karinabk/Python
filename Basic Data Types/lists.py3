Initialize your list and read in the value of 

followed by 

lines of commands where each command will be of the 

types listed above. Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    list_=[]
    N = int(input())
    for _ in range(N):
        ins = list(str(input()))
        print(ins[:3])
        if ins[:3]==list("ins"):
            print(int(ins[10]))
            list_.insert(int(ins[7], int(ins[9]))
        else if ins[:3]==list("pri"):
            print(list_)
        else if ins[:3]==list("rem"):
            list_.remove(int(ins[7]))
        else if ins[:3]==list("app"):
            list_.append(int(ins[7]))
        else if ins[:3]==list("sor"):
            list_.sort()
        else if ins[:3]==list("pop"):
            list_.pop()
        else if ins[:3]==list("rev"):
            list_.reverse()
