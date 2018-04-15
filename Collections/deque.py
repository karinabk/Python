'''Input Format
The first line contains an integer N, the number of operations. 
The next N lines contains the space separated names of methods and their values. 
Output Format
Print the space separated elements of deque d.'''

from collections import deque

d = deque()
N = int(input())
for i in range(N):
    method=list(map(str,input().split()))

    if method[0]=='append':
        d.append(int(method[1]))
    if method[0]=='appendleft':
        d.appendleft(int(method[1]))
    if method[0]=='pop':
        d.pop()
    if method[0]=='popleft':
        d.popleft()
    if method[0]=='reverse':
        d.reverse()
    if method[0]=='remove':
        d.remove(method[1])
    if method[0]=='extend':
        d.extend(method[1])
    if method[0]=='extendleft':
        d.extendleft(method[1])
    
    if method[0]=='rotate':
        d.rotate(int(method[1]))
    if method[0]=='clear':
        d.clear()
print(' '.join(str(x) for x in d))
