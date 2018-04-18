'''Task
The National University conducts an examination of N students in 
X subjects. 
Your task is to compute the average scores of each student.

Sample Input
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
Sample Output
90.0 
91.0 
82.0 
90.0 
85.5       
'''


N,X = map(int,input().split())
num=[]
for _ in range(X):
    num.append(list(map(float,input().split())))

vals=list(zip(*num))

for i in range(N):
    avg=0.0
    for k in range(X):
        avg += vals[i][k]
    print(avg/X)

