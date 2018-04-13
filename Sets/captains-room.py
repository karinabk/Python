'''Task
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms. 
One fine day, a finite number of tourists come to stay at the hotel. 
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K members per group where K≠1.
The Captain was given a separate room, and the rest were given one room per group.
Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. 
The room numbers will appear K times per group except for the Captain's room. 
Mr. Anant needs you to help him find the Captain's room number. 
The total number of tourists or the total number of groups of families is not known to you. 
You only know the value of K and the room number list.'''





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
    
    
    
  #  does not work yet


    
