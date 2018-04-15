'''Task 
You are the manager of a supermarket. 
You have a list of N items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence. 
item_name = Name of the item. 
net_price = Quantity of the item sold multiplied by the price of each item.
Input Format
The first line contains the number of items, N. 
The next N lines contains the item's name and price, separated by a space.

Output Format
Print the item_name and net_price in order of its first occurrence.'''



from collections import OrderedDict

d={}
d=OrderedDict()
items=[]
N = int(input())
for k in range(N):
    items.append(list(map(str,input().split())))
    if not items[k][1].isdigit():                         # putting together name of item if it consists of two words
        temp_list=[]
        temp_list.append(items[k][0])
        temp_list.append(items[k][1])
        items[k][0]=' '.join(temp_list)
        items[k].remove(items[k][1])

for i in range(len(items)):                               #finding net price of items or adding it to dictionary if it does not have it
    if items[i][0] in d.keys():
        d[items[i][0]]+=int(items[i][1])
    else:
        d[items[i][0]]=int(items[i][1])
d=list(d.items())
d = [list(l) for l in d]
for g in d:
    print(' '.join(map(str,g)))
