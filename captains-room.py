


if __name__=='__main__':
    n=int(input()) # number of persons per family
    list1=list(map(int,input().split())) # all people 
    set1=set()
    set1.update(list1)
    for i in list1:
        if len(set1)==1:
            break
        set1.remove(i)
    listResult = list(set1)
    print(listResult[0])
    
    
    #does not work yet
